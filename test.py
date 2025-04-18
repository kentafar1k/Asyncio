# import asyncio
#
# async def print_hello():
#     await asyncio.sleep(2)
#     print('Hello')
#
# asyncio.run(print_hello())

# import asyncio
#
# async def multiply(n):
#     await asyncio.sleep(1)
#     return n*2
#
# print(asyncio.run(multiply(5)))


"""Task 3"""
# import asyncio
#
#
# async def task1():
#     await asyncio.sleep(1)
#     return "Task 1 done"
#
# async def task2():
#     await asyncio.sleep(1)
#     return "Task 2 done"
#
# async def main():
#     a, b = await asyncio.gather(task1(), task2())
#     print(a)
#     print(b)
#
# asyncio.run(main())

# """TASK 4"""
# import asyncio
# import random
#
# async def get_random_numbers():
#     await asyncio.sleep(0.1)
#     return random.randint(1, 100)
#
# async def main():
#     numbers = [await get_random_numbers() for _ in range(10)]
#     return sum(numbers) // len(numbers)
#
# print(asyncio.run(main()))


import asyncio
import time


async def f1():
    await asyncio.sleep(1)
    print("f1")


async def f2():
    await asyncio.sleep(2)
    print("f2")


async def f3():
    await asyncio.sleep(3)
    print("f3")


async def main():
    task = [
        f1(), f2(), f3()
    ]
    await asyncio.gather(*task)


asyncio.run(main())