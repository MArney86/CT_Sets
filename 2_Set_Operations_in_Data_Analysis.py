#Task 1:
def print_unique_ids(customer_ids): #function to print the unique ids nicely
    unique_ids = {id for id in customer_ids} #set comprehension to create a set of unique customer ids from the list of customer ids

    print("\n\033[7m Unique Customer IDs:\033[0m") #Header list of unique ids
    for customer_id in sorted(unique_ids): #iterate through the sorted set of unique ids
        print(f" - {customer_id}") #print the customer id in a formatted manner

customer_ids = ["CID001", "CID002", "CID003", "CID002", "CID001", "CID004", "CID005", "CID006", "CID004", "CID007"] #list of customer ids

while True: #loop for program menu
    print('''\nCustomer ID cleanup
1 - Cleanup duplicates
2 - Exit''')
    choice = input("Enter your choice: ") #choice input from user

    if choice == '1': #test if choice is '1'
        print_unique_ids(customer_ids) # run print_unique_ids()
    elif choice == '2': #test if choice is '2'
        break #leave loop and program
    else: #invalid choice
        print("\nInvalid choice: Please try again.") #notify user of invalid choice