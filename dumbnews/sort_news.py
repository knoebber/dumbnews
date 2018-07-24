'''
Provide an even spread of the top articles in feeds
Takes O(n) time, where n is bounded by limit
'''
def sort_top(feeds, limit=25, depth=0):
    news = []

    while len(news) <= limit:
        for feed in feeds:
            if len(feed.entries) > depth:
                news.append(feed.entries[depth])
        depth += 1

    return news

'''
Sort feed entries by publish date
Takes O(n) time to collect articles using sort_top
    and O(nlog(n)) to sort, where n is bounded by limit
'''
def sort_new(feeds, limit=25, depth=0):
    news = sort_top(feeds, limit=limit, depth=depth)

    news = sorted(news,
            key=lambda article: article.updated_parsed,
            reverse=True)

    return news

sorts = {
        'new' : lambda f: sort_new(f),
        'top'  : lambda f: sort_top(f)
        }
