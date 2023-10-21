#use requests for requesting header from the website and saving the respose in the response variable
#import BeautifulSoup version 4
#use lxml as a parser
#use smtlib for sending emails
#created an email account and an App passowrd to send emails from our python project

import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
url="https://www.amazon.co.uk/Tefal-Capacity-Programs-EY801827-Exclusive/dp/B0BFFQD43H/ref=sr_1_1_sspa?crid=B02SDI9YO5TW&keywords=air+fryers&qid=1679670560&sprefix=Air%2Caps%2C91&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
header = {'Acent-Language': 'en-US,en;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}


response = requests.get(url, headers=header)
print(response)
soup = BeautifulSoup(response.content, "lxml")
title = soup.title.string
print(title)

#now go to website and click on the price and right-click on it and click inspect, get the Id or class that is
#responsible for the price. here I found class and then get the text

price = soup.find(name="span", class_="a-offscreen").get_text()
price_without_currency = price.split("£")[1]
price_as_float=float(price_without_currency)
print(price_as_float)
#I want the price below £140, but to test the system is working i chose less than £200 as the current value is £179.99
#if price_as_float < 200:
if price_as_float < 140:
    my_gmail = "myworkuse93@gmail.com"
    password = "{{ github.gmail_secret }}"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()  # make connection secure
    connection.login(user=my_gmail, password=password)
    subject = "Amazon Price Change Alert!"
    message = f"{title} is now {price}. Buy the Air Fryer now!"
    msg = f"Subject:Amazon Price Alert\n\n{message}".encode('utf8')
    connection.sendmail(from_addr="mohsinaahmedchowdhury@gmail.com", to_addrs=my_gmail, msg=msg)
    print("Email has sent successfully")
    connection.close()


