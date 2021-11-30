#!/usr/bin/python3
# Read weather highs and lows, and output max/min values for each month
#This was not written by a student, and was copy pasted from https://github.com/thrasherht/python-homework-help/blob/main/high_low.py

#Setup Environment
import csv
import datetime
months = {}
month_check = "1"
prcp=0
input_file="Phoenix_2020.csv"

#Read CSV input file, this assumes data column is in accending order
with open(input_file) as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        #Read in row information
        month_num = str(row['DATE'].split('/')[0])
        input_high = int(row['TMAX'])
        input_low = int(row['TMIN'])
        input_prcp = float(row['PRCP'])

        #Calculate running prcp total
        prcp = prcp + input_prcp
        
        #Check if this is a new month, and clear values if it is
        if month_check != month_num:
            del store_high
            del store_low

        #Check if stored value exists, if not set to first input value
        try:
            store_high
        except:
            store_high = input_high
            months[month_num + "_tmax"] = input_high
        try:
            store_low
        except:
            store_low = input_low
            months[month_num + "_tmin"] = input_low

        #Check if stored value needs to be increased
        if store_high < input_high:
            store_high = input_high 
            months[month_num + "_tmax"] = input_high

        #Check if stored value needs to be decreased
        if store_low > input_low:
            store_low = input_low
            months[month_num + "_tmin"] = input_low

        
        #Set working month to check against next loop
        month_check = month_num

        #Clear input data
        del input_high
        del input_low

#This was not written by a student, and was copy pasted from https://github.com/thrasherht/python-homework-help/blob/main/high_low.py

#Print total prcp
print("The total amount of percipitation in Phoenix for 2020 was " + str(prcp) + " inches\n")

#Output temp high values
print("The highest temperature for each month in Phoenix during 2020:")
for month in range(1, 13):
  #Convert month number to name
  num = str(month)
  datetime_object = datetime.datetime.strptime(num, "%m")
  month_name = datetime_object.strftime("%B")

  #Output data
  print(month_name + "'s temperature was " + str(months[num + "_tmax"]) + ".")

print("\n")
#Output temp low values
print("The lowest temperature for each month in Phoenix during 2020:")
for month in range(1, 13):
  #Convert month number to name
  num = str(month)
  datetime_object = datetime.datetime.strptime(num, "%m")
  month_name = datetime_object.strftime("%B")

  #Output data
  print(month_name + "'s temperature was " + str(months[num + "_tmin"]) + ".")

#This was not written by a student, and was copy pasted from https://github.com/thrasherht/python-homework-help/blob/main/high_low.py
