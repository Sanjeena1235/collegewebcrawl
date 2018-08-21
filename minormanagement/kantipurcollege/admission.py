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


python_button = driver.find_element_by_xpath("//*[@id='menu-item-99']/a").click()
python_button2 = driver.find_element_by_xpath("//*[@id='menu-item-101']/a").click()
soup = BeautifulSoup(driver.page_source, "html.parser")
article_text = ''
article = soup.find("div", {"class": "col-md-9 content-main"}).findAll('p')
for element in article:
    article_text += '\n' + ''.join(element.findAll(text=True))

print(article_text)

python_button = driver.find_element_by_xpath("//*[@id='menu-item-99']/a").click()
python_button3 = driver.find_element_by_xpath("//*[@id='menu-item-1946']/a").click()
souper = BeautifulSoup(driver.page_source, "html.parser")
uls=souper.find_all("div",attrs={"class":"col-md-9 content-main"})
for ul in uls:
    for li in ul.findAll('li'):
        print(li.text)

articles = souper.find_all("div", {"class": "col-md-9 content-main"})
for element in articles:
   procedure=element.text

print(procedure)



driver.quit()
myCursor.close()
conn.commit()
