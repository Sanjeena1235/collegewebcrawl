from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains

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


def function1(states):

 for i in range(0,2):
  action = ActionChains(driver);
  python=driver.find_element_by_xpath("//*[@id='menu-item-1586']/a").click()
  firstLevelMenu = driver.find_element_by_xpath("//*[@id='menu-item-142']/a")
  action.move_to_element(firstLevelMenu).perform();
  secondLevelMenu = driver.find_element_by_xpath("//*[@id='menu-item-"+ str(states)+ "']/a");
  action.move_to_element(secondLevelMenu).perform();
  secondLevelMenu.click();
  souper = BeautifulSoup(driver.page_source, "html.parser")
  titles=souper.find("div",{"class":"site-content"})
  print(titles.h1.text)
  states=states+1


function1(143)


state = 146
for i in range(0,2):
  action = ActionChains(driver);
  python=driver.find_element_by_xpath("//*[@id='menu-item-1586']/a").click()
  firstLevelMenu = driver.find_element_by_xpath("//*[@id='menu-item-142']/a")
  action.move_to_element(firstLevelMenu).perform();
  secondLevelMenu = driver.find_element_by_xpath("//*[@id='menu-item-"+ str(state)+ "']/a");
  action.move_to_element(secondLevelMenu).perform();
  secondLevelMenu.click();
  soup = BeautifulSoup(driver.page_source, "html.parser")
  title=soup.find("div",{"class":"site-content"})
  print(title.h1.text)
  state=state+2

state = 1394
for i in range(0,2):
  action = ActionChains(driver);
  python=driver.find_element_by_xpath("//*[@id='menu-item-1586']/a").click()
  firstLevelMenu = driver.find_element_by_xpath("//*[@id='menu-item-142']/a")
  action.move_to_element(firstLevelMenu).perform();
  secondLevelMenu = driver.find_element_by_xpath("//*[@id='menu-item-"+ str(state)+ "']/a");
  action.move_to_element(secondLevelMenu).perform();
  secondLevelMenu.click();
  soup = BeautifulSoup(driver.page_source, "html.parser")
  title=soup.find("div",{"class":"site-content"})
  print(title.h1.text)
  driver.get(linking)
  state=state+1

driver.quit()
myCursor.close()
conn.commit()

