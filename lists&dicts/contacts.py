n = int(input("how many contacts are you looking to add this time?"))
contact_book = []
for i in range(n):
    contact_name = input("enter contact name")
    contact_number = input("enter number")
    contact_tag = input("enter tag")
    
    contact = {"name" : contact_name,
               "number" : contact_number,
               "tag" : contact_tag}
    
    contact_book.append(contact)
    
    
    print(contact_book)

flag = False 
delete_contact = input("enter contact name")
for i, d in enumerate(contact_book):
    if d["name"] == delete_contact:
        flag = True
        index = i
        break
else:
    print("contact name not found. please enter valid contact")

if flag == True:
    contact_book.pop(index)

print(contact_book)
        

#before, we gave if and else inside for loop. when given inside for loop will check both if and else for each value in the list 
