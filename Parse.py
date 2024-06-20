from selenium import webdriver

options = webdriver.ChromeOptions()

binary_yandex_driver_file = 'yandexdriver.exe' # path to YandexDriver

service = webdriver.chrome.service.Service(executable_path=binary_yandex_driver_file) #v4.10+
#service = webdriver.ChromeService(executable_path=binary_yandex_driver_file) #v4.11+

driver = webdriver.Chrome(service=service, options=options)
driver.get('https://yandex.ru')
driver.quit()
import requests
st_accept = "text/html"
st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"

headers = {
   "Accept": st_accept,
   "User-Agent": st_useragent
}
req = requests.get("https://stratz.com/players/325135986", headers)

src = req.text
print(src)
