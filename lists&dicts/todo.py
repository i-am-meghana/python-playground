
number_of_tasks = int(input("Enter number of tasks: "))

todo_list = []
for i in range(number_of_tasks):#we are entering inside each dicts
    task_dict = {}
    users_task = input("enter task")
    task_dict["task"] = users_task
    task_dict["done"] = False
    
    todo_list.append(task_dict)
print(f"to-do:{todo_list}")

delete_task = input("enter task to delete") #we are entering the loop
todo_list = [d for d in todo_list if d["task"] != delete_task] 
print(f"to-do:{todo_list}") 

update_status_task = input("enter task you have completed")
for d in todo_list:
    if d["task"] == update_status_task:
        d["done"] = True
        
print(f"to-do:{todo_list}")
