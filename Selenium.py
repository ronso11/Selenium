from selenium import webdriver
import time


# 1.
chrome_drv = webdriver.Chrome(
    executable_path="C:\\Users\\ron\\Documents\\DevOPs_Course\\chromedriver_win32\\chromedriver.exe")
ff_drv = webdriver.Firefox(
    executable_path="C:\\Users\\ron\\Documents\\DevOPs_Course\\geckodriver-v0.29.1-win64\\geckodriver.exe")

chrome_drv.get("https://www.walla.co.il")
ff_drv.get("http://www.ynet.co.il")
print("End of exercise number 1")
time.sleep(30)
chrome_drv.close()
ff_drv.close()

# 2.
#
chrome_drv = webdriver.Chrome(
    executable_path="C:\\Users\\ron\\Documents\\DevOPs_Course\\chromedriver_win32\\chromedriver.exe")

web_title = "'walla"
chrome_drv.get("https://www.walla.co.il")
chrome_drv.refresh()
get_title = chrome_drv.title

if web_title == get_title:
    print("same title")
else:
    print("not the same title")
print("End of exercise number 2")
time.sleep(30)
chrome_drv.close()
#
# # 3.
# #  yes
#
# # 4.
#
chrome_drv = webdriver.Chrome(
    executable_path="C:\\Users\\ron\\Documents\\DevOPs_Course\\chromedriver_win32\\chromedriver.exe")
chrome_drv.get("https://translate.google.co.il/")
chrome_drv.find_element_by_xpath\
    ("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea").send_keys\
    ("תרגיל מספר 4")
print("End of exercise number 4")
time.sleep(30)
chrome_drv.close()
#
# # 5.
#
ff_drv = webdriver.Firefox(
    executable_path="C:\\Users\\ron\\Documents\\DevOPs_Course\\geckodriver-v0.29.1-win64\\geckodriver.exe")
ff_drv.get("https://www.youtube.com")
ff_drv.find_element_by_name("search_query").send_keys("noga erez cipi")
ff_drv.find_element_by_id("search-icon-legacy").click()
print("End of exercise number 5")
time.sleep(30)
ff_drv.close()
#
# # 6.
#
chrome_drv = webdriver.Chrome(
    executable_path="C:\\Users\\ron\\Documents\\DevOPs_Course\\chromedriver_win32\\chromedriver.exe")
chrome_drv.get("https://translate.google.co.il/")
chrome_drv.find_element_by_xpath\
    ("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea").send_keys\
    ("מספר 1, ")

chrome_drv.find_element_by_class_name("er8xn").send_keys("מספר 2, ")

chrome_drv.find_element_by_xpath(
    '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea')\
    .send_keys("מספר 3")

time.sleep(15)
element = chrome_drv.find_element_by_xpath\
    ("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span")
print(element.text)
print("End of exercise number 6")
time.sleep(30)
chrome_drv.close()
#
# # 7.
#
chrome_drv = webdriver.Chrome(
    executable_path="C:\\Users\\ron\\Documents\\DevOPs_Course\\chromedriver_win32\\chromedriver.exe")
chrome_drv.get("http://www.facebook.com")
chrome_drv.find_element_by_id("email").send_keys("ronsomeh.11@gmail.com")
chrome_drv.find_element_by_name("pass").send_keys("Srmoen908!")
chrome_drv.find_element_by_name("login").click()
print("End of exercise number 7")
time.sleep(30)
chrome_drv.close()
#
#
# # 8.
#
ff_drv = webdriver.Firefox(
    executable_path="C:\\Users\\ron\\Documents\\DevOPs_Course\\geckodriver-v0.29.1-win64\\geckodriver.exe")
ff_drv.get("https://www.facebook.com")
cookies = ff_drv.get_cookies()
print(cookies)
ff_drv.delete_all_cookies()
cookies = ff_drv.get_cookies()
print(cookies)
print("End of exercise number 8")
time.sleep(30)
ff_drv.close()
#
# # 9.
#
chrome_drv = webdriver.Chrome(
    executable_path="C:\\Users\\ron\\Documents\\DevOPs_Course\\chromedriver_win32\\chromedriver.exe")
chrome_drv.get("https://github.com")
chrome_drv.fullscreen_window()
element = chrome_drv.find_element_by_xpath\
    ("/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]")
element.send_keys("selenium")
element.submit()
print("End of exercise number 9")
time.sleep(30)
chrome_drv.close()
#
# # 10.
#
options = webdriver.ChromeOptions()
options.add_argument("--disable-extensions")
chrome_drv = webdriver.Chrome(
    executable_path="C:\\Users\\ron\\Documents\\DevOPs_Course\\chromedriver_win32\\chromedriver.exe", options=options)
print("End of exercise number 10")
time.sleep(30)
chrome_drv.close()
#


