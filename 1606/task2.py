

from bs4 import BeautifulSoup

with open("phases_soften.html", "r") as file:
    fp = file.read()
    
soup = BeautifulSoup(fp, "html.parser")
headers = soup.find_all("h3")

phases = {0: "Testing", 1:"Deploynet", 2:"Development", 3:"monitoring"}

for i in range(4):
    print(headers[i].get_text(), phases[i])
    print(headers[i].find_next("p").get_text())
    print()
# print(soup)