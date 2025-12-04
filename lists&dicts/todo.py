
todo_list = []

def show_todo():
    for item in todo_list:#each item is a dict, so for each item we can access the value of specific key
        print("\nTask:", item["task"], "| Done:", item["done"])

while True:
    print("=== MENU ===")
    print("1. Add Task")
    print("2. Mark task as done")
    print("3. Delete item")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        users_task = input("Enter task: ")
        task_dict = {"task": users_task, "done": False}
        todo_list.append(task_dict)
        show_todo()
        
    elif choice == "2":
        update_status_task = input("Enter task you have completed: ")
        found = False
        for d in todo_list:
            if d["task"] == update_status_task:
                d["done"] = True
                found = True 
                break
        if not found:
            print("task does not exist")
        show_todo()
                
    elif choice == "3":
        delete_task = input("Enter task to delete: ")
        updated_todo_list = []
        found = False
        for item in todo_list:
            if item["task"] != delete_task:
                updated_todo_list.append(item)
            else:
                found = True
        todo_list[:] = updated_todo_list
        if not found:
            print("invalid task")
        
        show_todo()
        
    elif choice =="4":
        print("looks like you are done for now!")
        show_todo()
        break