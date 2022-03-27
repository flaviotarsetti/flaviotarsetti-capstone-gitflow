def get_top_retweets(tweets):
    top_retweets = sorted(tweets, key=lambda d: d['retweetCount'], reverse=True) 
    print('{:^4}{:^70}{:^20}'.format("N°","Tweet URL", "Number of retweets"))
    for i in range(10):
        print('{:^4}{:^70}{:^20}'.format(i+1, top_retweets[i]["url"], top_retweets[i]["retweetCount"]))