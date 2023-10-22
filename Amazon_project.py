import requests, time
from bs4 import BeautifulSoup
import lxml
import smtplib
import os  # Import the os module for environment variables

url = "https://www.amazon.co.uk/Tefal-Capacity-Programs-EY801827-Exclusive/dp/B0BFFQD43H/ref=sr_1_1_sspa?crid=B02SDI9YO5TW&keywords=air+fryers&qid=1679670560&sprefix=Air%2Caps%2C91&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
header = {'Accept-Language': 'en-US,en;q=0.9',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

response = requests.get(url, headers=header)
print(response)
soup = BeautifulSoup(response.content, "lxml")
title = soup.title.string
print(title)

# Find the price element
time.sleep(5) 
#price_element = soup.find(name="span", class_="a-offscreen")
price_element = soup.select_one("span.a-offscreen")
print(price_element)

# Check if the element is found before accessing its text
if price_element:
    # Get the text content of the price element
    price_text = price_element.get_text(strip=True)

    # Check if the price text is not empty and contains the currency symbol "£"
    if price_text and '£' in price_text:
        # Extract the numeric part of the price text
        price_without_currency = price_text.split("£")[1]

        # Convert the price to a float
        price_as_float = float(price_without_currency)
        print(price_as_float)

        # Continue with the rest of your code...
        if price_as_float < 140:
            my_gmail = "myworkuse93@gmail.com"
            password = os.environ.get('GMAIL_SECURITY')  # Retrieve the password from environment variable

            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=my_gmail, password=password)
            subject = "Amazon Price Change Alert!"
            message = f"{title} is now {price_text}. Buy the Air Fryer now!"
            msg = f"Subject:Amazon Price Alert\n\n{message}".encode('utf8')
            connection.sendmail(from_addr="mohsinaahmedchowdhury@gmail.com", to_addrs=my_gmail, msg=msg)
            print("Email has sent successfully")
            connection.close()
    else:
        print("Price format is not as expected.")
else:
    print("Price element not found.")
