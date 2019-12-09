from pathlib import Path
import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

def getresponse(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


filepath = Path("C:/Users/cawalden/Desktop/subdomains.txt")
filepath2 = Path("C:/Users/cawalden/passwords.txt")

with open(filepath2, "r") as f:
    for x in f:
        print(x)



password = "ASDVBDFGHSDF2019dfgdfgdfgdfgldfgdklfgnldfngldnfg2019sdjngfkjdfngjkdnfkjgndfjkgnf2019"

count = re.findall('2019', password)
print(len(count))



# url = "google.com"


# with open(filepath, "r") as f:
#         for x in f:
#             word = x.strip()
#             test_urls = word + "." + url
#             response = getresponse(test_urls)
#             if response:
#                 print("[+] Discovered subdomain " + test_urls)


#####################################################

#Web Scraping

website_url = requests.get("https://ung.edu/student-counseling/faculty-staff-bio/index.php").text

soup = BeautifulSoup(website_url, "lxml")

My_table = soup.find('table', {'class': 'table-bluehead-altbkgd tablesorter'})

link = My_table.findAll('a')


Names  =[]

for x in link:
    Names.append(x.contents)

print(Names)

#
# website_url = requests.get("https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area").text
#
# soup = BeautifulSoup(website_url, "lxml")
#
# My_table = soup.find('table', {'class': 'wikitable sortable'})
#
# links = My_table.findAll('a')
# Countries = []
# for link in links:
#     Countries.append(link.get('title'))
#
#
# df = pd.DataFrame()
# df['Country'] = Countries
# print(df)


































