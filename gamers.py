# Определение класса "Gamer"
# Задание 2. Добавь поле nickname
# Задание 3. Добавь поле email
class Gamer:
    def __init__(self, name, age, nickname, email):
        self.name = name
        self.age = age
        self.nickname = nickname  
        self.email = email
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    # Задание 4. Измени сообщение
    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет. Всегда на связи по {self.email}. Ищи меня в игре по нику {self.nickname}")

# Создание экземпляра класса "Gamer"
gamer1 = Gamer("Иван", 14, "John", "john@gmail.com")

# Добавление игр
gamer1.add_game("Minecraft")
gamer1.add_game("Dota 2")

# Минипрезентация геймера
gamer1.introduce()

# Вывод любимых игр
print(f"{gamer1.name} любит игры: {', '.join(gamer1.games)}")
