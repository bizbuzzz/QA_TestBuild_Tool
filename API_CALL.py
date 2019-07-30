import requests
import json
import numpy as np

array = np.array(["9DlCHWEg0tYjjGCxgNrqhpa4Ect2","UYEfqCf6kCUR3RjA1hMYSTkfZ7m1",'7BcSA21UQbTOQIEYNMpdB91DzmF3','3hyKr6wcWeZJqPcKjRhrZhSu2J53',
"uDRXjH8cAtgh3LCy5WocAhEO1TI3",
"MpuvbdwZYmYTNwCiF7yriK22QFA2",
"6xwbSZ4Pt7expgK2FsyqU6ff7Wh1",
"iZeU5QCYAHRuLJsxEQIXY768JYf2",
"TkGbqKqceyTehHmxhzgIKWeGNR83"])




body = {
       "offerStatus": "ONGOING_OFFER",
       "bizCashBackRules": {
           "totalNumberOfNewCustomersEligible4CashBack": 50,
           "minOrderVal4CashBackInPaise": 25000,
           "orderNumberEligibleForCashBack": [
               1,
               2,
               3,
               4,
               5,
               6,
               7,
               8,
               9,
               10
           ],
           "cashBackValInPaiseForOrderNumber": [
               5000,
               5000,
               5000,
               5000,
               5000,
               5000,
               5000,
               5000,
               5000,
               5000
           ]
       },
       "bizCashBackReport": {
           "numberOfNewCustomersUsingCashBackOffer": 0,
           "numberOfNewCustomersEligible4CashBack": 50,
           "totalCashPaidToCustomersInPaise": 0,
           "offerStartedOnTimeStamp": 1556116516000
       }
   }

headers = {
    "API_KEY":"rOXJaQBmSgBtD5Y6wbQvy2IlT7V7UyyX",
    "API_PASSWD":"D2E4E9F868281",
    "Content-Type":"application/json"
}

for i in range(len(array)):
    url = 'https://appstaging-dot-bizbuzzztestbed-8ba40.appspot.com/commons/start_cash_back_offer_for_biz/'+array[i]
    apiresponse = requests.post(url, json=body, headers=headers)
    jsons = apiresponse.json()
    print("UserID: "+array[i]+ "    result:" + jsons['result']+",   code:" + str(apiresponse.status_code))
       
