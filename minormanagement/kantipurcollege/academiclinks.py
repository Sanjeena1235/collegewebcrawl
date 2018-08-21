import urllib.request
from bs4 import BeautifulSoup
from minormanagement import connectdatabase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

conn = connectdatabase.connect()

myCursor = conn.cursor()



myCursor.execute("SELECT id,links FROM college WHERE name LIKE 'Kantipur%'")
data=myCursor.fetchone()

temp=''
wel=''
numbering=data[0]
linking=data[1]
driver=webdriver.Chrome("C:\\Chrome\\chromedriver.exe")
driver.get(linking)
python_button = driver.find_element_by_xpath("//*[@id='menu-item-90']/a").click()
contacts=driver.find_element_by_class_name("contact")
temp=(contacts.text)
myCursor.execute("""INSERT INTO contact(college_id,information) VALUES(%s,%s)""", (numbering,temp))

python_button2=driver.find_element_by_xpath('/html/body/div[1]/section[2]/div/div/div/a').click()
#review=driver.find_element_by_class_name("col-md-9 content-main")
review=driver.find_element_by_css_selector(".col-md-9.content-main")
wel=(review.text)
myCursor.execute("""INSERT INTO information(college_id,description) VALUES(%s,%s)""", (numbering,wel))
driver.quit()
myCursor.close()
conn.commit()
conn.close()