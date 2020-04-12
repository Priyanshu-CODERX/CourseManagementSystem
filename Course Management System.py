import time
def courseList():
    # Creating COURSE LIST
    courses = ["Java For Beginners", "Python For Beginners", "C++ Full Course",
               "Android Development", "IoS Development", "Game Development using Unity"]
    for i in courses:
        # LOOPING THROUGH THE COURSES
        print(i)
        print("\n")
    chooseCourse = input("Select a Course: ")
    for i in range(0, len(courses)):
        if courses[0] == chooseCourse:
            print("Name: Java For Beginners")
            print("Course Level: Beginner")
            print("Course Price: Rs1000")
            print("\n")
            buyCourse = input("Do you want to buy this course(Y/N): ").upper()
            print("\n")
            if buyCourse == "Y":
                print("Payment Methods")
                print("\n")
                pay = ["Debit Card", "PayPal", "Google Pay"]
                for i in pay:
                    print(i)
                paymentMethod = input("Enter Payment Method: ")
                if pay[0] == paymentMethod:
                    dbNum = input("Enter Debit Card Number: ")
                    dbPin = input("Enter Debit Card Pin: ")
                    print("\n")
                    print("Total Amount Paid: Rs 1000")
                    time.sleep(2)
                    print("\n")
                    print("Transaction Successfull")
                elif pay[1] == paymentMethod:
                    ppNum = input("Enter PayPal Number :")
                    ppPin = input("Enter PayPal Pin: ")
                    print("\n")
                    print("Total Amount Paid: Rs 1000")
                    time.sleep(2)
                    print("\n")
                    print("Transaction Successfull")
                elif pay[2] == paymentMethod:
                    gpNum = input("Enter Google Pay Number: ")
                    gpPin = input("Enter Google Pay Pin: ")
                    print("Total Amount Paid: Rs 1000")
                    print("\n")
                    time.sleep(2)
                    print("\n")
                    print("Transaction Successfull")

            elif buyCourse == "N":
                login()
            else:
                print("Wrong Input")
            break
        elif courses[1] == chooseCourse:
            print(2)
            break
        else:
            print("No Such Course Out There")


def login():
    # Login Created
    username = input("USERNAME: ")
    password = input("PASSWORD: ")
    defaultUsernames = ["Priyanshu", "Piyush", "user1", "user2"]
    defaultPasswords = ["1234", "5678", "9101", "3454"]
    usernameLength = len(defaultUsernames)

    for i in range(0, usernameLength):
        if defaultUsernames[i] == username:
            if defaultPasswords[i] == password:
                time.sleep(1.0)
                print("Access Granted")
                print("\n")
                time.sleep(1.0)
                print("Loading....")
                print("\n")
                time.sleep(1.0)
                courseList()
                break
            else:
                time.sleep(1.0)
                print("Access Denied")
                break
        else:
            time.sleep(1.0)
            print("Access Denied")
            break


def signup():
    pass

# Main Execution Point
time.sleep(1.0)
print("\n")
print("***************Welcome To Course Management System***************")
print("\n")
login()
