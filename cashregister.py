item1 = float(input("Enter price of the first item: "))
item2 = float(input("Enter price of the second item: "))


hasClubCard = str(input("Does customer have a club card? (Y/N): "))
tax = float(input("Enter tax rate, e.g. 5.5 for 5.5% tax: "))

if (hasClubCard.capitalize() == 'Y'):
    isMember = True
else:
    isMember = False

basePrice = item1 + item2
txt = "base price ={sum: 2.2f}"
print(txt.format(sum=basePrice))


def calcBasePriceAfterPromo(price1, price2):
    if (price1 > price2):
        item2AtReducedPrice = price2 - price2 / 100 * 50
        basePriceAfterPromo = item2AtReducedPrice + price1
        return basePriceAfterPromo
    elif (price1 < price2):
        item1AtReducedPrice = price1 - price1 / 100 * 50
        basePriceAfterPromo = item1AtReducedPrice + price2
        return basePriceAfterPromo
    else:
        item1AtReducedPrice = price1 - price1 / 100 * 50
        basePriceAfterPromo = item1AtReducedPrice + price2
        return basePriceAfterPromo


if (isMember):
    basePriceAfterPromo = calcBasePriceAfterPromo(item1, item2)
    clubMemberReduction = basePriceAfterPromo / 100 * 10
    basePriceWithMemberReduction = basePriceAfterPromo - clubMemberReduction
    txt = "price after discounts = {sum:2.2f}"
    print(txt.format(sum=basePriceWithMemberReduction))
    taxAmount = basePriceWithMemberReduction / 100 * tax
    total = basePriceWithMemberReduction + taxAmount
    totalTxt = "total price = {sum:2.2f}"
    print(totalTxt.format(sum=total))
else:
    basePriceAfterPromo = calcBasePriceAfterPromo(item1, item2)
    txt = "price after discounts = {sum:2.2f}"
    print(txt.format(sum=basePriceAfterPromo))
    taxAmount = basePriceAfterPromo / 100 * tax
    total = basePriceAfterPromo + taxAmount
    totalTxt = "total price = {sum:2.2f}"
    print(totalTxt.format(sum=total))
