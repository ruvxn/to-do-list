intro = " \n THIS IS YOUR TO DO LIST APP"
print(intro.title())

while True:
    user_input = input("\n Enter 'add' 'show' 'edit' 'complete' 'quit': ")
    user_input =   user_input.strip().lower()


    if  user_input.startswith("add"):
        file = open("todos.txt", "r")
        todos = file.readlines()
        file.close()
        todo = user_input[4:]
        todos.append(todo)

        file = open("todos.txt", "w")
        file.writelines(todos)
        file.close()
        print("\n to do added\n")
        
    elif user_input.startswith("show"):
        print("\n This is your to do list \n\n")
        file = open("todos.txt", "r")
        todos = file.readlines()
        file.close()

        new_todos = []

        for i in todos:
            new_item= i.strip("\n")
            new_todos.append(new_item)
        
        #new_todos = [i.strip("\n") for i in todos]:

        for index, item in enumerate(new_todos):

            print(f"{index+1}-{item}")
    
    elif user_input.startswith("edit"):
        try:
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            edit_num = user_input[5:]
            edit_item_num = int(edit_num)-1

            edit_item = input("\n What do you want to edit it to: ") + "\n"
            todos[edit_item_num] = edit_item 

            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()

            print("\n item edited")
        except ValueError:
            print("your command is not valid")
            continue

    elif user_input.startswith("complete"):
        try:
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            complete_num = int(user_input[9:])
            completed_todo = todos[complete_num-1]
            todos.pop(complete_num-1)
            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()
            print(f"you completed to do {complete_num}-{completed_todo}")

        except IndexError:
            print("There is no item with that number")
            continue

    elif user_input.startswith("quit"):
            print("Thank you! see you soon!")
            break
    else:
        print("invalid statement.")



    