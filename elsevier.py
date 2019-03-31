from requests_html import HTMLSession
session = HTMLSession()
words=[]
with open('word.csv') as i:
    for item in i:
        if item != "\n":
            words.append(item.rstrip())

#words = ['bus']
for word in words:
    temp = ""
    item_temp = ""
    for item in word.split():
        if item.isspace():
            item_temp = '%20'
        else:
            item_temp =  item
        temp = temp +'%20'+ item_temp
    r = session.get("https://www.sciencedirect.com/search?qs=%27"+temp+"%27&show=25&sortBy=relevance&years=2019%2C2018%2C2020&lastSelectedFacet=articleTypes&articleTypes=FLA%2CREV")
    #r.html.render(timeout=30)
    #r.html.find('span.search-body-results-text').text
    print(r.html.find('span.search-body-results-text')[0].text)

    #print(r.html.find('span'))
