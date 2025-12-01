users_task = input("enter task")
task_status = input("done?")
#want the keys to be fixed
task_dict = {"task": None, "done": None} #had to ask "i want to set the key but value for those 2 keys will be suer inputed" 
task_dict["task"] = users_task
task_dict["done"] = task_status

todo_list = []
todo_list.append(task_dict)
print(f"to-do:{todo_list}")