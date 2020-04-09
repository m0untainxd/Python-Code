#Bus Ticket Program
#By Andrew Radcliffe

#This will create a pop-up window called 'main'
#It will be with the dimensions of 200x200
from tkinter import *
main = Tk()
main.geometry("200x200")

#Creates a function
def get_info():

    #Creating the variables needed for this function
    num_people = 0 #local var
    Ages = [] #global var
    age = 0 #local var
    student = False #local var
    Students = [] #global var
    family = False #global var

    #This will prompt the user to input how many tickets are required 
    print("How many people are travelling?")
    num_people = int(input())
    
    #This creates a fixed loop for getting values and appending them to the arrays
    for index in range(num_people):
        #This asks for the age of the person for that index
        print("What is the age of person", index+1, "? ")
        age = input()

        #This is a validation while loop where it blocks the user from carrying on as long as
        #they input something that is not a digit or below 0 or above 100
        while not age.isdigit() or int(age) < 0 or int(age) > 100:
            print("Please enter a valid age")
            age = input()
       #end while

        #This asks the user to input yes or no for if they are a student
        print("Are you a student? (Yes/No)")
        student = input()
        #This takes any value that could be interpreted as true and set the value to a boolean
        if student == "Yes" or student == "yes" or student == "Y" or student == "y":
            student = True
        #This sets everything else to false
        else:
            student = False
        Students.append(student) #Appends the boolean value to an array
        
        Ages.append(int(age)) #Appends the age for this particular loop to the array
    #end for

    #This asks if the passengers are travelling as a family
    print("Are you travelling as a family? (True/False)")
    family = input()
    #Again, this changes the values to boolean
    if family == "Yes" or family == "yes" or family == "Y" or family == "y":
        family = True
    else:
        family = False

    #This returns the variables that need to be passed on to other functions
    #This turns the values into global variables
    return Ages, Students, family 

#Defines a function for calculation
def calc(Ages, Students, family):

    #Creates the variables for required for this function
    total_price = 0 #local var
    ticket = 0 #local var

    #Creates a fixed loop for calculating the price for a ticket and then adding that to the total price
    for index in range(len(Ages)):

        #This makes the program choose between multiple conditions depending on the age of the person
        #The ticket price is free for people between 0 and 5
        if Ages[index] >=0 and Ages[index] <= 5: 
            print("The price for a", Ages[index], "year old is free.")
            
        #The ticket price is £1.35 for people between 6 and 16
        elif Ages[index] > 5 and Ages[index] <= 16:
            print("The price for a", Ages[index], "year old is £1.35.")
            ticket = 1.35 #Assigns a value to the ticket price

        #The ticket price is £2.70 for people between 17 and 65
        elif Ages[index] > 16 and Ages[index] <= 65:
            print("The price for a", Ages[index], "year old is £2.70.")
            ticket = 2.70
            
        #The ticket price is £1.35 for people older than 65
        else:
            print("The price for a", Ages[index], "year old is £1.35.")
            ticket = 1.35
        #end if

        #This applies the student discount if applicable
        if Students[index] == True:
            print("You get a 10% student discount for ticket", index+1)
            ticket = ticket * 0.9 #Takes 10% off the ticket price

        total_price = total_price + ticket #The indvidual ticket is added on to the total price
    #end for

    #This applies the family discount if applicable
    if family == True:
        print()
        print("You get a 10% family discount.")
        total_price = total_price * 0.9 #Takes 10% from the total price
    return total_price #Ends the function and returns the value of the total price

#This displays the total price for the journey
def display(total_price):
    print()
    print("The total price for this journey is £",round(total_price,2))
    return

#-------------------------Interface Section-----------------------#

#This function is called by the tkinter interface to run the program
#This runs each function in order then ends the program
def run_program():
    Ages,Students,family=get_info()
    total_price=calc(Ages,Students,family)
    display(total_price)
    return #Ends the function

#This function is called by the tkinter interface to exit the program
def terminate():
    exit()

#This defines 2 buttons in the interface for running and terminating the program
button1 = Button(main,text="Run Program", command=run_program)
button2 = Button(main,text="Exit Program", command=terminate)

#This places the buttons at specific coordinates
button1.place(x=62.5, y=25)
button2.place(x=62.5, y=150)

#This places the buttons
button1.place()
button2.place()

#This runs the interface to where it is constantly running until it is terminated
mainloop()

    
#-----------------------------------------------------------------#

Ages,Students,family=get_info()
total_price=calc(Ages,Students,family)
display(total_price)
