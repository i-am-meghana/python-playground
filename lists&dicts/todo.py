number_of_tasks = int(input("enter number of tasks"))
task_dict = {"task": None, "done": None}
todo_list = []
for i in range(number_of_tasks): 
    
    users_task = input("enter task")
    task_status = input("done?")
    task_dict["task"] = users_task 
    task_dict["done"] = task_status
    
    todo_list.append(task_dict) #all n indices point to the same object since the same task_dict is getting updated each iteration


print(f"to-do:{todo_list}")

'''
1st iteration for index 0 takes study and nope as values of dict and appends it to the list
to-do:[{'task': 'study', 'done': 'nope'}]
2nd iteration for index 1 takes garden and yep as values and appends it to the list. 
since we modified the SAME dict all the exisiting instances also gets modified with this value as well
todo_list = [task_dict, task_dict]
so now list becomes to-do:[{'task': 'garden', 'done': 'yep'}, {'task': 'garden', 'done': 'yep'}
'''