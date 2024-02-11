import yfinance as yf

def calculate_stock_score(pe_ratio, roe, dividend_yield, beta, moving_average_trend, volatility):
    # Coefficients for the formula
    pe_weight = 0.2
    roe_weight = 0.15
    dividend_yield_weight = 0.1
    beta_weight = 0.2
    moving_average_trend_weight = 0.15
    volatility_weight = 0.2

    # Calculate Stock Score
    stock_score = (
        pe_weight * pe_ratio +
        roe_weight * roe +
        dividend_yield_weight * dividend_yield +
        beta_weight * beta +
        moving_average_trend_weight * moving_average_trend +
        volatility_weight * volatility
    )

    return stock_score

def interpret_stock_score(stock_score):
    # Define scoring ranges
    if stock_score > 80:
        return "Strong buy"
    elif 60 <= stock_score <= 80:
        return "Buy with caution"
    elif 40 <= stock_score < 60:
        return "Hold or analyze further"
    else:
        return "Consider selling"

def main():
    # Read stock symbols from the file
    with open('sp500_symbols.txt', 'r') as file:
        stock_symbols = [line.strip() for line in file]

    for stock_symbol in stock_symbols:
        # Fetch historical stock data from Yahoo Finance
        stock_data = yf.download(stock_symbol, start='2022-01-01', end='2023-01-01')

        # Example: Extract relevant financial metrics (replace with actual data extraction)
        pe_ratio = 15
        roe = 0.12
        dividend_yield = 0.03
        beta = 1.5
        moving_average_trend = 0.1
        volatility = 0.18

        # Calculate Stock Score
        stock_score = calculate_stock_score(pe_ratio, roe, dividend_yield, beta, moving_average_trend, volatility)

        # Interpret the Stock Score
        interpretation = interpret_stock_score(stock_score)

        # Print the stock symbol and recommendation for scores > 60
        if stock_score > 60:
            print(f"The Stock Score for {stock_symbol} is: {stock_score:.2f}")
            print(f"Recommendation: {interpretation}")
            print()

if __name__ == "__main__":
    main()
