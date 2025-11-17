def student_discount(price):
    if price > 1000:
        return price * 0.9
    else:
        return price * 0.95

def other_discount(price):
    if price > 2000:
        return price * 0.85
    else:
        return price

def discount(price, category):
    if category == "student":
        return student_discount(price)
    else:
        return other_discount(price)

print(discount(1000, "student"))