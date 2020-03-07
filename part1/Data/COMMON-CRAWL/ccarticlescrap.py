import urllib.request
from bs4 import BeautifulSoup
urllist=[]
all_articles=[]
with open("/home/tanmay/Documents/DIC/Proj2/ccrankersite.txt") as f:
        for line in f:
            urllist.append(line)
j=1
for urls in urllist:
    print(j)
    f=open('ccarticle'+str(j)+".txt",'w')
    article_url=urls
    try:
       soup = BeautifulSoup(urllib.request.urlopen(article_url), 'html.parser')
    except:
       continue
    soup.prettify()
    print(article_url)
    # retrieve all of the paragraph tags
    try:
        paragraphs=soup.find('article').find_all('p')
    except:
        print("exception occured")
        continue
    for paragraph in paragraphs:
        f.write(paragraph.text)
    j+=1

    all_articles.append(article_url)

