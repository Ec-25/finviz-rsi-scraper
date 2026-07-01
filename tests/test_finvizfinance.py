from finvizfinance.quote import finvizfinance

stock = finvizfinance("tsla")

fundament = stock.ticker_fundament()

print(fundament)
