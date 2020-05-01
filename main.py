from selenium import webdriver
from time import sleep

url = "https://instagram.com"
username = "born2kickbooty"
password = "Non!2005GJ"

class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        sleep(2)
        # self.driver.find_element_by_xpath("//a[contains(text(), 'Log In')]").click()
        self.driver.find_element_by_name("username").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(password)
        # self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys(username)
        # self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys(password)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button").click()
        sleep(2)
        # self.driver.find_element_by_class_name("aOOlW HoLwm").click()
        # self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        try:
            self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
        except Exception:
            pass

        # self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/a").click()

if __name__ == '__main__':
    bot = InstaBot(username=username, password=password)