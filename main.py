import pandas
import random
import datetime as dt
import smtplib

now = dt.datetime.now()

##################### GETTING THE CURRENT DATE
curent_month = now.month
current_day = now.day

##################### CHECKING IF THE TODAY IS SOMEONES BIRTHDAY
data = pandas.read_csv("birthdays.csv")
data_to_dict = data.to_dict("records")
for info in data_to_dict:
  if curent_month == info['month'] and current_day == info['day']:
    ##################### WRITING A LETTER
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter:
      random_letter = letter.read()
      #CHANGING [NAME] WITH ACTUAL NAME
      letter_to_send = random_letter.replace("[NAME]", info['name'])

    ##################### SENDING THE EMAIL
    my_email = 'YOUR EMAIL ADRRESS'
    password = 'YOUR PASSWORD'

    with smtplib.SMTP('smtp.gmail.com') as connection:
      connection.starttls()
      connection.login(user=my_email, password=password)
      connection.sendmail(from_addr=my_email,
                          to_addrs=info['email'],
                          msg=f'Subject:Happy Birthday\n\n {letter_to_send}')
