import urllib
import urllib.request
from bs4 import BeautifulSoup
from minormanagement import connectdatabase

conn = connectdatabase.connect()


def make_soup(url):
    thepage=urllib.request.urlopen(url)
    soupdata =BeautifulSoup(thepage,"html.parser")
    return soupdata

myCursor = conn.cursor()

supper=make_soup("https://en.wikipedia.org/wiki/Pulchok_Campus")
count=6
for constituent in supper.find_all("a",rel="nofollow"):
    if(count>0):
        if(count!=6 and count!=5 and count!=4):
          linking=constituent.get('href')
          namecollege=(constituent.text)
          myCursor.execute("""INSERT INTO college(name ,links) VALUES(%s,%s)""",(namecollege,linking))
          print(linking)
          print(namecollege)
    count=count-1



soup=make_soup("https://en.wikipedia.org/wiki/Institute_of_Engineering")
object=""
naming=""
count=13

for link in soup.find_all("a", rel="nofollow"):

     if(count > 0):
        if(count!=13 and count!=5 and count!=4 and count!=1):
          object=link.get('href')
          naming=(link.text)
          myCursor.execute("""INSERT INTO college(name ,links) VALUES(%s,%s)""",(naming,object))
          print(link.get('href'))
          print(link.text)
     count = count - 1



for row in soup.find_all("a",rel="nofollow",string=("Janakpur Engineering College","Pulchowk Campus")):
     collegelink=row.get('href')
     name=(row.text)
     myCursor.execute("""INSERT INTO college(name ,links) VALUES(%s,%s)""", (name, collegelink))
     print(collegelink)
     print(name)







conn.commit()
conn.close()

