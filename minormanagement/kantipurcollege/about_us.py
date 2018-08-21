from bs4 import BeautifulSoup

from minormanagement import connectdatabase
from selenium import webdriver


conn = connectdatabase.connect()

myCursor = conn.cursor()



myCursor.execute("SELECT id,links FROM college WHERE name LIKE 'Kantipur%'")
data=myCursor.fetchone()

numbering=data[0]
linking=data[1]
driver=webdriver.Chrome("C:\\Chrome\\chromedriver.exe")
driver.get(linking)


#python_button = driver.find_element_by_xpath("//*[@id='menu-item-91']/a").click()
#review=driver.find_element_by_class_name("col-md-12")
#python_button2=driver.find_element_by_xpath("//*[@id='menu-item-"+str(state)+"']/a").click()
#review=driver.find_element_by_class_name("col-md-9 content-main")
temp=''
state=92
for i in range(0,2):
     python_button = driver.find_element_by_xpath("//*[@id='menu-item-91']/a").click()
     python_button2 = driver.find_element_by_xpath("//*[@id='menu-item-"+ str(state)+"']/a").click()
     soup= BeautifulSoup(driver.page_source,"html.parser")

     #link=soup.find_all('div', attrs={"class": "col-md-9 content-main"})
     #for lin in link:
        #  faculty = (lin.find('p').text)
     #review=driver.find_element_by_css_selector(".col-md-9.content-main")
       #   print(faculty)
     article_text = ''
     article = soup.find("div", {"class": "col-md-9 content-main"}).findAll('p')
     for element in article:
          article_text += '\n' + ''.join(element.findAll(text=True))
         
     temp=article_text
     myCursor.execute("""INSERT INTO information(college_id,description) VALUES(%s,%s)""",(numbering,temp))
     print(temp)
     state=state+1



driver.quit()
myCursor.close()
conn.commit()
