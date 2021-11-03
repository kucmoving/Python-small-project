import tkinter
from tkinter import *
import datetime
import pandas as pd
import pandas_datareader.data as web
import os
import plotly.express as px
########################################
RED = "e7305b"
GREEN = "#9bdeac"

now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day
start_date = 0
end_date = 0
#######################################

def years_collect():
    global start_date
    global end_date
    num = years_entry.get()
    try:
        val = int(num)
        system.config(text="Data has been collected", fg="GREEN")
    except ValueError:
        system.config(text="Please enter number", fg="RED")
    this_year = now.year
    last_year = int(now.year) - int(num)
    raw_start_date = datetime.datetime(last_year, month, day)
    start_date = raw_start_date.strftime('%Y-%m-%d')
    raw_end_date = datetime.datetime(this_year, month, day)
    end_date = raw_end_date.strftime('%Y-%m-%d')


def ticker_collect():
    ticker = fred_entry.get()
    system.config(text="Tickers have been collected.", fg="GREEN")
    tickerlist = (ticker.split())
    with open("fred_ticker.csv", "w") as file:
        file.write("symbol\n")
        for num in tickerlist:
            file.write(num + "\n")

def dl():
    global start_date
    global end_date
    system.config(text="Please wait a moment...^^", fg="GREEN")
    fred_symbol = pd.read_csv("fred_ticker.csv")  #### you can add your ticker inside the csv
    fred_list = fred_symbol.symbol.to_list()
    for fred_data in fred_list:
        print(fred_data)
        df = web.DataReader(fred_data, 'fred', start_date, end_date)
        df.to_csv(f"{fred_data}.csv")
        print(df.head())
        df = pd.read_csv(f'{fred_data}.csv')  ###匯入該檔案CSV檔案
        fig = px.line(df, x='DATE', y=f"{fred_data}", title="Federal Funds Effective Rate")
        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all")
                ])
            )
        )
        fig.show()
    system.config(text="Files have been downloaded! Please Check.", fg="GREEN")


def del_file():
    fred_symbol = pd.read_csv("fred_ticker.csv")  #### you can add your ticker inside the csv
    fred_list = fred_symbol.symbol.to_list()
    for fred_data in fred_list:
        os.remove(f"{fred_data}.csv")
        print("File Removed!")
    os.remove("fred_ticker.csv")
    system.config(text="Files has been deleted!", fg="GREEN")

###UI SETTING###
window = tkinter.Tk()
window.title("Fred data uploader")
window.minsize(width=500, height=200)
window.config(padx=20, pady=20)

#Labels 寫出所有簡介
years = Label(text="Years trace back:")
years.grid(row=1, column=0)

fred = Label(text="Fred Ticker:")
fred.grid(row=4, column=0)

years_remind = Label(text="How many years do you want to trace back. e.g. 10")
years_remind.grid(row=3, column=1)

fred_remind = Label(text="Please go to fred website and enter the ticker like e.g. DFF WALCL T10Y2Y")
fred_remind.grid(row=5, column=1)

#entry 輸入位置
years_entry = Entry(width=85)
years_entry.grid(row=1, column=1)
years_entry.focus()

fred_entry = Entry(width=85)
fred_entry.grid(row=4, column=1)
fred_entry.focus()

# Buttons 製造按鍵
years_enter = Button(text="Enter", command=years_collect)
years_enter.grid(row=1, column=2)

fred_enter = Button(text="Enter", command=ticker_collect)
fred_enter.grid(row=4, column=2)

dl_but = Button(text="Download and Plot!", width=80, height=2, command=dl)
dl_but.grid(row=6, column=1)

del_file_but = Button(text="del_file!", height=2, command=del_file)
del_file_but.grid(row=6, column=2)

system = Label(text="System: Welcome! This is a Fred data downloader!", font='Helvetica 18 bold')
system.grid(row=0, column=1)

###collect
window.mainloop()