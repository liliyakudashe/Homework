import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    average_price = data['Close'].mean()
    print(f'Average closing price: {average_price:.2f}')


def notify_if_strong_fluctuations(data, threshold):
    min_price = data['Close'].min()
    max_price = data['Close'].max()
    price_difference = max_price - min_price
    percentage_change = (price_difference / min_price) * 100

    if percentage_change > threshold:
        print(f"Внимание: цена акций колебалась более чем на {threshold}% за данный период.")
    else:
        print("Цена акций не колебалась на заданный порог.")
