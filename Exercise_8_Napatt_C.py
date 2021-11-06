print("Welcome to P's Shop")


# Username and password
true_user = "napattC"
true_pass = "1234"

user_box = input("Username :")
pass_box = input("Password :")

# log-in condition
if user_box == true_user and pass_box == true_pass :
    print("Log-in Succeeded ! Select a fruit which you want here")

    # product select
    print("(1) Banana   :    7 THB/EA")
    print("(2) Apple    :    15 THB/EA")
    print("(3) Orange   :    8 THB/EA")
    print("(4) Durian   :    250 THB/EA")
    print("(5) Mango    :    18 THB/EA")

    fruit_selected = int(input("Number of fruit (1,2,3,4,5) :"))
    fruit_quan = int(input("Quantity (EA) :"))

    if fruit_selected == 1:
        print("You selected Banana (7 THB/EA) x", fruit_quan, "EA =", 7*fruit_quan, "THB")
    elif fruit_selected == 2:
        print("You selected Apple (15 THB/EA) ", fruit_quan, "EA =", 15*fruit_quan, "THB")
    elif fruit_selected == 3:
        print("You selected Orange (8 THB/EA) ", fruit_quan, "EA =", 8 * fruit_quan, "THB")
    elif fruit_selected == 4:
        print("You selected Durain (250 THB/EA) ", fruit_quan, "EA =", 250 * fruit_quan, "THB")
    elif fruit_selected == 5:
        print("You selected Apple (18 THB/EA) ", fruit_quan, "EA =", 18 * fruit_quan, "THB")


else:
    print("Username or password was wrong. Please try again")


