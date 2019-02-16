import pytest

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help = "Type in browser name e.g. Chrome or Firefox.")

@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver

    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        # driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        driver = webdriver.Chrome(executable_path="C:/Users/krishna/PycharmProjects/AF_1/drivers/chromedriver.exe")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="C:/Users/krishna/PycharmProjects/AF_1/drivers/geckodriver.exe")

    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Login Test Completed")
