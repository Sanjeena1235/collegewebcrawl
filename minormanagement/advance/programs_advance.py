from bs4 import BeautifulSoup

from minormanagement import connectdatabase
from selenium import webdriver

conn = connectdatabase.connect()

myCursor = conn.cursor()

myCursor.execute("SELECT id,links FROM ioecollege WHERE college_name LIKE 'Advance%'")
data = myCursor.fetchone()

numbering = data[0]
linking = data[1]
driver = webdriver.Chrome("C:\\Chrome\\chromedriver.exe")
driver.get(linking)

state = 1
for i in range(0, 3):
    python_button = driver.find_element_by_xpath("//*[@id='mainMenu']/ul/li[2]/a").click()
    #python_button2 = driver.find_element_by_xpath("//*[@id='menu-item-" + str(state) + "']/a").click()
    python_button3=driver.find_element_by_xpath("//*[@id='mainMenu']/ul/li[2]/ul/li["+str(state)+"]/a").click()
    soup = BeautifulSoup(driver.page_source, "html.parser")
    title = soup.find("div", {"class": "col-sm-12 col-md-12 lead-article"})
    print(title.text)
    state=state+1


driver.quit()
myCursor.close()
conn.commit()