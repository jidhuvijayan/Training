from sys import argv
import requests
def get_person_data(email, api_key):
    url = "https://api.fullcontact.com/v3/person.enrich"
    headers = { "Authorization" : "Bearer {}".format(api_key) }
    data = {"email": email}
    r = requests.post(url=url, headers=headers, json=data)
    return r.json()
email_list=["anubhav.yadav@fullcontact.com",
    "aswani@fullcontact.com",
    "sruthi.soman@fullcontact.com",
    "aiswarya@fullcontact.com",
    "sruthy@fullcontact.com",
    "sivapriya@fullcontact.com",
    "ramseena.pa@fullcontact.com",
    "amitha.chalappuram@fullcontact.com",
    "jismy@fullcontact.com",
    "jidhu@fullcontact.com",
    "anu@fullcontact.com",
    "bimsha@fullcontact.com",
    "haritha@fullcontact.com"
   ]
api_key 
if __name__ == '__main__':

    def get_person_data_for_list(email_list,api_key):
        person_data_list=[]
        for email in email_list:
            d=get_person_data(email,api_key)
            person_data_list.append(d)
        return person_data_list
    s=get_person_data_for_list(email_list,api_key)
    print s
