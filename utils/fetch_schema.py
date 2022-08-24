import json

import requests
import texttable

URL = "https://api.ssis.nu/cal/?room="

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
            classroom = li[2]
        except:
            classroom = "?"

        time = lession["start_time"] + " - " + lession["end_time"]


        rows.append([lession["subject"], classroom, time])

    table_obj.add_rows(rows)
    output = "```" + table_obj.draw() + "```"
    return output

