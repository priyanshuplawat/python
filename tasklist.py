tasks = []

while True:
    print("\n===== To-Do List =====")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter your Choice: ")

    if choice == '1':
        nooftask = (input("How many tasks do you want to add: "))
        for i in range(nooftask):
            task = input("Enter the task: ")
            tasks.append({"task": task, "done": False})
        print("Task added successfully!")

    elif choice == '2':
        if tasks:
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")
        else:
            print("there is no tasks")

    elif choice == '3':
        if tasks:
            task_index = (input("Enter the task number to mark as done: "))
                index = task_index - 1
                if 0 <= index < len(tasks):
                    tasks[index]["done"] = True
                    print("Task marked as done")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No tasks to mark as done.")

    elif choice == '4':
        if tasks:
            try:
                task_index = int(input("Enter the task number to REMOVE: "))
                index = task_index - 1
                if 0 <= index < len(tasks):
                    tasks.pop(index)
                    print("Task removed successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No tasks to remove.")

    elif choice == '5':
        print("Exit To-Do List.")
        break

    else:
        print("Invalid choice..please try again.")
