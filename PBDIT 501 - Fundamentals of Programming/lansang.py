"""
PBDIT 1-2
Group 3
Institutional Repository System
Backend
"""


#1.0 - Import the datetime module

import datetime                                                                         #import the datetime module


#1.1 - Create empty storage for users and publications

users = []                                                                              #empty storage for registered users
publications = []                                                                       #empty storage for publications


#1.2 - Create the sign up function

def sign_up():

        print("========== CREATE ACCOUNT ==========")                                   #display the create account heading

        full_name = input("Enter full name: ")                                          #input for user's full name
        email = input("Enter e-mail: ")                                                 #input for user's e-mail
        username = input("Enter username / ID: ")                                       #input for user's username or ID
        password = input("Enter password: ")                                            #input for user's password
        role = input("Enter role: ").lower()                                            #input for user's role and convert to lowercase

        if      (full_name == "" or
                 email == "" or
                 username == "" or
                 password == "" or
                 role == ""):                                                           #check if any required field is empty

                print("Please complete all fields.")                                    #display incomplete fields message

        elif    (role != "student" and
                 role != "faculty" and
                 role != "librarian"):                                                  #check if the role is invalid

                print("Invalid role.")                                                  #display invalid role message

        else:

                username_exists = False                                                 #set username existence to false

                for user in users:                                                      #check each registered user

                        if user["username"] == username:                                #check if username already exists

                                username_exists = True                                  #set username existence to true

                if      username_exists:                                                #check if username already exists

                        print("Username / ID already exists.")                          #display username exists message

                else:

                        user = {                                                        #create a dictionary for user information
                                "full_name": full_name,                                 #store user's full name
                                "email": email,                                         #store user's e-mail
                                "username": username,                                   #store user's username or ID
                                "password": password,                                   #store user's password
                                "role": role                                            #store user's role
                        }

                        users.append(user)                                              #add the new user to the users list

                        print("Account created successfully.")                          #display successful account creation message


#1.3 - Create the login function

def login():

        print("========== LOGIN ==========")                                            #display the login heading

        username = input("Enter username / ID: ")                                       #input for user's username or ID
        password = input("Enter password: ")                                            #input for user's password

        if      (username == "" or
                 password == ""):                                                       #check if any login field is empty

                print("Please complete all fields.")                                    #display incomplete fields message

                return None                                                             #return no user

        else:

                for user in users:                                                      #check each registered user

                        if      (user["username"] == username and
                                 user["password"] == password):                         #check if username and password match

                                print("Login successful.")                              #display successful login message
                                print("Welcome,", user["full_name"] + "!")              #display user's name
                                print("Role:", user["role"])                            #display user's role

                                return user                                             #return the logged-in user's information

                print("Invalid username or password.")                                  #display login error message

                return None                                                             #return no user


#1.4 - Create the publication submission function

def submit_publication(user):

        print("========== SUBMIT PUBLICATION ==========")                               #display the submission heading

        title = input("Enter publication title: ")                                      #input for publication title
        author = user["full_name"]                                                      #get the full name of the logged-in faculty user
        description = input("Enter publication description: ")                          #input for publication description

        submission_time = datetime.datetime.now()                                       #get the current date and time

        if      (title == "" or
                 description == ""):                                                    #check if required publication fields are empty

                print("Please complete all fields.")                                    #display incomplete fields message

        else:

                publication = {                                                         #create a dictionary for publication information
                        "title": title,                                                 #store publication title
                        "author": author,                                               #store publication author
                        "description": description,                                     #store publication description
                        "status": "Pending",                                            #set the initial publication status to Pending
                        "submission_time": submission_time                              #store the publication submission time
                }

                publications.append(publication)                                        #add the publication to the publications list

                print("Publication submitted successfully.")                            #display successful submission message
                print("Status:", publication["status"])                                 #display the current publication status


#1.5 - Create the function to view all publications

def view_publications():

        print("========== PUBLICATIONS ==========")                                     #display the publications heading

        if      len(publications) == 0:                                                 #check if there are no publications

                print("No publications available.")                                     #display no publications message

        else:

                for publication in publications:                                        #go through each publication

                        print("------------------------------")                         #display a separator
                        print("Title:", publication["title"])                           #display publication title
                        print("Author:", publication["author"])                         #display publication author
                        print("Description:", publication["description"])               #display publication description
                        print("Status:", publication["status"])                         #display publication status
                        print("Submission Time:", publication["submission_time"])       #display publication submission time


#1.6 - Create the function to view approved publications

def view_approved_publications():

        print("========== APPROVED PUBLICATIONS ==========")                            #display the approved publications heading

        approved_found = False                                                          #set approved publication indicator to false

        for publication in publications:                                                #go through each publication

                if      publication["status"] == "Approved":                            #check if publication status is Approved

                        approved_found = True                                           #set approved publication indicator to true

                        print("------------------------------")                         #display a separator
                        print("Title:", publication["title"])                           #display publication title
                        print("Author:", publication["author"])                         #display publication author
                        print("Description:", publication["description"])               #display publication description

        if      approved_found == False:                                                #check if no approved publication was found

                print("No approved publications available.")                            #display no approved publications message


#1.7 - Create the function to view faculty publications

def view_my_publications(user):

        print("========== MY PUBLICATIONS ==========")                                  #display the faculty publications heading

        my_publication_found = False                                                    #set publication indicator to false

        for publication in publications:                                                #go through each publication

                if      publication["author"] == user["full_name"]:                     #check if publication belongs to logged-in faculty

                        my_publication_found = True                                     #set publication indicator to true

                        print("------------------------------")                         #display a separator
                        print("Title:", publication["title"])                           #display publication title
                        print("Description:", publication["description"])               #display publication description
                        print("Status:", publication["status"])                         #display publication status
                        print("Submission Time:", publication["submission_time"])       #display publication submission time

        if      my_publication_found == False:                                          #check if no publication was found

                print("You have no publications.")                                      #display no publications message


