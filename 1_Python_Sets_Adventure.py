#1. Python Sets Adventure
#Objective: The aim of this assignment is to deepen your understanding and application of Python sets.

#Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:

#1. Destinations that both airlines fly to.

#2. Destinations unique to your airline.

#3. Whether there are any destinations that neither airline shares.

#Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB", "IAH", "SAN", "SDP", "SBA", "SAF", "MDW", "SLC", "SLW", "CUN"}
competitor_routes = {"JFK", "CDG", "IAH", "LHR", "BKK", "HOU", "SAT", "SAF", "ORD", "MDW", "LGA", "SLW"}

def common_destinations(set_1, set_2):
    new_set = set_1.intersection(set_2)
    print("\033[7mCommon Destinations:\033[0m")
    print_destinations(new_set)

def our_unique_destinations(set_1, set_2):
    new_set = set_1.difference(set_2)
    print("\033[7mOur Unique Destinations:\033[0m")
    print_destinations(new_set)

def unshared_destinations(set_1, set_2):
    new_set = set_1.symmetric_difference(set_2)
    print("\033[7mDestinations Not Shared By Us Or Competitor:\033[0m")
    print_destinations(new_set)

def print_destinations(output_set):
    for destination in output_set:
        print(f"- {destination}")


while True:
    print("\033[1m\nMenu:")
    print("1: Common Destinations between us and competitor")
    print("2: Destinations unique to us only")
    print("3: Destinations not shared between us and competitor")
    print("4: Exit")
    choice = input("Enter your choice: \033[0m")
    if choice == '1':
        common_destinations(our_routes, competitor_routes)
    elif choice == '2':
        our_unique_destinations(our_routes, competitor_routes)
    elif choice == '3':
        unshared_destinations(our_routes, competitor_routes)
    elif choice == '4':
        break
    else:
        print("\033[7mInvalid choice. Please try again.\033[0m")