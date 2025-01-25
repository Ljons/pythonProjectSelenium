from selenium.webdriver.common.by import By
class HomePage:

    def __init__(self, before):
        self.before = before
    def open(self):
        self.before.get("https://www.demoblaze.com/index.html")

    def click_galaxy_s6(self):
            self.before.find_element(By.XPATH, "//*[text()='Samsung galaxy s6']").click()
