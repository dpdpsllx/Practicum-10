def finalprice(price, card, isholiday):
    discount = 0

    if price > 30000:
        discount += 10
    elif price > 20000:
        discount += 7
    elif price > 15000:
        discount += 5
    elif price > 5000:
        discount += 3

    if card:
        discount += 5

    if isholiday:
        discount += 3

    discount = min(discount, 15)

    return round(price * (1 - discount / 100), 2)

'''price = float(input())
card = input() == "True"
isholiday = input() == "True"

print(finalprice(price, card, holiday))'''