#1.8 - Create the librarian review function

def review_publications():

        print("========== REVIEW PUBLICATIONS ==========")                              #display the review publications heading

        pending_found = False                                                           #set pending publication indicator to false

        for publication in publications:                                                #go through publications in submission order

                if      publication["status"] == "Pending":                             #check if publication is still pending

                        pending_found = True                                            #set pending publication indicator to true

                        print("------------------------------")                         #display a separator
                        print("Title:", publication["title"])                           #display publication title
                        print("Author:", publication["author"])                         #display publication author
                        print("Description:", publication["description"])               #display publication description
                        print("Status:", publication["status"])                         #display publication status
                        print("Submission Time:", publication["submission_time"])       #display publication submission time

                        decision = input("Enter decision (approve/reject): ").lower()   #get librarian decision

                        if      decision == "approve":                                  #check if librarian selected approve

                                publication["status"] = "Approved"                      #change status to Approved

                                print("Publication approved.")                          #display approval message

                        elif    decision == "reject":                                   #check if librarian selected reject

                                publication["status"] = "Rejected"                      #change status to Rejected

                                print("Publication rejected.")                          #display rejection message

                        else:

                                print("Invalid decision.")                              #display invalid decision message

                        break                                                           #stop after reviewing the oldest pending publication

        if      pending_found == False:                                                 #check if no pending publication was found

                print("No pending publications available for review.")                  #display no pending publications message


#1.9 - Create the student menu

def student_menu():

        while True:                                                                     #repeat the student menu until logout

                print()
                print("========== STUDENT AREA ==========")                             #display the student area heading
                print("1. View Approved Publications")                                  #display student option 1
                print("2. Logout")                                                      #display student option 2

                choice = input("Enter your choice: ")                                   #get the student's menu choice

                if      choice == "1":                                                  #check if student selected view publications

                        view_approved_publications()                                    #call the approved publications function

                elif    choice == "2":                                                  #check if student selected logout

                        print("Logging out...")                                         #display logout message

                        break                                                           #exit the student menu loop

                else:

                        print("Invalid choice.")                                        #display invalid choice message


#1.10 - Create the faculty menu

def faculty_menu(user):

        while True:                                                                     #repeat the faculty menu until logout

                print()
                print("========== FACULTY AREA ==========")                             #display the faculty area heading
                print("1. Submit Publication")                                          #display faculty option 1
                print("2. View My Publications")                                        #display faculty option 2
                print("3. Logout")                                                      #display faculty option 3

                choice = input("Enter your choice: ")                                   #get the faculty user's menu choice

                if      choice == "1":                                                  #check if faculty selected submit publication

                        submit_publication(user)                                        #call the publication submission function

                elif    choice == "2":                                                  #check if faculty selected view publications

                        view_my_publications(user)                                      #call the faculty publications function

                elif    choice == "3":                                                  #check if faculty selected logout

                        print("Logging out...")                                         #display logout message

                        break                                                           #exit the faculty menu loop

                else:

                        print("Invalid choice.")                                        #display invalid choice message


#1.11 - Create the librarian menu

def librarian_menu():

        while True:                                                                     #repeat the librarian menu until logout

                print()
                print("========== LIBRARIAN AREA ==========")                           #display the librarian area heading
                print("1. View All Publications")                                       #display librarian option 1
                print("2. Review Publications")                                         #display librarian option 2
                print("3. Logout")                                                      #display librarian option 3

                choice = input("Enter your choice: ")                                   #get the librarian's menu choice

                if      choice == "1":                                                  #check if librarian selected view publications

                        view_publications()                                             #call the view publications function

                elif    choice == "2":                                                  #check if librarian selected review publications

                        review_publications()                                           #call the review publications function

                elif    choice == "3":                                                  #check if librarian selected logout

                        print("Logging out...")                                         #display logout message

                        break                                                           #exit the librarian menu loop

                else:

                        print("Invalid choice.")                                        #display invalid choice message


#1.12 - Create the main menu

def main_menu():

        while True:                                                                     #repeat the main menu until the user exits

                print()
                print("========== INSTITUTIONAL REPOSITORY ==========")                 #display the main system heading
                print("1. Sign Up")                                                     #display sign up option
                print("2. Login")                                                       #display login option
                print("3. Exit")                                                        #display exit option

                choice = input("Enter your choice: ")                                   #get the user's menu choice

                if      choice == "1":                                                  #check if user selected sign up

                        sign_up()                                                       #call the sign up function

                elif    choice == "2":                                                  #check if user selected login

                        logged_in_user = login()                                        #call login and store returned user information

                        if      (logged_in_user != None and
                                 logged_in_user["role"] == "student"):                  #check if logged-in user is a student

                                student_menu()                                          #open the student menu

                        elif    (logged_in_user != None and
                                 logged_in_user["role"] == "faculty"):                  #check if logged-in user is faculty

                                faculty_menu(logged_in_user)                            #open the faculty menu

                        elif    (logged_in_user != None and
                                 logged_in_user["role"] == "librarian"):                #check if logged-in user is librarian

                                librarian_menu()                                        #open the librarian menu

                elif    choice == "3":                                                  #check if user selected exit

                        print("Thank you for using the Institutional Repository.")      #display exit message

                        break                                                           #end the main menu loop

                else:

                        print("Invalid choice.")                                        #display invalid choice message


#1.13 - Start the system

main_menu()                                                                             #call the main menu function


#END OF SAMPLE