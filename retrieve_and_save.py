import requests

API_URL = 'http://127.0.0.1:5000/prices'


def retrieve_and_save():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()

        stock_data = response.json()

        print('Data successfully retrieved!')
        print(stock_data)

        with open('data.txt', 'w') as file:
            for entry in stock_data:
                line = f"Action: {entry['action']}, Date: {entry['date']}, Price: {entry['price']}\n"
                file.write(line)

        print("Data saved in data.txt")

        return stock_data

    except requests.exceptions.RequestException as e:
        print(f"Error during the data retrieval : {e}")
        return None


if __name__ == "__main__":
    stock_data = retrieve_and_save()
    print(stock_data)
