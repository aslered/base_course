import random

flowers = ["Роза", "Тюльпан", "Мак", "Подсолнух"]
colors = ["красный", "желтый", "белый", "синий", "фиолетовый", "оранжевый"]
flower_colors = dict(zip(flowers, random.choices(colors, k=len(flowers))))

print(flower_colors)
