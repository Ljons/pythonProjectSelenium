from pages.homepage import HomePage

def test_demoblazesite(browser):
    homePage = HomePage(browser)
    homePage.open()
    homePage.click_galaxy_s6()
