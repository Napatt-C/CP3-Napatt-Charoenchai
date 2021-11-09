total_price = int(input("TOTAL PRICE :"))

def vatCalculator(total_price):
    result = "Price icluding VAT : " + str(total_price + (total_price * 7/100)) + " THB"
    return result

print(vatCalculator(total_price))




