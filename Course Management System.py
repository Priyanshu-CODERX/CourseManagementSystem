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
            print("Name: Python For Beginners")
            print("Course Level: Beginner")
            print("Course Price: Rs1500")
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
                    print("Total Amount Paid: Rs 1500")
                    time.sleep(2)
                    print("\n")
                    print("Transaction Successfull")
                elif pay[1] == paymentMethod:
                    ppNum = input("Enter PayPal Number :")
                    ppPin = input("Enter PayPal Pin: ")
                    print("\n")
                    print("Total Amount Paid: Rs 1500")
                    time.sleep(2)
                    print("\n")
                    print("Transaction Successfull")
                elif pay[2] == paymentMethod:
                    gpNum = input("Enter Google Pay Number: ")
                    gpPin = input("Enter Google Pay Pin: ")
                    print("Total Amount Paid: Rs 1500")
                    print("\n")
                    time.sleep(2)
                    print("\n")
                    print("Transaction Successfull")

            elif buyCourse == "N":
                login()
            else:
                print("Wrong Input")
            break

        elif courses[2] == chooseCourse:
            print("Name: C++ For Beginners")
            print("Course Level: Beginner")
            print("Course Price: Rs3000")
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
                    print("Total Amount Paid: Rs 3000")
                    time.sleep(2)
                    print("\n")
                    print("Transaction Successfull")
                elif pay[1] == paymentMethod:
                    ppNum = input("Enter PayPal Number :")
                    ppPin = input("Enter PayPal Pin: ")
                    print("\n")
                    print("Total Amount Paid: Rs 3000")
                    time.sleep(2)
                    print("\n")
                    print("Transaction Successfull")
                elif pay[2] == paymentMethod:
                    gpNum = input("Enter Google Pay Number: ")
                    gpPin = input("Enter Google Pay Pin: ")
                    print("Total Amount Paid: Rs 3000")
                    print("\n")
                    time.sleep(2)
                    print("\n")
                    print("Transaction Successfull")

            elif buyCourse == "N":
                login()
            else:
                print("Wrong Input")
            break

        elif courses[3] == chooseCourse:
            print("Name: IoS Development")
            print("Course Level: Advance")
            print("Course Price: Rs4500")
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
                    print("Total Amount Paid: Rs 4500")
                    time.sleep(2)
                    print("\n")
                    print("Transaction Successfull")
                elif pay[1] == paymentMethod:
                    ppNum = input("Enter PayPal Number :")
                    ppPin = input("Enter PayPal Pin: ")
                    print("\n")
                    print("Total Amount Paid: Rs 4500")
                    time.sleep(2)
                    print("\n")
                    print("Transaction Successfull")
                elif pay[2] == paymentMethod:
                    gpNum = input("Enter Google Pay Number: ")
                    gpPin = input("Enter Google Pay Pin: ")
                    print("Total Amount Paid: Rs 4500")
                    print("\n")
                    time.sleep(2)
                    print("\n")
                    print("Transaction Successfull")

            elif buyCourse == "N":
                login()
            else:
                print("Wrong Input")
            break

        elif courses[4] == chooseCourse:
            print("Name: IoS Development")
            print("Course Level: Advance")
            print("Course Price: Rs6000")
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
                    print("Total Amount Paid: Rs 6000")
                    time.sleep(2)
                    print("\n")
                    print("Transaction Successfull")
                elif pay[1] == paymentMethod:
                    ppNum = input("Enter PayPal Number :")
                    ppPin = input("Enter PayPal Pin: ")
                    print("\n")
                    print("Total Amount Paid: Rs 6000")
                    time.sleep(2)
                    print("\n")
                    print("Transaction Successfull")
                elif pay[2] == paymentMethod:
                    gpNum = input("Enter Google Pay Number: ")
                    gpPin = input("Enter Google Pay Pin: ")
                    print("Total Amount Paid: Rs 6000")
                    print("\n")
                    time.sleep(2)
                    print("\n")
                    print("Transaction Successfull")

            elif buyCourse == "N":
                login()
            else:
                print("Wrong Input")
            break

        elif courses[5] == chooseCourse:
            print("Name: Game Development using Unity")
            print("Course Level: Advance")
            print("Course Price: Rs7000")
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
                    print("Total Amount Paid: Rs 7000")
                    time.sleep(2)
                    print("\n")
                    print("Transaction Successfull")
                elif pay[1] == paymentMethod:
                    ppNum = input("Enter PayPal Number :")
                    ppPin = input("Enter PayPal Pin: ")
                    print("\n")
                    print("Total Amount Paid: Rs 7000")
                    time.sleep(2)
                    print("\n")
                    print("Transaction Successfull")
                elif pay[2] == paymentMethod:
                    gpNum = input("Enter Google Pay Number: ")
                    gpPin = input("Enter Google Pay Pin: ")
                    print("Total Amount Paid: Rs 7000")
                    print("\n")
                    time.sleep(2)
                    print("\n")
                    print("Transaction Successfull")

            elif buyCourse == "N":
                login()
            else:
                print("Wrong Input")
            break

        else:
            print("No Such Course Out There")


def login():
    # Login Created
    dUsername = "Priyanshu"
    dPassword = "1234"
    user = input("USERNAME: ")
    passw = input("PASSWORD: ")
    if dUsername == user:
        if dPassword == passw:
            courseList()
        else:
            print("Invalid Login Credentials")
    else:
        print("Invalid Login Credentials")

# Main Execution Point
time.sleep(1.0)
print("\n")
print("***************Welcome To Course Management System***************")
print("\n")
login()
