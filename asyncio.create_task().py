# import asyncio
#
# async def generator():
#     for i in range(3):
#         yield i
#         await asyncio.sleep(1)
#
# async def main():
#     async for value in generator():
#         print(value)
#
# asyncio.run(main())

import asyncio


async def background_task():
    print("Фоновая задача запущена")
    await asyncio.sleep(1)
    print("Фоновая задача завершена")


async def main():
    print("Запуск основной программы")

    # Запускаем корутину, но НЕ ждем её завершения
    asyncio.create_task(background_task())

    print("Основной код продолжает выполняться")
    await asyncio.sleep(3)  # Даем немного времени фоновым задачам
    print("Основной код завершен")


asyncio.run(main())