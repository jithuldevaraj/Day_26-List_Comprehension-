import pandas

data = pandas.read_csv("./weather_data.csv")

for (key, value) in data.iterrows():
    if key == 1:
        print(value.day)

    # if value.day == "Monday":
    #     print(value.temp)