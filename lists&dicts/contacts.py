n = int(input("how many contacts are you looking to add this time?"))
contact_book = []
for i in range(n):
    contact_name = input("enter contact name")
    contact_number = input("enter number")
    
    contact_details = {contact_name : contact_number}
    
    contact_tag = input("enter tag")
    contact_details["tag"] = contact_tag
    
    contact_book.append(contact_details)
    
    print(contact_book)