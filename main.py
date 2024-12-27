todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            # method 1 (read from file)
            # file = open("todos.txt", "r")
            # todos = file.readlines()
            # file.close()

            # method 2
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            # method 1
            # file = open("todos.txt", "w")
            # file.writelines(todos)
            # file.close()

            # method 2
            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case 'show':
            # method 1
            # file = open("todos.txt", "r")
            # todos = file.readlines()
            # file.close()

            # method 2
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
        case 'edit':
            number = int(input("Enter the number of the todo to edit: "))
            number -= 1
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Enter the number of the todo to complete: "))
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos.pop(number - 1)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

            # todos.remove("xxx")
        case 'exit':
            break
        case whatever:
            print("Hey, you entered an unknown command.")

print("Bye!")



















