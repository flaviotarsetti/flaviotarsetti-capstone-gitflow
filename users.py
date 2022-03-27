from collections import Counter

def get_top_users(tweets):
    users = Counter(d['user']["username"] for d in tweets)
    top_users = sorted(users.items(), key=lambda item: item[1], reverse=True)
    print('{:^4}{:^30}{:^20}'.format("N°","Username", "Number of tweets"))
    for i in range(10):
        print('{:^4}{:^30}{:^20}'.format(i+1, top_users[i][0], top_users[i][1]))