import os
from todostorage import storage_todolist

if os.name in ('nt', 'dos'):
    os.system('cls')
else:
    os.system('clear')

print("Welcome to your todo list, type 'help' for commands!\n")

todolist = storage_todolist

while True:
    inp = input("\n>> ").split()
    if inp == []:
        continue
    if inp[0] == "stop" or inp[0] == "exit":
        with open("todostorage.py", "w") as f:
            f.write("storage_todolist = " + str(todolist))
        break


    if inp[0] == "add":
        if len(inp) == 1:
            print("Please specify what you would like to add.")
        else:
            todolist[' '.join(inp[1:])] = False
            print("Added to todo list!")
    
    elif inp[0] == "show":
        if len(todolist.keys()) == 0:
            print("Todo list is empty!")
        else:
            x = 0
            for i, j in todolist.items():
                print(str(x) + ":", i, end=" ")
                print('| Not done' if not j else '| Done')
                x += 1
    
    elif inp[0] == "done":
        if len(inp) == 1:
            print("Please specify which todo item you want to done.")
        elif not inp[1].isdigit():
            print("Please specify which index you would like to done.")
        elif int(inp[1]) > len(todolist.keys()) - 1:
            print("Out of range.")
        else:
            x = 0
            for i in todolist.keys():
                if x == int(inp[1]):
                    todolist[i] = True
                    break
                x += 1
            print("Checked off todo!")
    
    elif inp[0] == "undone":
        if len(inp) == 1:
            print("Please specify which todo item you want to undone.")
        elif not inp[1].isdigit():
            print("Please specify which index you would like to undone.")
        elif int(inp[1]) > len(todolist.keys()) - 1:
            print("Out of range.")
        else:
            x = 0
            for i in todolist.keys():
                if x == int(inp[1]):
                    todolist[i] = False
                    break
                x += 1
            print("Unchecked todo!")
    
    elif inp[0] == "remove":
        if len(inp) == 1:
            print("Please specify which todo item you want to remove.")
        elif not inp[1].isdigit():
            print("Please specify which index you would like to remove.")
        elif int(inp[1]) > len(todolist.keys()) - 1:
            print("Out of range.")
        else:
            x = 0
            for i in todolist.keys():
                if x == int(inp[1]):
                    del todolist[i]
                    break
                x += 1
            print("Removed from todo list!")
    
    elif inp[0] == "help":
        print("\nCommands:")
        print("stop / exit     | exits the console and saves todo list")
        print("add (todo)      | adds a todo")
        print("remove (todo)   | removes a todo")
        print("done (todo)     | check off a todo")
        print("undone (todo)   | uncheck a todo")
        print("show            | shows todo list\n")

    else:
        print("Unknown command. Please use 'help' for usable commands.")
