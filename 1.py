import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(0)  # Позволяет другим задачам выполняться
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")


async def main():
    await asyncio.gather(
        factorial("A", 15),
        factorial("B", 7),
        factorial("C", 4),
    )


if __name__ == '__main__':
    asyncio.run(main())

# При использовании asyncio.gather задачи будут выполняться параллельно,
# но порядок завершения может зависеть от времени,
# затраченного на выполнение каждой задачи.
# Таким образом, задачи могут завершаться в любом порядке, не обязательно совпадая с их стартом.
