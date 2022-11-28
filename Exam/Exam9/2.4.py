# 2.4  Calculate Amount Paid in Taxes
# You are given a 0-indexed 2D integer array brackets where brackets[i] = [upper(i), percent(i)]
# means that the i(th) tax bracket has an upper bound of upper(i) and is taxed at a rate of percent(i).
# The brackets are sorted by upper bound (i.e. upper(i-1) < upper(i) for 0 < i < brackets.length).
# Tax is calculated as follows:
# - The first upper(0) dollars earned are taxed at a rate of percent(0).
# - The next upper(1) - upper(0) dollars earned are taxed at a rate of percent(1).
# - The next upper(2) - upper(1) dollars earned are taxed at a rate of percent(2).
# - And so on.
# You are given an integer income representing the amount of money you earned.
# Return the amount of money that you have to pay in taxes.
def calculate_tax(brackets: list[list[int]], income: int) -> float:
    num = 0
    pay = 0
    while brackets[num][0] <= income:
        num += 1
    for i in range(0, num):
        if i == 0:
            pay += brackets[i][0] * brackets[i][1] / 100
        else:
             pay += (brackets[i+1][0] - brackets[i][0]) * brackets[i][1] / 100
    return pay


brackets = [[3,50],[7,10],[12,25]]
income = 10
print(calculate_tax(brackets, income))



