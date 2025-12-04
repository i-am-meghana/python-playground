
todo_list = []

def show_todo():
    for item in todo_list:#each item is a dict, so for each item we can access the value of specific key
        print("\nTask:", item["task"], "| Done:", item["done"])

while True:
    print("\n=== MENU ===")
    print("1. Add Task")
    print("2. Mark task as done")
    print("3. Delete item")
    print("4. Exit")
    
    choice = input("\nEnter your choice: ")
    
    if choice == "1":
        users_task = input("\nEnter task: ")
        task_dict = {"task": users_task, "done": False}
        todo_list.append(task_dict)
        show_todo()
        
    elif choice == "2":
        update_status_task = input("\nEnter task you have completed: ")
        for d in todo_list:
            if d["task"] == update_status_task:
                d["done"] = True
        show_todo()
                
    elif choice == "3":
        delete_task = input("\nEnter task to delete: ") 
        todo_list = [d for d in todo_list if d["task"] != delete_task]
        show_todo()
        
    elif choice =="4":
        print("\nlooks like you are done for now!")
        show_todo()
        break
    
    else:
        print("\npls enter a number 1 through 5")