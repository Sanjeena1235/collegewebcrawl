from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains

from minormanagement import connectdatabase
from selenium import webdriver


conn = connectdatabase.connect()

myCursor = conn.cursor()



myCursor.execute("SELECT id,links FROM college WHERE name LIKE 'Pulchowk%'")
data=myCursor.fetchone()

tit=''
wel=''
numbering=data[0]
linking=data[1]
driver=webdriver.Chrome("C:\\Chrome\\chromedriver.exe")
driver.get(linking)

action = ActionChains(driver);
firstLevelMenu = driver.find_element_by_xpath("//*[@id='menu-item-137']/a")
action.move_to_element(firstLevelMenu).perform();
secondLevelMenu = driver.find_element_by_xpath("//*[@id='menu-item-140']/a");
action.move_to_element(secondLevelMenu).perform();
secondLevelMenu.click();
soup = BeautifulSoup(driver.page_source, "html.parser")
title = soup.find("div", {"class": "site-content"})
wel=(title.text)
myCursor.execute("""INSERT INTO information(college_id,title,description) VALUES(%s,%s,%s)""", (numbering,tit,wel))

driver.quit()
myCursor.close()
conn.commit()