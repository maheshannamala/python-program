import requests
import time
s_api="https://api.sheety.co/d9523cf51042f2fb4b72320790be230f/flightTicketsDeal/prices"
sheety_api="https://api.sheety.co/d9523cf51042f2fb4b72320790be230f/flightTicketsDeal/prices"
token_endpoint="https://test.api.amadeus.com/v1/security/oauth2/token"
iata_api="https://test.api.amadeus.com/v1/reference-data/locations/cities"
head={"Authorization":"Basic bWFoZXNoOm1haGVzaEAxMw"}

AMADEUS_API_KEY="imdUqWNvS7DOprDN3FttTSVHzgiKZBpr"
AMADEUS_SECRET="A1EQQtZyWAYak5l4"

class DataManager:
    def __init__(self):
        self.destination_data={}
    def get_destination_data(self):
            response=requests.get(url=sheety_api,headers=head)
            data=response.json()
            self.destination_data=data['prices']
            print(self.destination_data)
    def destination_code(self):  
         for i in self.destination_data:  
        #     i["iataCode"]="Testing"
        #     print(i)
            new_data={
                 'price':{"iataCode":"Testing"}
            }
            response=requests.put(url=f"{sheety_api}/{i['id']}",json=new_data,headers=head)
            response.raise_for_status()
            print(response.text)
#{self.token}
class FlightSearch:
    def __init__(self):
          self.api_key=AMADEUS_API_KEY
          self.api_secret=AMADEUS_SECRET
          self.token=self.get_token()
    def get_token(self):
        header={
             "content-type":"application/x-www-form-urlencoded"
        }
        body = {
               'grant_type':'client_credentials',
               'client_id':AMADEUS_API_KEY,
               'client_secret':AMADEUS_SECRET
        }
        response=requests.post(url=token_endpoint,headers=header,data=body)
        response.raise_for_status()
        response.json()['access_token']
        print(f"your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()["access_token"]
    def destination_code(self):
         print(f"Using this token to get destination {self.token}")
         header = {"Authorization": f"Bearer {self.token}"}
         query={
              "Keyword":"Paris",
              "max": "2",
              "include": "AIRPORTS",
         }
         response=requests.get(url=iata_api,headers=header,params=query)
         
         result=response.json()
         return result
d=DataManager() 
#d.get_destination_data()


fs=FlightSearch()

print(fs.destination_code())
