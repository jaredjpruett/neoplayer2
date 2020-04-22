class Locator():
    XPath = None
    Class = None

    def __init__(self, XPath=None, Class=None):
        self.XPath = XPath
        self.Class = Class

login = {
    'field_username'    : Locator(".//*[@id='content']/table/tbody/tr/td/div[3]/div[4]/form/div/div[1]/div[2]/input"),
    'field_password'    : Locator(".//*[@id='content']/table/tbody/tr/td/div[3]/div[4]/form/div/div[2]/div[2]/input"),
    'button_login'      : Locator(".//*[@id='content']/table/tbody/tr/td/div[3]/div[4]/form/input[2]", "welcomeLoginButton"),
}

bank = {
    'element_field_withdraw'    : Locator(".//*[@id='content']/table/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/div/input[1]"),
    'element_button_withdraw'   : Locator(".//*[@id='content']/table/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/div/input[2]"),
}
