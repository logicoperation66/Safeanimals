import datetime
import os
import time
from web import webactions
from data_export import data_func
import csv
from selenium import webdriver
import pyautogui
from dotenv import load_dotenv

load_dotenv()

login = os.getenv("sa_login")
password = os.getenv("sa_password")
print(login, password)
url = 'https://www.safe-animal.eu/pl/dodaj-zwierze/Animals/add'

if __name__ == "__main__":
    #Open csv with bunch of data to upload
    with open("./BAZA DANYCH SCHRONISKO - BAZA DANYCH.csv", 'r', encoding="UTF-8") as data:
        reader = csv.reader(data)
        SS = f"{datetime.datetime.now()}"
        repired_SS = SS.replace(".", "-")
        for i in reader:
            driver = webdriver.Chrome()
            #Ope web browser and specific url
            webactions.site_opener(url=url,
                                   driver=driver)
            time.sleep(2)
            webactions.login(login=login,
                             password=password,
                             driver=driver)
            time.sleep(1)
            #Chip
            webactions.form_filler(xpath='//*[@id="zNumerId"]',
                                   variable_to_fill=i[1],
                                   driver=driver)
            #Imie
            webactions.form_filler(xpath='//*[@id="zImie"]',
                                   variable_to_fill=i[0],
                                   driver=driver)
            #RASA
            webactions.form_filler(xpath='//*[@id="zRasa"]',
                                   variable_to_fill="MIX",
                                   driver=driver)
            #MAŚĆ
            webactions.form_filler(xpath='//*[@id="zMasc"]',
                                   variable_to_fill=i[5],
                                   driver=driver)
            #ŚIERŚĆ
            webactions.form_filler(xpath='//*[@id="zSiersc"]',
                                   variable_to_fill="ŚREDNI",
                                   driver=driver)
            #Gatunek
            webactions.select_filler_by_index(xpath='//*[@id="zGatunek"]',
                                              select_option=1,
                                              driver=driver)
            #SEX !!! [I'm just too old for that kind of jokes...]
            if i[3] == 'SAMIEC':
                sex = 1
            else:
                sex = 2

            webactions.select_filler_by_index(xpath='//*[@id="zPlec"]',
                                              select_option=sex,
                                              driver=driver)
            #Birth date
            num_of_months = i[4]
            month, year = data_func.subtract_months_from_now(int(num_of_months))
            webactions.select_filler_by_index(xpath='//*[@id="zDataUr1"]',
                                              select_option=month,
                                              driver=driver)

            webactions.select_filler_by_name(xpath='//*[@id="zDataUr2"]',
                                             select_option=str(year),
                                             driver=driver)
            time.sleep(1)
            webactions.scroll(driver=driver)
            ss = pyautogui.screenshot()

            time.sleep(10)
            try:
                webactions.click(xpath='/html/body/div[2]/div[2]/section[1]/section[2]/div/div[1]/div[3]/form/ul/li[2]',
                                 driver=driver)
            except Exception as e: print(e
                                         )
            time.sleep(1)
            webactions.select_filler_by_index(xpath='//*[@id="ownerType"]',
                                              select_option=1,
                                              driver=driver)

            webactions.click(xpath='//*[@id="pasteOwnerData"]',
                             driver=driver)
            webactions.click(xpath='//*[@id="payment-required-submit"]/input',
                             driver=driver)
            print("Dpa")
            time.sleep(1)
            driver.quit()

            # print("If all is ok now we should only save this shit\n and pop out this element from csv")
            print(f"I think we are done for this dog: {i[0]}, {i[1]}")




