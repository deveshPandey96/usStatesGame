# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#
# print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))


import pandas

data = pandas.read_csv("weather_data.csv")

# print(data)
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# temp_avg = data["temp"].mean()
# temp_max = data["temp"].max()
# print(f"Avg temp {temp_avg}")
# print(f"Max temp {temp_max}")
#
# # Get data in column
# print(data["condition"])

# Get data in row
# print(data[data.temp == data["temp"].max()])

def to_fahrenheit(temp):
    temp_f = temp * 9/5 + 32
    return temp_f


monday = data[data.day == "Monday"]
# print(f"Temperature in F: {to_fahrenheit(monday.temp[0])}")

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")