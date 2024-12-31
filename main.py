from functions import get_todos, write_todos

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = get_todos()
        todos.append(todo)
        write_todos(todos)

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
            write_todos(todos)
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

            write_todos(todos)

            message = f"Todo [{todo_completed}] was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")

    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid input.")

print("Bye!")



















