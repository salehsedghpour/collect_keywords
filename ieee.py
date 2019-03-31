from requests_html import HTMLSession
session = HTMLSession()
words=[]
with open('word.csv') as i:
    for item in i:
        if item != "\n":
            words.append(item.rstrip())

words = ['bus']
for word in words:
    temp = ""
    item_temp = ""
    for item in word.split():
        if item.isspace():
            item_temp = '%20'
        else:
            item_temp =  item
        temp = temp + item_temp +'%20'
    r = session.get("https://ieeexplore.ieee.org/search/searchresult.jsp?action=search&newsearch=true&searchField=Search_All&matchBoolean=true&queryText=(%22Author%20Keywords%22:"+temp+")&refinements=ContentType:Journals%20.AND.%20Magazines&ranges=2018_2019_Year")
    r.html.render(timeout=30)
    for item in r.html.find('div.Dashboard-header'):
        print(item.text)
    #print(r.html.find('span'))
