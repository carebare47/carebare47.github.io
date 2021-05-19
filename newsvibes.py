#!/usr/bin/python3.8
# python3.8 -m pip install newsapi-python
from newsapi import NewsApiClient

class NewsVibes():
    def __init__(self, terms):
        self.newsapi = NewsApiClient(api_key='daea6be269b844b784e7ff55ba7fa464')
        range_1 = ['2021-05-18', '2021-05-19']
        range_2 = ['2021-04-19', '2021-04-20']
        for term in terms:
            self.compare(term, new=range_1, old=range_2)

    def compare(self, term, new, old):
        print("Term: {}".format(term))
        a = self.get_articles(new[0], new[1], term)
        b = self.get_articles(old[0], old[1], term)
        print("\tnew: ")
        self.get_pos_neg(a)
        print("\told: ")
        self.get_pos_neg(b)
    
    def get_articles(self, from_date, to_date, term='bitcoin'):
        return self.newsapi.get_everything(q=term, from_param=from_date, to=to_date, language='en', sort_by='relevancy')
    
    def get_pos_neg(self, articles):
        positive=0
        negative=0
        for key, value in articles.items():
            if 'articles' not in key:
                    print("{a}: {b}".format(a=key, b=value))
            else:
                    for l in value:
                            for i, k in l.items():
                                    if 'description' in i:
                                        negative = negative + k.count('fell')
                                        negative = negative + k.count('sunk')
                                        negative = negative + k.count('downk')
                                        negative = negative + k.count('dropped')
                                        negative = negative + k.count('crashing')
                                        positive = positive + k.count('rose')
                                        positive = positive + k.count('risen')
                                        positive = positive + k.count('climbed')
                                        positive = positive + k.count('up')
                                        # print("{a}: {b}".format(a=i, b=k))
    
        print("\t\tplus: {a}\n\t\tminus: {b}".format(a=positive, b=negative))


n = NewsVibes(['bitcoin', 'ether', 'etherium'])
