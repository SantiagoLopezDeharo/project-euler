weekdays = ["monday", "tuesday", "wednesday", "thursday", 'friday', 'sautrday', 'sunday']
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekday = 365 % 7
counter = 0

for j in range(1, 101):
    for i in range(12):
        if weekdays[weekday] == "sunday":
            counter += 1
        weekday = (weekday + month[i]) % 7
        if (i == 1) and ((1900 + j)%4 == 0):
            weekday = (weekday+1)%7

print(counter)

