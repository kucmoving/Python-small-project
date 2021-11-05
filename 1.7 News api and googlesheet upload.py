from googleapiclient.discovery import build
from google.oauth2 import service_account
import requests
#-------------------------------------------------------Setup google sheet---------------------------#
SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
SAMPLE_SPREADSHEET_ID = '_____________________________________'                   # the code after d/


service = build('sheets', 'v4', credentials=creds)                                       # Call the Sheets API
sheet = service.spreadsheets()
#-------------------------------------------------------date setting---------------------------#

NEWS_ENDPOINT = "https://newsapi.org/v2/top-headlines"                                   #you can choose other endpoint
NEWS_API_KEY = "_____________________________________"                                   #input your key
news_params = {
    "apiKey": NEWS_API_KEY,
    "country": "gb",
}
#https://newsapi.org/v2/top-headlines this documentation is perfect. it teaches each step really clearly!!
news_response = requests.get(NEWS_ENDPOINT, params=news_params)
#print(news_response.text) #and past it on http://jsonviewer.stack.hu/ i will use this to see which part i should slice^^

headlines = 0
total_list = []
to_clear = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="news!A:C").execute()

for _ in range(10):
    day = news_response.json()["articles"][headlines]['publishedAt'][0:10]
    time = news_response.json()["articles"][headlines]['publishedAt'][11:19]
    articles = news_response.json()["articles"][headlines]['title']
    headlines = headlines + 1
    message = [day, time, articles]
    total_list.append(message)
    print(message)

print(total_list)
to_update = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="news!A:C", valueInputOption="USER_ENTERED", body={"values":total_list}).execute()