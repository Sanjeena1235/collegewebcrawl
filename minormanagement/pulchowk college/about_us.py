from bs4 import BeautifulSoup

from minormanagement import connectdatabase
from selenium import webdriver


conn = connectdatabase.connect()

myCursor = conn.cursor()



myCursor.execute("SELECT id,links FROM college WHERE name LIKE 'Pulchowk%'")
data=myCursor.fetchone()

numbering=data[0]
linking=data[1]
driver=webdriver.Chrome("C:\\Chrome\\chromedriver.exe")
driver.get(linking)

tit=''
python_button = driver.find_element_by_xpath("//*[@id='menu-item-45']/a").click()
souper = BeautifulSoup(driver.page_source, "html.parser")
titles = souper.find("div", {"class": "entry-content"})
tit=titles.text
print(tit)


python_button1 = driver.find_element_by_xpath("//*[@id='menu-item-511']/a").click()
soup = BeautifulSoup(driver.page_source, "html.parser")
article_text=''
article= soup.find("div", {"class": "entry-content"}).findAll('p')
for element in article:
    article_text += '\n' + ''.join(element.findAll(text=True))

wel=article_text
print(wel)
myCursor.execute("""INSERT INTO information(college_id,title,description) VALUES(%s,%s,%s)""", (numbering,tit,wel))







driver.quit()
myCursor.close()
conn.commit()