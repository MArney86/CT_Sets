def common_destinations(set_1, set_2): #function to find destinations common between us and competitor
    new_set = set_1.intersection(set_2) #intersection to find common destinations
    print("\n\033[7mCommon Destinations:\033[0m") #Heading for list of destinations
    print_destinations(new_set) #print the destinations from intersection nicely

def our_unique_destinations(set_1, set_2): #function to find destinations unique to our airline
    new_set = set_1.difference(set_2) #difference to find the destinations unique to our airline
    print("\n\033[7mOur Unique Destinations:\033[0m") #Heading for list of destinations
    print_destinations(new_set) #print the destinations from difference nicely

def unshared_destinations(set_1, set_2): #function to find destinations that neither we nor the competition share
    new_set = set_1.symmetric_difference(set_2) #symmetric difference to find destinations not shared
    print("\n\033[7mDestinations Not Shared By Us Or Competitor:\033[0m") #Heading for list of destinations
    print_destinations(new_set) #print the destinations from symmetric difference nicely

def print_destinations(output_set): #function to nicely print the destination sets from our functions
    for destination in output_set: #iterate through the set
        print(f"- {destination}") #print the destination in a formatted way

our_routes = {"LAX", "JFK", "CDG", "DXB", "IAH", "SAN", "SDP", "SBA", "SAF", "MDW", "SLC", "SLW", "CUN"} #set of our destinations
competitor_routes = {"JFK", "CDG", "IAH", "LHR", "BKK", "HOU", "SAT", "SAF", "ORD", "MDW", "LGA", "SLW"} #set of competitor's destinations

while True: #loop for program menu
    print("\033[1m\nMenu:") #heading
    print("1: Common Destinations between us and competitor") #first choice
    print("2: Destinations unique to us only") #second choice
    print("3: Destinations not shared between us and competitor") #third choice
    print("4: Exit") #exit
    choice = input("Enter your choice: \033[0m") #choice input from user
    if choice == '1': #test if choice is '1'
        common_destinations(our_routes, competitor_routes) #call common_destinations()
    elif choice == '2': #test if choice is '2'
        our_unique_destinations(our_routes, competitor_routes) #call unique_destinations()
    elif choice == '3': #test if choice is '3'
        unshared_destinations(our_routes, competitor_routes) #call unshared_destinations()
    elif choice == '4': #test if choice is '4'
        break #exit loop and program
    else: #invalid choice
        print("\nInvalid choice. Please try again.") #notify user of invalid choice