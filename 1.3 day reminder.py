from datetime import datetime
import pandas as pd
from random import choice, randint
import smtplib

#-----------------------------------------basic setup---------------------------------------#

MY_EMAIL = "_____________________"
MY_PASSWORD = "__________________"
MY_2EMAIL = "____________________"
today = datetime.now()
today_tuple = (today.month, today.day)

#-------------------------------------------------------------------------------------------#

data1 = pd.read_csv("critical_day.csv")
day_dict = {(data1_row["month"], data1_row["day"]): data1_row for (index, data1_row) in data1.iterrows()}

#---------------------report the day and select action randomly-----------------------------#
if today_tuple in day_dict:
    remind_day = day_dict[today_tuple]["title"]
    data2 = pd.read_csv("activities.csv")
    suggest_action = [choice((data2['things'])) for _ in range(randint(4,5))]
    print(f"{remind_day} is coming !!!!!!!! / Suggest action: {suggest_action}")

# ------------------to send a email to you--------------------------------------------------#
with smtplib.SMTP("_________________") as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_2EMAIL,
        msg=f"Subject:{remind_day} is coming !!!!!!!!\n\nSuggest action: {suggest_action}"



