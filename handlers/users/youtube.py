from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Text
from pytube import YouTube
from io import BytesIO

@dp.message_handler(Text(startswith="https"))
async def get_audio(message:types.Message):
  link=message.text
  buffer=BytesIO()
  url=YouTube(link)
  if url.check_availability() is None:
    audio=url.streams.get_audio_only()
    audio.stream_to_buffer(buffer=buffer)
    buffer.seek(0)
    filename=url.title
    await message.answer_audio(audio=buffer, caption=filename) 
  else:
    await message.answer('Xatolik!')

@dp.message_handler(content_types=['url'])
async def asosiy(message:types.Message):
    url=message.text
    await bot.send_message(message.chat.id,"<b>🔁Iltimos kuting sizning so'rovingiz bajarilmoqda!!!</b>",parse_mode='html')
