print("- - - - Calculate Helper - - - -")

def login():
    corr_user = "napattC"
    corr_pass = "1234"

    input_user = input("Username :")
    input_pass = input("Password :")

    if input_user == corr_user and input_pass == corr_pass:
        print("Log-in succeeded, please select calculation you need :")
        return showMenu()
    else:
        print("Please, try again")
        return login()

def showMenu():
    print("(1) VAT(7%) calculator")
    print("(2) Product price calculator (including VAT)")

    return menuSelect()

def menuSelect():
    user_selected = int(input(">>"))
    if user_selected == 1:
        print(vatCalculate())
        return moreOrNot()
    elif user_selected == 2:
        print(priceCalculate())
        return  moreOrNot()
    else:
        print("Select only (1) or (2)")
        return menuSelect()

def vatCalculate():
    user_input = int(input("Product price :"))
    vat = 7/100
    vat_only = "VAT only :" + str(user_input*vat) + " THB"
    return vat_only

def priceCalculate():
    user_input_price1 = int(input("First product price (THB) : "))
    user_input_price2 = int(input("Second Product price (THB) : "))
    total_price = user_input_price1 + user_input_price2
    vat = 7/100
    price_incld_vat = "Total price (including VAT) :" + str(total_price + (total_price * vat)) + " THB"
    return price_incld_vat

def moreOrNot():
    mOn_input = input("Do you want to calculate more? (y/n) :")
    if mOn_input == "y":
        return showMenu()
    elif mOn_input == "n":
        print("Have a nice day")
        exit()
    else:
        print("Please select only y or n, try again")
        return moreOrNot()

print(login())







