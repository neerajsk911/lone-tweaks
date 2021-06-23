"""

Author: Neeraj S Kumar
Handle: w1tch3r

A Python Program that parses the JSON returned by the API request for slots by a week and prints
them slots available and highlights any available slots! 

"""
import requests
import time

class SlotFinder:
    def __init__(self):
        self.uri="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?"
        self.parameters={
                "pincode":690533,
                "date":"25-06-2021"
        }
        # self.headers={
        #         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        # }
        self.pincodes=[690533,690526,690525,690518,690501,690502]
        self.foundSessions=0
        self.foundString=""
        self.logString=""
        self.responseString=None
    

    def generateParams(self):
        for i in self.pincodes:
            self.parameters['pincode']=i
            self.checkSlot()
    
    def checkSlot(self):
        try:
            responseString=requests.get(url=self.uri,params=self.parameters)
            self.responseString=responseString
            if responseString.status_code ==200:
                responseData=responseString.json()
                if len(responseData['centers']):
                    for _ in range(len(responseData['centers'])):
                        centerName=responseData['centers'][_]['name']
                        pincode=responseData['centers'][_]['pincode']
                        print(f"{centerName}({pincode}):")
                        self.logString+=f"\n\n{centerName}({pincode}):"
                        sessions=responseData['centers'][_]['sessions']
                        hit=0
                        for i in sessions:
                            hit+=i['available_capacity_dose2']
                            if i['available_capacity_dose2']>0:
                                print(f"\033[92m{i['date']}:{i['available_capacity_dose2']}")
                                self.logString+=f"\n\n{i['date']}:{i['available_capacity_dose2']}"
                                print(f"\033[92m {i['available_capacity_dose2']} slot(s) available in {centerName}({pincode}) for {i['date']}\033[0;37;40m")
                                self.logString+=f"\n\n{i['available_capacity_dose2']} slot(s) available in {centerName}({pincode}) for {i['date']}"
                                self.foundSession()
                                self.updateFoundString(centerName,pincode,i['date'],i['available_capacity_dose2'])
                                hit+=i['available_capacity_dose2']
                            else:
                                print(f"\033[0;37;40m{i['date']}:{i['available_capacity_dose2']}")
                                self.logString+=f"\n\n{i['date']}:{i['available_capacity_dose2']} slots"
                        self.logString+=f"\n\n{i['available_capacity_dose2']} total slot(s) available in {centerName}({pincode}) spread among dates" if hit>0 else ""
            else:
                print(f"{responseString.status_code} received!")
        except requests.exceptions.ConnectionError:
            print("Unable to connect to CoWin portal! Check internet connection of the bot!")
            self.logString+=f"Bot error! Message:{requests.exceptions.ConnectionError.getMessage}"
            print(self.logString)
            time.sleep(5)
                        
    def foundSession(self):
        self.foundSessions+=1
    
    def getFoundSession(self):
        return self.foundSessions
    
    def updateFoundString(self,name,pincode,date,count):
        self.foundString+=f"\n{date} : {name}({pincode}) : {count}"

    def getFoundString(self):
        return self.foundString
    
    def getLogString(self):
        return self.logString

    def getStatusCode(self):
        return self.responseString.status_code if self.responseString is not None else -1

# """
if __name__ == '__main__':
    s=SlotFinder()
    s.generateParams()
    print(f"\033[0;37;40mTotal Sessions Found:\033[9m{s.foundSessions}\033[0;37;40m")
    print(s.getFoundString())
# """