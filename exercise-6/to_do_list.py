todo_list = []

while True:
    print("\nMenu: add | view | remove | done | quit")
    user_input = input("> ").strip()
    
    if not user_input:
        continue
        
    input_parts = user_input.split(" ", 1)
    command = input_parts[0].lower()
    
    if len(input_parts) > 1:
        argument = input_parts[1].strip()
    else:
        argument = ""

    if command == "add":
        if argument == "":
            print("Error: Please provide a task description.")
        else:
            new_task = {"task_text": argument, "is_done": False}
            todo_list.append(new_task)
            print("Task added.")

    elif command == "view":
        if len(todo_list) == 0:
            print("Your to-do list is empty.")
        else:
            for i in range(len(todo_list)):
                current_item = todo_list[i]
                
                text_content = current_item["task_text"]
                status_check = current_item["is_done"]
                
                if status_check:
                    marker = "[x]"
                else:
                    marker = "[ ]"
                    
                print(f"{i + 1}. {marker} {text_content}")

    elif command == "done":
        if len(todo_list) == 0:
            print("Error: Your to-do list is empty.")
        elif argument == "":
            print("Error: Please specify a task number.")
        elif not argument.isdigit():
            print("Error: Task number must be numeric.")
        else:
            task_num = int(argument)
            if task_num < 1 or task_num > len(todo_list):
                print("Error: Task number out of range.")
            else:
                target_task = todo_list[task_num - 1]
                target_task["is_done"] = True
                print(f"Task {task_num} marked as done.")

    elif command == "remove":
        if len(todo_list) == 0:
            print("Error: Your to-do list is empty.")
        elif argument == "":
            print("Error: Please specify a task number to remove.")
        elif not argument.isdigit():
            print("Error: Task number must be numeric.")
        else:
            task_num = int(argument)
            if task_num < 1 or task_num > len(todo_list):
                print("Error: Task number out of range.")
            else:
                todo_list.pop(task_num - 1)
                print("Task removed.")

    elif command == "quit":
        print("Goodbye!")
        break

    else:
        print("Invalid command. Choose from add, view, remove, done, or quit.")
