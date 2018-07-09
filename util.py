import os
import time
import urllib.request

url = "http://www.vi.gov.lv/captcha.php"


def get_latest_file_name():
    data_files = os.listdir('data')
    name = sorted(data_files, reverse=True)[0].replace(".png", "")
    return int(name)


def download_images(amount=1):
    file_name_counter = get_latest_file_name()
    for i in range(0, amount):
        file_name_counter += 1
        file_name = str(file_name_counter) + ".png"
        print("Downloading image " + file_name)
        urllib.request.urlretrieve(url, "data/" + file_name)
        time.sleep(0.5)


download_images(5)
