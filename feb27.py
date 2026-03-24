# # Input details
# salary = float(input("Enter salary: "))
# experience = int(input("Enter years of experience: "))
# rating = float(input("Enter performance rating (1-5): "))
# department = input("Enter department (IT/HR/Sales): ")

# # Decision making
# if experience >= 10 and rating >= 4.5:
#     print("Senior Level - Eligible for Promotion")

# elif experience >= 5 and rating >= 4:
#     print("Mid Level - Salary Bonus Eligible")

# elif experience < 5 and rating >= 3:
#     print("Junior Level - Needs Skill Improvement")

# else:
#     print("Performance Improvement Required")

# # Department-based message
# if department.lower() == "it":
#     print("IT Department - Technical Role")

# elif department.lower() == "hr":
#     print("HR Department - Management Role")

# elif department.lower() == "sales":
#     print("Sales Department - Target Based Role")

# else:
#     print("Unknown Department")
# # Employee Evaluation System

# def calculate_bonus(salary, experience, rating):
#     if experience >= 10 and rating >= 4.5:
#         bonus = salary * 0.20
#         level = "Senior Level - Promotion Eligible"
#     elif experience >= 5 and rating >= 4:
#         bonus = salary * 0.10
#         level = "Mid Level - Bonus Eligible"
#     elif experience < 5 and rating >= 3:
#         bonus = salary * 0.05
#         level = "Junior Level - Small Bonus"
#     else:
#         bonus = 0
#         level = "Performance Improvement Required"
    
#     return bonus, level


# def department_role(department):
#     department = department.lower()
    
#     if department == "it":
#         return "Technical Role - Developer/Engineer"
#     elif department == "hr":
#         return "Management Role - Recruitment/Operations"
#     elif department == "sales":
#         return "Target Based Role - Business Development"
#     elif department == "finance":
#         return "Financial Role - Accounts/Investment"
#     else:
#         return "Unknown Department"


# def main():
#     print("===== Employee Evaluation System =====")
    
#     name = input("Enter employee name: ")
#     salary = float(input("Enter salary: "))
#     experience = int(input("Enter years of experience: "))
#     rating = float(input("Enter performance rating (1-5): "))
#     department = input("Enter department (IT/HR/Sales/Finance): ")
    
#     bonus, level = calculate_bonus(salary, experience, rating)
#     role = department_role(department)
#     final_salary = salary + bonus
    
#     print("\n===== Employee Summary =====")
#     print("Name:", name)
#     print("Department:", department)
#     print("Experience:", experience, "years")
#     print("Performance Rating:", rating)
#     print("Employee Level:", level)
#     print("Department Role:", role)
#     print("Bonus Amount:", bonus)
#     print("Final Salary:", final_salary)


# # Run the program
# if __name__ == "__main__":
#     main()
# a=20
# b=10
# print(a+b, a-b, a*b, a/b)
# print("Hey everyone its me {} and I am interest in {}".format("Shashank karna", "travelling, playing, riding"))
# employees = [
#     ("Bigyan", 26, "IT"),
#     ("Shashank", 25, "Python"),
#     ("Janak", 27, "Docker"),
#     ("Subash", 28, "Frontend")
# ]

# print(f"{'Name':<10} {'Age':<5} {'Department':<10}")
# print ("-" * 27)
# for emp in employees:
#     print(f"{emp[0]:<10} {emp[1]:<5} {emp[2]:<10}")
# age=25
# if age >=25:
#     print("you're an adult")
# elif age >=20:
#     print("You're a junior")
# def add(x, y):
#     return x+y
# def subtract(x, y):
#     return x-y
# def multiply(x, y):
#     return x*y
# def divide(x, y):
#     if y==0:
#         return"Error Divison By Zero."
#     else:
#         return x/y
#     def calculator():
#         print("Welcome to the python calculator!")
#         print("Select operation:")
#         print("1.add")
#         print("1.subtract")
#         print("1.multiply")
#         print("1.divide")
#     choice=input("Enter choice(1/2/3/4):")
    
#     if choice in ('1', '2', '3', '4'):
#         num1=float (input("Enter first number: "))
#         num2=float(inpout("Enter second number: "))\
        
#     if choice == '1':
#         print(f"{num1} + {num2}={add (num1, num2)}")
#     elif choice == '2':
#         print(f"{num1}-{num2}={subtract(num1, num2)}")
#     elif choice =='3':
#         print(f"{num1}*{num2}={multiply(num1, num2)}")
#     elif choice=='4':
#         print(f"{num1}/{num2}={divide(num1, num2)}")
#     else: 
#         print("Invalid Input")

# import random

# def guess_the_number():
#     print("Welcome to 'Guess the Number' Game!")
#     print("Select Difficulty Level")
#     Print("1. Easy (10 attempts)")
#     print("2.Medium (7 attempts)")
#     print("3. Hard (5 attempts)")
    
#     #Choose difficulty
#     choice = input("Enter choice (1/2/3):")
    
#     if choice == "1":
#         attempts_left = 10
#     elif choice == "2":
#         attempts_left = 7
#     elif choice == "3":
#         attempts_left = 5
#     else:
#         print("Invalid choice! Defaulting to Mediun level.")
#         attempts_left = 7
        
#         number_to_guess = random.randint(1, 100)
#         print("\nI'm thinking of a number between 1 and 100.")
        
#         while attempts_left > 0:
#             try:
#                 guess = int(input(f"\nTake a guess({attempts_left} attempts left):"))
                
#                 if guess < number_to_guess:
#                     print("Too low!")
#                 elif guess > number_to_guess:
#                     print("Too high!")
#                 else:
#                     print(f"congratulations! you guessed the number {number_to_guess}!")
#                     return #End game if correct
                
#                 attempts_left -=1
                
#             except ValueError:
#                 print("please enter a valid number.")
                
#                 #If player runs out of attempts

# print(f"\n Game Over! The number was {number_to_guess}.") 
# #Run the game
# guess_the_number              
# word="laptop"
# a=word[2]
# b=word[-1]
# print(a+b)
from turtle import *
bgcolor("black")
pensize(2)
color("green")
left(90)
backward(100)
speed(200)
shape("turtle")

def tree(i):
    if i<10:
        return
    else:
        forward()
        color("orange")
        circle(2)
        color("brown")
        left(30)
        tree(3*i/4)
        right(60)
        tree(3*i/4)
        left(30)
        backward(i)
        
        tree(100)
        done()
import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Roaming Turtle with Boundaries")

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)
t.width(3)

colors = ["red", "blue", "green", "yellow", "purple",
          "orange", "cyan", "white", "pink"]

# Initial direction
direction = 45

while True:
    t.color(random.choice(colors))
    t.forward(20)

    x, y = t.position()

    # Bounce from walls
    if x > 290 or x < -290:
        direction = 180 - direction
        t.setheading(direction)

    if y > 290 or y < -290:
        direction = -direction
        t.setheading(direction)

    t.right(random.randint(0, 30))


