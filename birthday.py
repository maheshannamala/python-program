import pandas
from smtplib import *
from datetime import *
import random
d=pandas.read_csv("birthdays.csv")
data=d.to_dict()
d1={}
d1=data.copy()

my_email="mahesha132004@gmail.com"
password="drprgagcrmdexgdj"
now=datetime.now()
a=["letter_1.txt","letter_2.txt","letter_3.txt"]
b=random.choice(a)
for i in range(len(d1["month"])):
 if d1["month"][i]==now.month and d1["day"][i]==now.day:
  file=open(f"{b}")
  lst=file.read()
  list=lst.replace("[NAME]",str(d1["name"][i]))
  print(list)
  connection=SMTP("smtp.gmail.com")
  connection.starttls()
  connection.login(my_email,password)
  connection.sendmail(from_addr=my_email,to_addrs=str(d1["email"][i]),msg=f"Subject:Happy Birthday\n\n{list}")
  connection.close()
