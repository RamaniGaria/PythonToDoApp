tasks = []

while True:
    print("\nAvailable actions: 1 = Add, 2 = Delete, 3 = Show, 4 = Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        task = input("Enter a task to add: ")
        tasks.append(task)
        print("Added task:", task)

    elif choice == '2':
        task = input("Enter a task to delete: ")
        if task in tasks:
            tasks.remove(task)
            print("Deleted task:", task)
        else:
            print("Task not found.")

    elif choice == '3':
        if tasks:
            print("Tasks list:")
            for task in tasks:
                print("-", task)
        else:
            print("No tasks to show.")

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid choice, please choose again.")