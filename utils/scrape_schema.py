from bs4 import BeautifulSoup as bs, SoupStrainer as ss
import requests

SCHEMA_URL = "https://ssis.nu/?p=scheman"

def scrape_schema():
    r = requests.get(SCHEMA_URL)

    soup = bs(r.content, "html5lib")


    output = ""
    for line in soup.find_all("a"):
        if line.text.startswith("Te"):
            output += "[" + line.text + "](" + line["href"] + ")\n"
            #output += "**" + line.text + "** - " + line["href"] + "\n"
    
    return output


        