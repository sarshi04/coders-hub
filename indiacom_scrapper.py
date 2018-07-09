from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from pymongo import MongoClient

#chrome webdriver
ch = "C:\\Users\Arshi Sinha\PycharmProjects\chromedriver"
driver = webdriver.Chrome(ch)

#mongoclient for creating database
client1 = MongoClient()
db = client1.indiacom
col2 = db.col2


def get_site():   #function to get the access to the site
    driver.get("https://www.indiacom.com/yellowpage/listcategory.asp?city=9114731&keyword=coaching+classes&businessname=&submit=&SearchOption=KW&criteria=1&searchtype=1&Page=1&Start=1&category=")


def max_window():  #maximize the window
    driver.maximize_window()


def get_fields():  #accessing all the fields on the current page
    time.sleep(20)
    lis = driver.find_elements_by_class_name("cat-title-row")
    link1 = []
    link2 = []
    for i in range(1, 14):
        link1.append(lis[i])
    for j in link1:
        link2.append(j.find_element_by_tag_name('a').get_attribute('href'))
    return link2


def get_links(field):  #accessing all the links of every coaching classes
    link4 = []
    for k in field:
        link3 = []
        driver.get(k)
        lists = driver.find_elements_by_class_name("b_name")
        for j in lists:
            searches = []
            a1 = (j.get_attribute("innerHTML"))
            for l in a1[17:]:
                if l != '"':
                    searches.append(l)
                else:
                    link3.append(''.join(searches))
                    searches = []
                    break
        for i in link3:
            link4.append("https://www.indiacom.com" + i)
        try:
            try:
                driver.find_element_by_xpath('// *[ @ id = "divlisting"] / div[63] / strong / a').click()
            except NoSuchElementException:
                driver.find_element_by_xpath('// *[ @ id = "divlisting"] / div[63] / strong / a[2]').click()
        except NoSuchElementException:
            pass
    return link4


def scrap_data(links):  #scrapping all the required data by clicking on the particular link
    for m in links:
        driver.get(m)
        driver.find_element_by_id('btn_phone').click()
        time.sleep(1)
        addr = driver.find_element_by_css_selector('.mr10.lighttext.lh1').get_attribute('innerText')
        name = driver.find_element_by_tag_name('h1').get_attribute("innerText")
        time.sleep(2)
        ph = driver.find_element_by_name('phone').get_attribute('innerText')
        try:
            courses = driver.find_element_by_id('div_promotext').get_attribute('innerText').split(',')
        except NoSuchElementException:
            pass
        try:
            tag = driver.find_element_by_class_name('divcat').find_element_by_tag_name('strong').get_attribute('innerText')
        except NoSuchElementException:
            tag = driver.find_element_by_class_name('divcat').get_attribute('innerText')
        source = {
            "name": "indiacom",
            "url": m
        }
        if '0731-' in ph:
            ph1 = {
                "ext": ph[:4],
                "phone": ph[5:],
                "source": "indiacom"
            }
        elif '+91' in ph and '-' not in ph:
            ph1 = {
                "ext": ph[:3],
                "phone": ph[3:],
                "source": "indiacom"
            }
        elif "+91-731-" in ph:
            ph.replace('-', '')
            ph1 = {
                "ext": "0731",
                "phone": ph[8:],
                "source": "indiacom"
            }
        add1 = addr[9:]
        land = []
        add3 = []
        k1 = []
        m1 = []
        add3 = add1.split(',')
        a = add3[len(add3) - 1]
        pin1 = a[8:]
        add3.remove(a)
        for k in add3:
            if ("Opp." in k) or ("Near" in k) or ("Above" in k) or ("Behind" in k) or ("Opposite" in k) or ("Below" in k) or ("Square" in k) or ("Infront" in k):
                land.append(k)
                add3.remove(k)
        a = float(len(add3)) / 2
        if a > 1:
            k1 = ",".join(add3[:2])
            m1 = ",".join(add3[2:])
        elif a == 1:
            k1 = ",".join(add3)
        add2 = {
                "city": "Indore",
                "state": "Madhya Pradesh",
                "country": "India",
                "pincode": pin1,
                "landmark": land,
                "address line1": k1,
                "address line2": m1,
                "longitude": " ",
                "latitude": " "
            }

        indiacom_db(name, source, ph1, add2, tag, courses)


def indiacom_db(name, source, ph1, add2, tag, courses):   #creating database using mongodb
    #dictionary format db
    db = {
        'name': name,
        'source': source,
        'phones': ph1,
        'emails': '',
        'contact person': '',
        'websites': '',
        'address': add2,
        'ratings': '',
        'reviews': '',
        'courses': courses,
        'tags': tag,
        'directions': ''
    }
    col2.insert_one(db)
    print(db)


get_site()
max_window()
field = get_fields()
links = get_links(field)
scrap_data(links)
driver.quit()