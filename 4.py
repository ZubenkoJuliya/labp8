import asyncio


async def process_plant(plant, soaking_time, germination_time, rooting_time):
    print(f"0 Beginning of sowing the {plant} plant")

    print(f"1 Soaking of the {plant} started")
    await asyncio.sleep(soaking_time / 1000)  # Эмуляция времени замачивания
    print(f"2 Soaking of the {plant} is finished")

    print(f"3 Shelter of the {plant} is supplied")
    await asyncio.sleep(germination_time / 1000)  # Эмуляция времени прорастания
    print(f"4 Shelter of the {plant} is removed")

    print(f"5 The {plant} has been transplanted")
    await asyncio.sleep(rooting_time / 1000)  # Эмуляция времени приживания
    print(f"6 The {plant} has taken root")

    print(f"9 The seedlings of the {plant} are ready")


async def sowing(*plants):
    for plant, soaking_time, germination_time, rooting_time in plants:
        await process_plant(plant, soaking_time, germination_time, rooting_time)


# Пример использования
plants = [
    ("Tomato", 3000, 5000, 2000),
    ("Cucumber", 4000, 6000, 2500),
]

asyncio.run(sowing(*plants))
