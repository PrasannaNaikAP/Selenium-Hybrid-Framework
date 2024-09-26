class LoginPage:
  textbox_username_id = "Email"
  textbox_password_id = "Password"
  button_login_xpath = "//input[@value='Log in']"
  link_logout_linktext = "Logout"

  def __init__(self, driver):
    self.driver=driver

  def setUsername(self, username):
    self.find_element(By.ID, textbox_username_id).clear()
    self.find_element(By.ID, textbox_username_id).send_keys(username)

  def setPassword(self, password):
    self.find_element(By.ID, textbox_password_id).clear()
    self.find_element(By.ID, textbox_password_id).send_keys(password)
    
    
  
