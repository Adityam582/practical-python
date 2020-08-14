import csv
import sys
def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    total_cost = 0.0
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for rowno, row in enumerate(rows, start=1):
#             record = dict(zip(header, row))
#             print(record)
#             print()
             try:
                record = dict(zip(header, row))
                name = record['name']
                shares = int(record['shares'])
                price = float(record['price'])
             #holding = (row[0], int(row[1]), float(row[2]))
             #holding = {header[0]:row[0], header[1]:float(row[1]), header[2]:float(row[2])}
#                 portfolio.append(holding)
#                print(record)
#                print(portfolio)
                portfolio.append(record)
#                print(portfolio)
             except ValueError:
                print("Bad row number", rowno, "with content", row)
        f.close()
    return portfolio
#portfolio = read_portfolio('Data/portfolio.csv')

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
         f.close()
    return prices

#prices = read_prices('Data/prices.csv')

#initial_price = 0
#current_price = 0
#for i in portfolio:
#    initial_price += float(i['shares'])*float(i['price'])
#    current_price += float(i['shares'])*float(prices[i['name']])
#diff = current_price - initial_price
#print("Total Cost", initial_price)
#print("Current Value", current_price)
#if diff >0:
#    print("Gain: ", diff)
#else:
#    print("Loss: ", diff)

def make_report(portfolio=[], prices={}):
   portfolio = read_portfolio('Data/portfolio.csv')
   prices = read_prices('Data/prices.csv')
   reports = []
   for i in portfolio:
       #t = (i['name'], '\t', i['shares'], '\t', i['price'], '\t', prices[i['name']], '\t', float(i['price'])-float(prices[i['name']]))
       t = (i['name'], int(i['shares']), float(prices[i['name']]), float(i['price'])-float(prices[i['name']]))
       reports.append(t)
   return reports
#portfolio = read_portfolio('Data/portfolio.csv')
#prices = read_prices('Data/prices.csv')
#report = make_report(portfolio, prices)
#for r in report:
#     print('%10s %10d %10.2f %10.2f' % r)
#    print('%10s %10d %10.2f %10.2f' % r)
def print_report(report):

    header = ('Name', 'Shares', 'Price', 'Change')
#print(header)
    print('%10s %10s %10s %10s' % header)
    print('-------- ----------- ------------ ------------')
    for r in report:
      print('%10s %10.2f %10.2f %10.2f' % r)
#for name, shares, price, change in report:
#    print(f'{name:>10s} {shares:>10.2f} ${price:>10.2f} {change:>10.2f}')

def portfolio_report(portfolio_filename, prices_filename):
#    portfolio = read_portfolio('Data/portfolio.csv')
#    prices = read_prices('Data/prices.csv')
    portfolio_filename = 'Data/portfolio.csv'
    prices_filename = 'Data/prices.csv'
    portfolio = read_portfolio(portfolio_filename)

    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

portfolio_report('Data/portfolio.csv','Data/prices.csv')
