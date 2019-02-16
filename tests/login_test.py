from selenium import webdriver
import pytest
import allure
import moment
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils
@pytest.mark.usefixtures("test_setup")

class TestLogin():
    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    def test_logout(self):
        try:
            driver = self.driver
            home = HomePage(driver)
            home.click_welcome()
            home.click_logout()
            x = driver.title
            assert x == "OrangeHRM"

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currTime = moment.now().strftime("%d-%m-%Y_%H:%M:%S")
            testName = utils.whoami()
            screenshotName = testName+"_"+currTime
            allure.attach(self.driver.get_screenshot_as_png(),name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            #driver.get_screenshot_as_file("C:/Users/krishna/PycharmProjects/AF_1/screenshots/" + screenshotName + ".png")
            raise

        except:
            print("We got an exception")
            currTime = moment.now().strftime("%d-%m-%Y_%H:%M:%S")
            testName = utils.whoami()
            screenshotName = testName + "_" + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            raise
        else:
            print("Logout Function executed without exceptions")

        finally:
            print("Close all DB connections or free objects")
            print("End of Logout Function")