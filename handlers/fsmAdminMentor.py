from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import ADMINS
from database.bot_db import sql_command_insert


class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.from_user.id in ADMINS:
        if message.chat.type == 'private':
            await FSMAdmin.id.set()
            await message.answer('ID ментора')


async def load_id(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Введите верный id')
    else:
        async with state.proxy() as data:
            data['id'] = message.text
        await FSMAdmin.next()
        await message.answer('Имя ментора')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Направление')


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMAdmin.next()
    await message.answer('Возраст ментора')


async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Введите возраст цифрами')
    elif int(message.text) > 70 or int(message.text) < 5:
        await message.answer('Введите действительный возраст')
    else:
        async with state.proxy() as data:
            data['age'] = message.text
        await FSMAdmin.next()
        await message.answer('Группа')


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
        await message.answer(f'{data["id"]} {data["name"]} {data["direction"]} {data["age"]} {data["group"]}')
    await FSMAdmin.next()
    await message.answer('Верно?')


async def submit(message: types.Message, state: FSMContext):
    if message.text == 'да':
        await sql_command_insert(state)
        await message.answer("Записано")
        await state.finish()
    elif message.text == 'нет':
        await state.finish()
    else:
        await message.answer("Не понял")


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state:
        await state.finish()
        await message.answer("Отменено")


def register_handlers_fsm(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, Text(equals="cancel", ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)
