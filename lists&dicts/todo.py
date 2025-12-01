number_of_tasks = int(input("enter number of tasks"))

todo_list = []
for i in range(number_of_tasks):
    task_dict = {} #keep creating new dict for each iteration 
    users_task = input("enter task")
    task_status = input("done?")
    task_dict["task"] = users_task
    task_dict["done"] = task_status
    
    todo_list.append(task_dict)
    
print(f"to-do:{todo_list}")

