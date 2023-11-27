import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from pytube import YouTube

# Задаем ваши реквизиты от бота
API_TOKEN = 'ТОКЕН'
CHANNEL_ID = 'bunikwar'

# Инициализируем бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Метод для отправки уведомлений
async def send_notification(video_link):
    # Получите ID всех подписчиков вашего канала и отправьте каждому уведомление о новом видео или шорте
    users = ["user_id"] # Пример

    for user in users:
        await bot.send_message(user, f'🎥 Новое видео на канале: {video_link}')

# Метод для проверки наличия новых видео на канале
async def check_new_videos():
    # Здесь ваш код для проверки наличия новых видео на канале
    channel_link = f'https://www.youtube.com/{CHANNEL_ID}'
    # Ваш код для проверки наличия новых видео/шортcов
    await send_notification('https://www.youtube.com/watch?v=VIDEO_ID')

# Хэндлер для проверки новых видео каждые 10 минут
async def run_periodically():
    while True:
        await asyncio.sleep(600)  # Проверяем каждые 10 минут
        await check_new_videos()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(run_periodically())
    # Запуск бота в режиме long-polling
    executor.start_polling(dp, skip_updates=True)