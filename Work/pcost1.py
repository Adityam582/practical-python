# pcost.py
#
# Exercise 1.27
import csv
def portfolio_cost(filename):

    with open("C:\\Users\\Aditya\\Documents\\GitVCS\\practical-python\\Work\\Data\\portfolioTest.csv") as f:
        rows = csv.reader(f)
        header = next(rows)
        total = 0
        try:
            for i in rows:
                total +=  float(i[1])*float(i[2])
        except ValueError:
            print("bad digits")
        print("Total", total)
        f.close()
    return total
cost = portfolio_cost(filename)
