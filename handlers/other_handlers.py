from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON

router: Router = Router()


# Этот хэндлер будет реагировать на любые сообщения пользователя,
# не предусмотренные логикой работы бота
@router.message()
async def other(message: Message):
    await message.answer(LEXICON['other'])