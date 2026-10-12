tasks = []

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task to add: ")
        tasks.append(task)
        print(f"Task '{task}' added.")
    elif choice == "2":
        if not tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            print("Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            try:
                task_index = int(input("Enter the number of the task to remove: ")) - 1
                if 0 <= task_index < len(tasks):
                    removed_task = tasks.pop(task_index)
                    print(f"Task '{removed_task}' removed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    elif choice == "4":
        print("Exiting the to-do list application.")
        break
    else:      
        print("Invalid choice. Please enter a number between 1 and 4.") 