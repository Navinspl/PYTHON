months=["january","February","March","April","may","june","july","August","September","October","November","December"]
first_quarter=months[0:3]
first_quarter=months[3:6]
third_quarter=months[6:9]
fourth_quarter=months[9:12]
fourth_quarter=months[0:12]
print(months[0:3],months[9:12],months[6:9],months[3:6])
print(len(months))
del months[4]
print(months[:12])
months.append("Bananas")
print(months[:12])
months.insert(5,"Apple")
print(months[:12])
months.remove("Apple")
print(months[:12])