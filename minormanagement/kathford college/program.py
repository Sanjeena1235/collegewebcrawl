from bs4 import BeautifulSoup

from minormanagement import connectdatabase
from selenium import webdriver

conn = connectdatabase.connect()

myCursor = conn.cursor()

myCursor.execute("SELECT id,links FROM college WHERE name LIKE 'Kathford%'")
data = myCursor.fetchone()

numbering = data[0]
linking = data[1]
driver = webdriver.Chrome("C:\\Chrome\\chromedriver.exe")
driver.get(linking)

tit=''
wel=''
python_button = driver.find_element_by_xpath("//*[@id='menu-item-1587']/a").click()
python_button2 = driver.find_element_by_xpath("//*[@id='menu-item-2391']/a").click()
souper = BeautifulSoup(driver.page_source, "html.parser")
titles = souper.find("div", {"class": "container clearfix"})
tit=(titles.h1.text)
print(tit)
news = souper.find("div", {"class": "text-block center"})
wel=(news.text)
print(wel)
myCursor.execute("""INSERT INTO programs(college_id,title,description) VALUES(%s,%s,%s)""", (numbering,tit,wel))


temp=''
til=''
state = 2403
for i in range(0, 2):
    python_button = driver.find_element_by_xpath("//*[@id='menu-item-1587']/a").click()
    python_button2 = driver.find_element_by_xpath("//*[@id='menu-item-" + str(state) + "']/a").click()
    soup = BeautifulSoup(driver.page_source, "html.parser")
    title = soup.find("div", {"class": "container clearfix"})
    temp=(title.h1.text)
    print(temp)
    new = soup.find("div", {"class": "text-block center"})
    til=(new.text)
    print(til)
    myCursor.execute("""INSERT INTO programs(college_id,title,description) VALUES(%s,%s,%s)""", (numbering, temp, til))
    state = state - 1

driver.quit()
myCursor.close()
conn.commit()
