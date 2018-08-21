from telnetlib import EC

import a as a
import br as br
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait

from minormanagement import connectdatabase
from selenium import webdriver

conn = connectdatabase.connect()

myCursor = conn.cursor()

myCursor.execute("SELECT id,links FROM college WHERE name LIKE 'kathford%'")
data = myCursor.fetchone()

numbering = data[0]
linking = data[1]
driver = webdriver.Chrome("C:\\Chrome\\chromedriver.exe")
driver.get(linking)



python_button = driver.find_element_by_xpath("//*[@id='menu-item-712']/a").click()
soup = BeautifulSoup(driver.page_source, "html.parser")
wel=''
title = soup.find("div", {"class": "text-block center"})
print(title.h3.text)
wel=title.h3.text
article_text = ''
article = soup.find("section", {"class": "section full-width-content parallax nobottommargin notopmargin notoppadding "}).findAll('p')
for element in article:
   article_text += '\n' + ''.join(element.findAll(text=True))

print(article_text)
myCursor.execute("""INSERT INTO information(college_id,title,description) VALUES(%s,%s,%s)""",(numbering,wel,article_text))


states = 2587
tit=''
raw=''
for i in range(0, 3):
  action = ActionChains(driver);
  firstLevelMenu = driver.find_element_by_xpath("//*[@id='menu-item-712']/a")
  action.move_to_element(firstLevelMenu).perform();
  secondLevelMenu = driver.find_element_by_xpath("//*[@id='menu-item-"+ str(states)+ "']/a");
  action.move_to_element(secondLevelMenu).perform();
  secondLevelMenu.click();
  souper = BeautifulSoup(driver.page_source, "html.parser")
  titles=souper.find("div",{"class":"container clearfix"})
  tit=(titles.h1.text)
  new = souper.find("div", {"class": "col_full"})
 # print(new.string())
  raw=new.text
  myCursor.execute("""INSERT INTO information(college_id,title,description) VALUES(%s,%s,%s)""", (numbering,tit,raw))
  print(tit)
  print(raw)
  states = states - 1




driver.quit()
myCursor.close()
conn.commit()
