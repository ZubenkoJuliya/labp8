import asyncio


async def perform_task(name, task_number, preparation_time, defense_time):
    print(f"{name} started the {task_number} task.")
    await asyncio.sleep(preparation_time / 100)  # Эмуляция времени подготовки
    print(f"{name} moved on to the defense of the {task_number} task.")
    await asyncio.sleep(defense_time / 100)  # Эмуляция времени защиты
    print(f"{name} completed the {task_number} task.")


async def interviews(*candidates):
    for name, prep1, defense1, prep2, defense2 in candidates:
        await perform_task(name, 1, prep1, defense1)
        print(f"{name} is resting.")
        await asyncio.sleep(5)  # Время отдыха
        await perform_task(name, 2, prep2, defense2)


# Пример использования
candidates = [
    ("Alice", 200, 100, 300, 150),
    ("Bob", 250, 120, 350, 180),
]

asyncio.run(interviews(*candidates))
