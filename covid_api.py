import requests
import json
import beepy as beep
import time

link1 = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id="
i = 395
link2 = "&date=23-06-2021"
link = link1 + str(i) + link2
response = requests.get(link)
sessions = response.json()["sessions"]

for session in sessions:
    print(session["name"])
i = 392
link = link1 + str(i) + link2
response = requests.get(link)
sessions2 = response.json()["sessions"]
for session in sessions2:
    print(session["name"])


while(1):
    link1 = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id="
    i = 395
    link2 = "&date=23-06-2021"
    link = link1 + str(i) + link2
    response = requests.get(link)
    sessions = response.json()["sessions"]


    for session in sessions:
        if(session["available_capacity_dose1"]>0 and session["min_age_limit"]==45 and session["vaccine"]=="COVAXIN"):
            if(session["pincode"]==400094 or session["pincode"]==400088 or session["pincode"]==400074 ):
                beep.beep(sound=1)
                print("\n\n\n\n\n\n\n\n")
                print(session["name"])
                print(session["pincode"])
                print("\n\n\n\n\n\n\n")
                #print(session)
    link1 = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id="
    i = 392
    link2 = "&date=23-06-2021"
    link = link1 + str(i) + link2
    response = requests.get(link)
    sessions = response.json()["sessions"]
    for session in sessions:
        if(session["available_capacity_dose1"]>0 and session["min_age_limit"]==45 and session["vaccine"]=="COVAXIN"):
            if(session["pincode"]==400094 or session["pincode"]==400088 or session["pincode"]==400074 ):
                beep.beep(sound=1)
                print("\n\n\n\n\n\n\n\n")
                print(session["name"])
                print(session["pincode"])
                print("\n\n\n\n\n\n\n")
                #print(session)

    time.sleep(6)
