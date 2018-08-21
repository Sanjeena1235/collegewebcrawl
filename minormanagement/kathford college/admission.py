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
python_button = driver.find_element_by_xpath("//*[@id='menu-item-3157']/a").click()
souper = BeautifulSoup(driver.page_source, "html.parser")
titles = souper.find("div", {"class": "container clearfix"})
tit=(titles.h1.text)
print(tit)
news = souper.find("div", {"class": "col_half"})
wel=(news.text)
myCursor.execute("""INSERT INTO information(college_id,title,description) VALUES(%s,%s,%s)""", (numbering, tit,wel))
driver.quit()
myCursor.close()
conn.commit()