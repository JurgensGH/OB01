class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        status = 'Выполнено' if self.completed else 'Не выполнено'
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        new_task = Task(description, deadline)
        self.tasks.append(new_task)

    def mark_task_completed(self, task_description):
        for task in self.tasks:
            if task.description == task_description:
                task.mark_completed()

    def get_current_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def __repr__(self):
        return "\n".join([repr(task) for task in self.tasks])

# Пример использования:
manager = TaskManager()
manager.add_task('Закончить проект', '2024-10-10')
manager.add_task('Позвонить клиенту', '2024-10-05')
manager.mark_task_completed('Позвонить клиенту')

print("Текущие задачи:")
for task in manager.get_current_tasks():
    print(task)

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"Товар {item_name} отсутствует в ассортименте.")

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print(f"Товар {item_name} отсутствует в ассортименте.")

    def __repr__(self):
        return f"Магазин: {self.name}, Адрес: {self.address}, Ассортимент: {self.items}"

# Пример использования:
store = Store('Магазин фруктов', 'ул. Примерная, 123')
store.add_item('apples', 0.5)
store.add_item('bananas', 0.75)
store.update_price('apples', 0.6)
print(store.get_price('apples'))  # Выведет: 0.6
store.remove_item('bananas')
print(store)


# Создание трех различных магазинов
store1 = Store('Зеленая лавка', 'ул. Парковая, 10')
store2 = Store('Магазин техники', 'просп. Технологический, 45')
store3 = Store('Книжный уголок', 'ул. Литературная, 7')

# Добавление товаров в магазин "Зеленая лавка"
store1.add_item('carrots', 0.9)
store1.add_item('potatoes', 0.3)
store1.add_item('tomatoes', 1.2)

# Добавление товаров в магазин "Магазин техники"
store2.add_item('laptop', 800)
store2.add_item('smartphone', 600)
store2.add_item('headphones', 100)

# Добавление товаров в магазин "Книжный уголок"
store3.add_item('fiction book', 15)
store3.add_item('notebook', 3)
store3.add_item('pen', 1.5)

# Вывод информации о каждом магазине
print(store1)
print(store2)
print(store3)
