todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if 'add' in user_action:
        todo = user_action[4:]

        # method 1 (read from file)
        # file = open("todos.txt", "r")
        # todos = file.readlines()
        # file.close()

        # method 2
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif 'show' in user_action:
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        # method 1 (to remove the extra \n from each todoitem)
        # new_todos = []
        #
        # for item in todos:
        #     new_item = item.strip("\n")
        #     new_todos.append(new_item)

        # method 2
        #new_todos = [item.strip("\n") for item in todos]

        # method 1 & 2
        #for index, item in enumerate(new_todos):

        # method 3
        for index, item in enumerate(todos):
            item = item.strip("\n")
            item = item.title()
            print(f"{index + 1}-{item}")
            # todos.index("xxx")

    elif 'edit' in user_action:
        number = int(user_action[5:])
        number -= 1
        new_todo = input("Enter a new todo: ")

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos[number] = new_todo + '\n'

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        number = int(user_action[9:])

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        index = number - 1
        todo_completed = todos[index].strip("\n").title()
        todos.pop(index)
        # todos.remove("xxx")

        with open("todos.txt", "w") as file:
            file.writelines(todos)

        message = f"Todo [{todo_completed}] was removed from the list."
        print(message)

    elif 'exit' in user_action:
        break

    else:
        print("Invalid input.")

print("Bye!")



















