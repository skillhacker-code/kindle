from distutils.command.upload import upload
import shutil 
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Below Function copy the clippings to a folder of your liking , you must give same destination in uploadToWebsite Fucntion 

def copyVocab():
    source=r"H:\documents\My Clippings.txt" #this was the destination for Kindle that i use
    destination=r'destination of the clipping to be saved here' # Destination of Kindle clipping to be saved
    try:
        shutil.copyfile(source,destination)
    except shutil.SameFileError:
        print('source and destination represent same file')
    except IsADirectoryError:
        print('Destination is a direcotory')
    except PermissionError:
        print('permission denied')
    except:
        print('error occured while copying file / Kindle is not Connected ')


def uploadToWebsite():
    brave_path=r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" # Becuase I use Brave
    driver_path=r"E:\driver 0.1\chromedriver.exe" # latest chrome driver downloaded

    chrome_options=webdriver.ChromeOptions()

    chrome_options.binary_location=brave_path
    chrome_options.add_experimental_option('detach',True)
    browser=webdriver.Chrome(executable_path=driver_path,options=chrome_options) 
    browser.get('https://kindle-clippings.us.aldryn.io/')
    # time.sleep(5)

    # Signin button home page

    elem=browser.find_elements(By.CSS_SELECTOR,"p")
    signInButton=browser.find_element(by=By.XPATH, value='//*[@id="navbarSupportedContent"]/ul[2]/li[2]/a')
    signInButton.click()

    # Login Page and Sign In
    emailInput='emailIdHere' #input your email id here
    passwordInput="passwordHere" #input your password here
    
    email=browser.find_element(by=By.XPATH, value=r'//*[@id="id_login"]')
    password=browser.find_element(by=By.XPATH, value=r'//*[@id="id_password"]')
    loginButton=browser.find_element(by=By.XPATH, value=r'/html/body/div/div/div[2]/form/button')

    email.send_keys(emailInput)
    password.send_keys(passwordInput)
    loginButton.click()

    # Upload Button 
    uploadButton=browser.find_element(by=By.XPATH,value=r"/html/body/div[2]/div/div/div[1]/div[2]/div/a[1]")
    uploadButton.click()

     # Upload File Page
    chooseButton=browser.find_element(by=By.XPATH,value=r'//*[@id="id_clippings_file"]')
    chooseButton.send_keys(r'destination of where the clipping is saved in copyVocab() funciton ') #give the destination of kindle clipping saved here
    finalUploadButton=browser.find_element(by=By.XPATH,value=r'/html/body/div/form/input[2]')
    finalUploadButton.click()

copyVocab()
uploadToWebsite()