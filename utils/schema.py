import json

import requests
import texttable
from bs4 import BeautifulSoup as bs

SCHEMA_URL = "https://ssis.nu/?p=scheman"
URL = "https://api.ssis.nu/cal/?room="

def scrape_schema(class_):
    r = requests.get(SCHEMA_URL)

    soup = bs(r.content, "html5lib")

    for line in soup.find_all("a"):
        if line.text.lower().startswith(class_.lower()):
            output = line["href"]
    
    return output

def fetch_schema(class_):

    r = requests.get(URL + class_.lower())
    j = json.loads(r.content)


    table_obj = texttable.Texttable(50)
    table_obj.set_cols_align(["c", "c", "c"])
    table_obj.set_cols_dtype(["t", "t", "t"])
    rows = [["LEKTION", "KLASSRUM", "TID"]]

    for lession in j:
        try:
            li = list(lession["participants"].split(", "))
            if next((s for s in li if "SSIS-Klassrum-" in s), None) is not None:
                classroom = next((s for s in li if "SSIS-Klassrum-" in s), None)
            else:
                raise Exception()
        except:
            classroom = "?"
        
        #cleaning up classroom string
        classroom = classroom.replace("SSIS-Klassrum-", "")
        classroom = classroom.split(" (")[0] # removing the unnecesary (35)

        time = lession["start_time"] + " - " + lession["end_time"]


        rows.append([lession["subject"], classroom, time])

    table_obj.add_rows(rows)
    output = "```" + table_obj.draw() + "```"
    return output

