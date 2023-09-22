import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import credentials  # for inputting the credentials


def parse_links():
    # scrape all accounts to unfollow
    html_file = open(credentials.path_to_file)
    soup = BeautifulSoup(html_file, 'html.parser')

    a_tags = soup.find_all('a')  # finds all links

    links = []  # to contain the links
    for tag in a_tags:
        links.append(tag['href'])

    for link in links:
        # display the account links, can be removed if desired
        print(str(links.index(link)) + ': ' + link)
    return links


links = parse_links()
driver = webdriver.Chrome()

## login ##
driver.get("https://instagram.com")
time.sleep(3)

# username form
username_field = driver.find_element(By.NAME, "username")
username_field.send_keys(credentials.username)

# password form
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys(credentials.password)

# click "login" button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
try:
    login_button.click()
except:
    print('There was a problem executing the login action')
    driver.quit()
    quit()

# wait for login to finish
time.sleep(6)

## unfollowing profiles ##
for link in links:
    driver.get(link)  # get the profile
    time.sleep(1.5)  # wait for page to load

    try:
        # click 'unfollow' (the XPATH to the unfollow button)
        driver.find_element(By.XPATH, "./html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div/button").click()
        # confirm 'unfollow' (again, the XPATH to the unfollow button)
        driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/button[1]").click()
        time.sleep(1) # wait for the request to be confirmed
    except:
        print('There was a problem finding the \'unfollow\' button')

# exit
driver.quit()
