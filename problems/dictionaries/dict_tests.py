(DATE, TICKER, OPEN, CLOSE) = (0, 1, 2, 3)

stocks = [['Date', 'Ticker Symbol', 'Open', 'Close'],
          ['2010-11-09', 'AMD', '8.22', '7.91'],
          ['2010-11-09', 'GOOG', '630.00', '624.82'],
          ['2010-11-09', 'QQQ', '53.95', '54.26'],
          ['2010-11-10', 'AMD', '8.22', '8.72'],
          ['2010-11-10', 'BSB', '620.00', '630.40'],
          ['2010-11-10', 'GOOG', '630.00', '630.40'],
          ['2010-11-10', 'QQQ', '53.95', '53.45'],
          ['2010-11-11', 'AMD', '8.22', '8.40'],
          ['2010-11-11', 'GOOG', '630.00', '634.82'],
          ['2010-11-11', 'QQQ', '53.95', '53.45']]

def f1(data):
    d = {}
    for row in data[1:]:
        ticker = row[TICKER]
        if (float(row[CLOSE]) - float(row[OPEN])) < 0:
            d[ticker] = d.get(ticker, 0) + 1
    return d

print("Result:")
print(f1(stocks))
# Result: {'AMD': 1, 'GOOG': 1, 'QQQ': 2}

def f2(data, threshold):
    d = {}
    for row in data[1:]:
        date = row[DATE]
        ticker = row[TICKER]
        spread = float(row[CLOSE]) - float(row[OPEN])
        if threshold <= spread:
            if date not in d:
                d[date] = []
            d[date].append(ticker)
    return d

print("Result:")
print(f2(stocks, 0))

def f3(data):
    d = {}
    for row in data[1:]:
        date = row[DATE]
        ticker = row[TICKER]
        close = float(row[CLOSE])
        if date not in d:
            d[date] = [close, [ticker]]
        elif d[date][0] < close:
            d[date] = [close, [ticker]]
        elif d[date][0] == close:
            d[date][1].append(ticker)
    return d

print("Result:")
print(f3(stocks))
# {'date: []}