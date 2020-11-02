
def compound_interest(prnpl, rt, yr):
    """Calculate interest given principal, rate and year"""
    return prnpl * (1 + rt) ** yr


def compound_interest_recursive(principal, rate, year):
    """Calculate interest given principal, rate and year using recursion"""
    if year <=0:
        return principal
    else:
        return compound_interest_recursive(principal+principal*rate, rate, year-1)


if __name__ == "__main__":

    while True:
        principal_input = input("Enter Principal: ")
        rate_input = input("Enter Interest Rate (as percent): ")
        year_input = input("Enter # of years: ")

        try:
            principal = float(principal_input)
            rate = float(rate_input)
            year = float(year_input)
        except Exception as e:
            print("Must enter real numbers")
        else:
            break
    
    interest = compound_interest(principal, rate/100, year)
    interest_rec = compound_interest_recursive(principal, rate/100, year)
    print("Interest calculated using non-recursive way: {:,.2f} and recursive way: {:,.2f) is matching".format(interest, interest_rec))