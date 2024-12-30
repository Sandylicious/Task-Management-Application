def get_todos(filepath="todos.txt"):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(filepath, todos_arg):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = get_todos()
        todos.append(todo)
        write_todos("todos.txt", todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            item = item.title()
            print(f"{index + 1}-{item}")
            # todos.index("xxx")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number -= 1
            new_todo = input("Enter a new todo: ")

            todos = get_todos()
            todos[number] = new_todo + '\n'
            write_todos("todos.txt", todos)
        except ValueError:
            print("Invalid input.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_completed = todos[index].strip("\n").title()
            todos.pop(index)
            # todos.remove("xxx")

            write_todos("todos.txt", todos)

            message = f"Todo [{todo_completed}] was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")

    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid input.")

print("Bye!")



















