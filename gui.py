import functions
import FreeSimpleGUI as sg

# Add to-do
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")
add_button = sg.Button("Add")

# Edit to-do
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")

# Complete to-do
complete_button = sg.Button("Complete")

# Exit
exit_button = sg.Button("Exit")

# Window
window = sg.Window("My To-Do App",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 15))

while True:
    selected_event, values = window.read() # window.read() returns a tuple made of a string and a dictionary
    print("selected_event:", selected_event)
    print("values:", values)
    print("values['todo']:", values["todo"])
    print("values['todos']:", values["todos"])

    match selected_event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

            window["todos"].Update(values=todos)

        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"] + "\n"

            todos = functions.get_todos()
            todo_to_edit_index = todos.index(todo_to_edit)
            todos[todo_to_edit_index] = new_todo

            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Complete":
            todo_completed = values["todos"][0]
            todos = functions.get_todos()
            todos.remove(todo_completed)

            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")

        case "todos":
            # update user input window so it shows the selected to-do from edit window
            window["todo"].update(value=values["todos"][0])

        case "Exit":
            break

        case sg.WINDOW_CLOSED:
            break

window.close()

















