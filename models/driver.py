from selenium.webdriver.firefox.options import Options
from selenium import webdriver


class Driver:

    proxyAddress = str()

    def __init__(self, proxy_ip):
        self.proxyAddress = proxy_ip

    def create_driver(self):
        options = Options()

        driver = webdriver.Firefox(options=options, executable_path='')
        return driver