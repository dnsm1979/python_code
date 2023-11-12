# 2 задание: класс стека для работы со строками (стек строк)
def menu():
    func_menu = [Stack[self.add_item], Stack.pop_item, Stack.score_ctack, Stack.isEmpty, Stack.isFull, Stack.clear_stack, Stack.peek]
    choice = int(input('1-помещение строки в стек\n'
                       '2-выталкивание строки из стека\n'
                       '3-подсчет количества строк в стеке\n'
                       '4-проверку пустой ли стек\n'
                       '5-проверку полный ли стек\n'
                       '6-очистку стека\n'
                       '7-получение значения без выталкивания верхней строки из стека\n'
                       '0-выход -> '))
    if choice == 0:
        return
    elif 1 <= choice <= 7:
        return func_menu[choice]
    # elif choice == 2:
    #     self.pop_item()
    # elif choice == 3:
    #     return self.score_ctack()
    # elif choice == 4:
    #     return self.isEmpty()
    # elif choice == 5:
    #     return self.isFull()
    # elif choice == 6:
    #     return self.clear_stack()
    # elif choice == 7:
    #     return self.peek()
    else:
        return f'Такого пункта нет!'
class Stack:


    def __init__(self):
        self.stack = []
        self.size = 100

    def add_item(self):
        if self.stack == self.size:
            return f'Стек полон!'
        else:
            item = (input('-> '))
            self.stack.append(item)

    def pop_item(self):
        if self.stack:
            self.stack.pop()

    def show_stack(self):
        return f'Очередь: ', self.stack

    def score_ctack(self):
        print(f'Количество строк в стеке: {len(self.stack)}')
        return self.stack

    def isEmpty(self):
        if len(self.stack) == 0:
            print('Стек пустой!')
            return self.stack
        print('Стек не пустой')
        return self.stack

    def isFull(self):
        if self.stack == self.size:
            print(f'Стек полный!')
            return self.stack
        else:
            print(f'Стек не полный!')
            return self.stack

    def clear_stack(self):
        while len(self.stack) > 0:
            self.stack.pop()
        print(f'Стек очищен! ')
        return self.stack

    def peek(self):
        if len(self.stack) == 0:
            print('Стек пустой')
            return self.stack
        print(self.stack[len(self.stack)-1])
        return self.stack



stack = Stack()
while True:
    menu()