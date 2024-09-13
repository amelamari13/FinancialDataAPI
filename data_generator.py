import random
from datetime import datetime, timedelta


def generate_synthetic_prices():
    actions = ['AAPL', 'GOOGL', 'AMZN']

    start_date = datetime.now()

    prices = []

    for i in range(3):
        current_date = start_date + timedelta(days=i)

        for action in actions:
            price = round(random.uniform(100, 1500), 2)

            prices.append({
                'action': action,
                'date': current_date.strftime('%Y-%m-%d'),
                'price': price
            })

    return prices
