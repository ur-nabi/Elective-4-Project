import requests
from bs4 import BeautifulSoup
import csv

# Define the target URL
url = 'https://www.youtube.com/'  # Replace with the actual URL you want to scrape

# Fetch the HTML content of the page
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Define the data list to store extracted information
    data = []

    # Scrape the desired elements (adjust based on your target website's HTML structure)
    for item in soup.find_all('div', class_='item'):  # Replace 'div' and 'item' with actual tags and classes
        title = item.find('h2').text.strip()  # Replace 'h2' with the correct tag for titles
        price = item.find('span', class_='price').text.strip()  # Replace 'span' and 'price' accordingly
        data.append([title, price])

    # Save the extracted data to a CSV file
    with open('data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price'])  # Column headers
        writer.writerows(data)

    print("Data successfully scraped and saved to 'data.csv'.")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
