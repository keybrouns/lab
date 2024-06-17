# Task 1

text = "If you need to Link to some research from a website or on social media, We want to encourage you to .Link to a RePEc page instead of directly to the full text."

words = text.split()

words = [word.rstrip(".") for word in words]

count = 0

for word in words:
    if word.endswith("t"):
        count += 1

print(count)


# Task 2

from bs4 import BeautifulSoup

with open(".html", "r") as file:
    fp = file.read()
    
soup = BeautifulSoup(fp, "html.parser")
headers = soup.find_all("h3")


for i in range(4):
    print(headers[i].get_text())
    print(headers[i].find_next("p").get_text())
    print()


# Task 3

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('covid_19_clean.csv')

# Filter the data for Poland
poland_data = data[data['Country/Region'] == 'Poland']

# Convert the 'Date' column to datetime
poland_data['Date'] = pd.to_datetime(poland_data['Date'])

# Plot the number of recovered individuals versus date
plt.figure(figsize=(10, 6))
plt.plot(poland_data['Date'], poland_data['Recovered'], marker='o', linestyle='-')
plt.xlabel('Date')
plt.ylabel('Number of Recovered Individuals')
plt.title('Number of Recovered Individuals in Poland Over Time')
plt.xticks(rotation=45)  # Rotate the date labels for better visibility
plt.tight_layout()  # Adjust layout to make room for rotated labels
plt.show()

# Find and print the earliest date with positive recovered cases
positive_recovered = poland_data[poland_data['Recovered'] > 0]
earliest_positive_date = positive_recovered['Date'].min()
print(f"The earliest date when the number of recovered individuals in Poland is positive: {earliest_positive_date.date()}")



import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("covid_19_clean.cs")

data = df[((df["Country/Region"] == " Poland") & (df["Recovered"]))]
first_day = df[((df["Country/Region"] == " Poland") & (df["Recovered"] > 0))]

print(first_day["Date"])

number = list(data["Recovered"])
print (number)

numeric_data = []

plt.xticks(range(0,100,15))

plt.plot(number)
plt.title("Poland covid 19 graph")

plt.show



