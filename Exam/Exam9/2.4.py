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
    brackets = [[0]] + brackets
    res = 0
    for i in range(len(brackets)):
        if income <= brackets[i][0]:
            for j in range(i, 0, -1):
                res += (income - brackets[j - 1][0]) * brackets[j][1] / 100
                income = brackets[j - 1][0]
            return res
print(calculate_tax(brackets, income))



