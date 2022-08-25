import datetime
import os

import fitz

PDF_URL = "https://api.eatery.se/skriv-ut/?id=2401"


# download pdf file from url to root dir

#function to return a formatted version of the day inputted in arguments
def formatDay(day):
    output = ""
    if day == datetime.datetime.today().weekday(): output += "__"

    # weekdays
    if day == 0: output += "**Måndag**"
    if day == 1: output += "**Tisdag**"
    if day == 2: output += "**Onsdag**"
    if day == 3: output += "**Torsdag**"
    if day == 4: output += "**Fredag**"
    
    if day == datetime.datetime.today().weekday(): output += "__"

    output += "\n"

    return output

def scrape_eatery():
    global monday
    global tuesday
    global wednesday
    global thursday
    global friday
    global week

    os.system("wget -t 10 -O meny.pdf " + PDF_URL)
    
    content = ""
    content_clean = ""

    with fitz.open("meny.pdf") as f:
        for page in f:
            content += page.get_text()


    for line in content.splitlines():
        if not "KISTA NOD" in line:
            content_clean += line + "\n"
            

    # add emojis to the text
    content_clean = content_clean.replace("SWEET", ":cake: SWEET") # cake emoji
    content_clean = content_clean.replace("FRUITY", ":tangerine: FRUITY") # mandarin emoji
    content_clean = content_clean.replace("PANCAKE", ":pancakes: PANCAKES") # pancake emoji
    content_clean = content_clean.replace("BURGER", ":hamburger: BURGER") # burger emoji


    # lstrip and rstrip removes unwanted whitespace
    monday = content_clean.split("MÅNDAG")[1].split("TISDAG")[0].lstrip().rstrip()
    tuesday = content_clean.split("TISDAG")[1].split("ONSDAG")[0].lstrip().rstrip()
    wednesday = content_clean.split("ONSDAG")[1].split("TORSDAG")[0].lstrip().rstrip()
    thursday = content_clean.split("TORSDAG")[1].split("FREDAG")[0].lstrip().rstrip()
    friday = content_clean.split("FREDAG")[1].lstrip().rstrip()


    week = [monday, tuesday, wednesday, thursday, friday]

    output = ""

    for day in range(5):
        output += formatDay(day) + week[day] + "\n\n"
    
    return output
