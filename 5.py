def cardvalue(price):
    if price == 5 or price == 10:
        return price
    elif price == 25:
        return price + 3
    elif price == 50:
        return price + 8
    elif price == 100:
        return price + 20
    else:
        return "Ошибка"

'''price = int(input())
print(cardvalue(price))'''
