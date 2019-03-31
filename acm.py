from requests_html import HTMLSession
session = HTMLSession()
words=[]
with open('word.csv') as i:
    for item in i:
        if item != "\n":
            words.append(item.rstrip())


for word in words:
    temp = ""
    item_temp = ""
    for item in word.split():
        if item.isspace():
            item_temp = '%20'
        else:
            item_temp = '%252B' + item
        temp = temp + item_temp +'%20'
    r = session.get("https://dl.acm.org/results.cfm?query=keywords.author.keyword:(" + temp + ")&within=owners.owner=HOSTED&filtered=&dte=2018&bfr=")
    print(r.html.find('div#searchtots > strong')[0].text+',')
