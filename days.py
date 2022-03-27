from collections import Counter
from datetime import datetime

def get_top_days(tweets):
    days = Counter(d["date"].split("T")[0] for d in tweets)
    top_days = sorted(days.items(), key=lambda item: item[1], reverse=True)
    print('{:^4}{:^30}{:^20}'.format("N°","Day", "Number of tweets"))
    for i in range(min(10, len(top_days))):
        day = datetime.strptime(top_days[i][0], '%Y-%m-%d').strftime("%d-%B-%Y")
        print('{:^4}{:^30}{:^20}'.format(i + 1, day, top_days[i][1]))