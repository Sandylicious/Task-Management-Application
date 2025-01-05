import functions
import FreeSimpleGUI as sg
import time
import os

# Handle the case when the output file does not exist
if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

# GUI Theme
sg.theme('LightBrown')

# Time
clock = sg.Text("", key="clock")    # we access sg.Text() using key value

# Add to-do
label = sg.Text("Type in a to-do", text_color="Grey")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")
add_button = sg.Button("Add", size=10)

# Edit to-do
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")

# Complete to-do
complete_button = sg.Button("Complete")

# Exit
exit_button = sg.Button("Exit")

# Display window
window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 15))

while True:
    # window.read() returns a tuple made of string and dictionary
    selected_event, values = window.read(timeout=200)    # timeout refreshes time every 200 ms

    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    # print("selected_event:", selected_event)
    # print("values:", values)
    # print("values['todo']:", values["todo"])
    # print("values['todos']:", values["todos"])

    match selected_event:
        case "Add":
            new_todo = values["todo"]
            new_todo = new_todo.strip("\n")

            if new_todo == "":
                continue

            todos = functions.get_todos()
            todos.append(new_todo + "\n")
            functions.write_todos(todos)

            window["todos"].Update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"] + "\n"

                todos = functions.get_todos()
                todo_to_edit_index = todos.index(todo_to_edit)
                todos[todo_to_edit_index] = new_todo

                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select a to-do first.", font=("Helvetica", 14))
        case "Complete":
            try:
                todo_completed = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_completed)

                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select a to-do first.", font=("Helvetica", 14))

        case "todos":
            # update user input window, so it shows the selected to-do from edit window
            window["todo"].update(value=values["todos"][0])

        case "Exit":
            break

        case sg.WINDOW_CLOSED:
            break

window.close()

















