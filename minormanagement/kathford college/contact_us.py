from bs4 import BeautifulSoup

from minormanagement import connectdatabase
from selenium import webdriver

conn = connectdatabase.connect()

myCursor = conn.cursor()

myCursor.execute("SELECT id,links FROM collegelist WHERE college_name LIKE 'Kathford%'")
data = myCursor.fetchone()

numbering = data[0]
linking = data[1]
driver = webdriver.Chrome("C:\\Chrome\\chromedriver.exe")
driver.get(linking)

tit=''
wel=''
python_button = driver.find_element_by_xpath("//*[@id='menu-item-1586']/a").click()
soup = BeautifulSoup(driver.page_source, "html.parser")
titles = soup.find("div", {"class": "container clearfix"})
tit=titles.h1.text
print(tit)
souper = BeautifulSoup(driver.page_source, "html.parser")
title = souper.find("div", {"class": "contact-wrap"})
wel=title.text
print(wel)
myCursor.execute("""INSERT INTO contact(college_id,title,information) VALUES(%s,%s,%s)""", (numbering,tit,wel))
driver.quit()
myCursor.close()
conn.commit()