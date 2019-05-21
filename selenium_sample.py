from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os.path
import codecs
import glob
import os
import shutil
import time
import datetime
from datetime import date, timedelta
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from dateutil.relativedelta import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def Move_to_s3(username,password,source,dest):
    chrome_options = Options()

    chrome_options.add_experimental_option("prefs", {
      "download.default_directory": "C:/Users/purushv/Downloads/Medallia",
      "download.prompt_for_download": False,
    })

    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    url="https://us-east-1.signin.aws.amazon.com/oauth?SignatureVersion=4&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJMOATPLHVSJ563XQ&X-Amz-Date=2019-05-17T22%3A38%3A22.133Z&X-Amz-Signature=e50b21c8f28acfe228ebc2436a94fdc45901c144925fbfa6341279fd274fb447&X-Amz-SignedHeaders=host&client_id=arn%3Aaws%3Aiam%3A%3A015428540659%3Auser%2Fhomepage&redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3Fstate%3DhashArgs%2523%26isauthcode%3Dtrue&response_type=code&state=hashArgs%23"
    url2="https://s3.console.aws.amazon.com/s3/buckets/bw-ea-revenuemanager-qs/"+dest+"/?region=us-west-2&tab=overview"
    try:
        driver.get(url2)
    except:
        print("No such Destination Folder exist")
    #driver.get(url)
    driver.find_element_by_id("resolving_input").send_keys("bestwestern-analytics")
    driver.find_element_by_id("next_button").click()
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id ('password').send_keys(password)
    driver.find_element_by_id("signin_button").click()
    time.sleep(5)
    driver.find_element_by_xpath("(//button[@class='awsui-button awsui-button-size-normal awsui-button-variant-primary awsui-hover-child-icons'])[position()=1]").click()
    driver.find_element_by_id("uploadInput").send_keys(source)
    time.sleep(2)
    for i in range(3):
        driver.find_element_by_id("next").click()
    div_element=driver.find_element_by_xpath("(//button[@class='awsui-button awsui-button-size-normal awsui-button-variant-primary awsui-hover-child-icons'])[position()=1]")
    hover = ActionChains(driver).move_to_element(div_element)
    hover.perform()
    driver.find_element_by_xpath("(//awsui-button[@class='awsui-util-f-r primary-button'])[position()=1]").click()
    time.sleep(2)
    ref=driver.find_element_by_xpath("//div[@class='operation-progress-bar active-fill']")
    t=True
    while t:
        try:
            ref.click()
            t=True
        except:
            t=False
            driver.quit()

