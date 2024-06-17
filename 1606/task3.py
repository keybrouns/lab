import pandas as pd

data = pd.read_csv("covid_19_clean.csv")

data['Date'] = pd.to_datetime(data['Date'])

first_june = data[data['Date']=="2020-06-01"]

print(first_june["Deaths"].sum())

mean_confirmed = first_june["Confirmed"].mean()
western_countries = first_june[(first_june["WHO Region"] == "Western Pacific")
    &(first_june["Confirmed"]>mean_confirmed)]

print(western_countries[["Country/Region", "Confirmed"]])
      
# print(first_june["Confirmed"].meand)