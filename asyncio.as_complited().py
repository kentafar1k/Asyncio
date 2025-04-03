import asyncio
import random

async def task(n):
    delay = random.randint(1, 5)  # Разное время выполнения
    await asyncio.sleep(delay)
    return f"Задача {n} завершилась за {delay} сек"

async def main():
    tasks = [task(i) for i in range(5)]  # Создаем 5 корутин

    # Запускаем их и обрабатываем по мере завершения
    for coro in asyncio.as_completed(tasks):
        result = await coro
        print(result)

asyncio.run(main())