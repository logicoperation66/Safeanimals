import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time, sys
from dotenv import load_dotenv

load_dotenv()


def site_opener(url,
                driver):
    driver.get(url)
    return 0


def form_filler(xpath:str,
                variable_to_fill:str,
                driver):
    xpath_form = driver.find_element(By.XPATH, xpath)
    xpath_form.send_keys(variable_to_fill)
    return 0


def select_filler_by_index(xpath:str,
                           select_option:int,
                           driver):

    select = Select(driver.find_element(By.XPATH, xpath))
    select.select_by_index(select_option)

    return 0

def select_filler_by_name(xpath:str,
                          select_option:str,
                          driver):
    select = Select(driver.find_element(By.XPATH, xpath))
    select.select_by_value(select_option)
    return 0


def click(xpath:str,
          driver):
    driver.find_element(By.XPATH, xpath).click()
    return 0


def login(login:str,
          password:str,
          driver):
    xpath_form = driver.find_element(By.XPATH, '//*[@id="username"]')
    xpath_form2 = driver.find_element(By.XPATH, '//*[@id="password"]')
    xpath_form.send_keys(login)
    xpath_form2.send_keys(password)
    login_button = driver.find_element(By.XPATH, '//*[@id="page-content-wrapper"]/section[1]/div[2]/div/div/div[1]/div[2]/div[1]/form/div[4]/div/button')
    login_button.click()
    time.sleep(1)
    accept_button = driver.find_element(By.XPATH, '//*[@id="infoboard-0"]/div/div/div[3]/button')
    accept_button.click()
    coockie_button = driver.find_element(By.XPATH, '//*[@id="cookie"]/div/span')
    coockie_button.click()
    return 0

def scroll(driver):
    driver.execute_script("window.scrollTo(0,0);")
    return 0
