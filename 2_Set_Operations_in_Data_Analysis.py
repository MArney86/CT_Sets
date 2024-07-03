#2. Set Operations in Data Analysis
#Objective: The aim of this assignment is to enhance your skills in using Python sets for data analysis tasks. You will apply various set operations to handle real-world data scenarios, focusing on their practical application and efficiency.

#Task 1: Duplicate Entries Cleanup You are given a list of customer IDs, some of which are duplicated. Write a Python script to remove duplicates and display the unique customer IDs.

#Example Code:
def print_unique_ids(customer_ids):
    unique_ids = {id for id in customer_ids}

    print("\n\033[7m Unique Customer IDs:\033[0m")
    for customer_id in sorted(unique_ids):
        print(f" - {customer_id}")

customer_ids = ["CID001", "CID002", "CID003", "CID002", "CID001", "CID004", "CID005", "CID006", "CID004", "CID007"]

while True:
    print("\nCustomer ID cleanup")
    print("1 - Cleanup duplicates")
    print("2 - Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        print_unique_ids(customer_ids)
    elif choice == '2':
        break
    else:
        print("\nInvalid choice: Please try again.")