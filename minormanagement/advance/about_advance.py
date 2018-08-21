from bs4 import BeautifulSoup

from minormanagement import connectdatabase
from selenium import webdriver


conn = connectdatabase.connect()

myCursor = conn.cursor()



myCursor.execute("SELECT id,links FROM ioecollege WHERE college_name LIKE 'Advance%'")
data=myCursor.fetchone()

numbering=data[0]
linking=data[1]
driver=webdriver.Chrome("C:\\Chrome\\chromedriver.exe")
driver.get(linking)


python=driver.find_element_by_xpath("//*[@id='mainMenu']/ul/li[1]/a").click()
souper = BeautifulSoup(driver.page_source, "html.parser")
welcome=souper.find("div", {"class": "fCont"})
print(welcome.h1.text)
titles = souper.find("div", {"class": "fCont"}).findAll("p",limit=2)
print(titles[1].text)


python1=driver.find_element_by_xpath("//*[@id='mainMenu']/ul/li[8]/a").click()
soup = BeautifulSoup(driver.page_source, "html.parser")
des=soup.find("div", {"class": "contact-mail"})
print(des.text)




driver.quit()
myCursor.close()
conn.commit()