from collections import Counter

def get_top_hashtags(tweets):
    all_hashtags = []
    for tweet in tweets:
        # Código basado en https://stackoverflow.com/a/6331688
        all_hashtags += list(tag.strip("#") for tag in tweet["content"].split() if tag.startswith("#"))
    hashtags = Counter(d for d in all_hashtags)
    top_hashtags = sorted(hashtags.items(), key=lambda item: item[1], reverse=True)
    print('{:^4}{:^40}{:^20}'.format("N°","Hashtag", "Number of tweets"))
    for i in range(10):
        print('{:^4}{:^40}{:^20}'.format(i+1, top_hashtags[i][0], top_hashtags[i][1]))