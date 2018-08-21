from bs4 import BeautifulSoup

from minormanagement import connectdatabase
from selenium import webdriver

conn = connectdatabase.connect()

myCursor = conn.cursor()

myCursor.execute("SELECT id,links FROM college WHERE name LIKE 'Kantipur%'")
data = myCursor.fetchone()

numbering = data[0]
linking = data[1]
driver = webdriver.Chrome("C:\\Chrome\\chromedriver.exe")
driver.get(linking)

wel=''
tit=''
state = 1006
for i in range(0, 5):
    python_button = driver.find_element_by_xpath("//*[@id='menu-item-998']/a").click()
    python_button2 = driver.find_element_by_xpath("//*[@id='menu-item-" + str(state) + "']/a").click()
    soup = BeautifulSoup(driver.page_source, "html.parser")
    title = soup.find("div", {"class": "col-md-9 content-main"})
    wel=(title.h2.text)
    article_text = ''
    article = soup.find("div", {"class": "col-md-9 content-main"}).findAll('p')
    for element in article:
        article_text += '\n' + ''.join(element.findAll(text=True))

    tit=(article_text)
    myCursor.execute("""INSERT INTO programs(college_id,title,description) VALUES(%s,%s,%s)""", (numbering,wel,tit))
    print(wel)
    print(tit)
    state = state + 1

driver.quit()
myCursor.close()
conn.commit()

