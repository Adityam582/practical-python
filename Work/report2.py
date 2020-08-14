# report.py
#
# Exercise 2.4
import csv
def read_prices(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    total_cost = 0.0
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:

                prices[row[0]]=row[1]
            except:
                pass
    return prices

prices = read_prices('Data/prices.csv')
