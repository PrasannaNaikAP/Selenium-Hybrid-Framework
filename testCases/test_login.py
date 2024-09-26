import pytest
from selenium import driver
from pageObjects.LoginPage import LoginPage


class Test_003_Login:
  baseURL = ReadConfig.getApplicationURL()
  username=ReadConfig.getUsername()

  def Home_pageTitle(self, setup):
    self.driver=setup
    self.driver.get(self.baseURL)
    title=driver.title
    if title=="your store":
      self.driver.close()
      assert true

  def LoginPage(self, setup):
    self.driver=setup
    self.driver.get(self.baseUrl)
    self.logpage=LoginPage(self.driver)
    self.logpage.setusername(self.username)
    
    
