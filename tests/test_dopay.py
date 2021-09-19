from seleniumbase import BaseCase
import time
from dojah_po.dopay_page import DoPayPage


class DoPayTestCase(BaseCase):

    def test_do_pay(self):
        # Open home page
        self.open('https://newwidget.dojah.io/payment?app_id='
                  '6138a052147a0100341ca124&p_key='
                  'prod_pk_Nehu272p0jW6Cg8DTzC5QBdqq&amount=1')
        # assert the current url
        dopay_url = self.get_current_url()
        self.assert_equal(dopay_url, "https://newwidget.dojah.io/payment?app_id="
                                     "6138a052147a0100341ca124&p_key="
                                     "prod_pk_Nehu272p0jW6Cg8DTzC5QBdqq&amount=1")
        # assert page title
        self.assert_title(DoPayPage.title)
        # assert logo
        time.sleep(5)
        self.assert_element(DoPayPage.logo_icon)
        # assert Secure text
        self.assert_text("Secured", "//div[@id='index']/div/form/div[3]/div[2]/p")
        self.assert_element("div[id='index'] p[class='text-dark-75']")

        # self.assert_true("pay" in "//div[@id='index']/div/form/p" )
        self.assert_text("Transfer of your information is encrypted end-to-end",
                         "//div[@id='index']/div/form/div[3]/div[2]/p[2]")
        self.assert_text("Private",
                         "//div[@id='index']/div/form/div[4]/div[2]/p")
        self.assert_text("Your credentials will never be made accessible to test",
                         "//div[@id='index']/div/form/div[4]/div[2]/p[2]")
        self.assert_text("By clicking continue, you agree to the terms and condition",
                         "//div[@id='index']/div/form/p[2]")
        self.assert_text("Powered by",
                         "//div[@id='index']/div/div[2]/p")
        self.assert_element("//div[@id='index']/div/div[2]/img")
        self.assert_text("Continue",
                         "//div[@id='index']/div/form/button")
        self.click("//div[@id='index']/div/form/button")
        self.click("//div[@id='account-type']/div/form/div/div/div/button/img")
        time.sleep(5)
        self.assert_text("Select account type",
                         "//div[@id='account-type']/div/form/div/p")
        self.assert_element("//div[@id='account-type']/div/form/div/div/div/button/img")
        self.assert_element("//div[@id='account-type']/div/form/div/div/div[2]/button/img")
        self.assert_text("Individual",
                         "//div[@id='account-type']/div/form/div/div/div/p")
        self.assert_text("Corporate",
                         "//div[@id='account-type']/div/form/div/div/div[2]/p")
        self.assert_text("Powered by",
                         "//div[@id='account-type']/div/div[2]/p")
        self.assert_element("//div[@id='account-type']/div/div[2]/img")

        self.assert_text("Continue",
                         "//div[@id='account-type']/div/form/button")

        self.click("//div[@id='account-type']/div/form/div/div/div/button/img")
        time.sleep(5)
        self.assert_element("//div[@id='account-type']/div/div[2]/img")
        time.sleep(5)
        self.click("//div[@id='account-type']/div/form/button")
        self.assert_text("Select your bank",
                         "//div[@id='bank-select']/div/form/div/p")
        self.assert_element("//input[@type='text']")
        self.assert_text("Powered by",
                         "//div[@id='bank-select']/div/div[2]/p")
        self.assert_element("//div[@id='bank-select']/div/div[2]/img")
        self.assert_text("Continue",
                         "//div[@id='bank-select']/div/form/button")
        time.sleep(5)
        self.type("//input[@type='text']", 'kuda')
        time.sleep(5)
        self.click("//div[@id='bank-select']/div/form/div/div[2]/button[9]/img")
        time.sleep(5)
        self.click("//div[@id='bank-select']/div/form/button")
        time.sleep(5)
        self.assert_element("//div[@id='login']/div/form/div/div/img")
       # self.assert_text("Login with the credentials to your Kuda Internet Banking",
               #          "//div[@id='login']/div/form/div/p")
        self.assert_element("#username")
        self.assert_element("#password")
        self.assert_element("#password")
        self.assert_text("Forgot Password?",
                         "//div[@id='login']/div/form/div/div[3]/p")
        self.assert_text("Forgot Password?",
                         "//div[@id='login']/div/form/div/div[3]/p")
        self.assert_text("Powered by",
                         "//div[@id='login']/div/div[2]")
        self.assert_element("//div[@id='login']/div/div[2]/img")
        time.sleep(10)
        self.assert_text("Continue",
                         "//div[@id='login']/div/form/button")
        self.type('#username', 'test@dojah.io')
        time.sleep(5)

        self.click("//div[@id='login']/div/form/div/div[3]/div[2]/label")
        time.sleep(5)
        self.type('#password', 'Exp3n5er_!@')
        time.sleep(5)
        self.click("//div[@id='login']/div/form/button")
        time.sleep(35)
        self.assert_element("//div[@id='account-select']/div/form/div/div/img")
        time.sleep(5)
        self.assert_text("Select the account you want to link",
                         "//div[@id='account-select']/div/form/div/p")
        self.assert_element("//div[@id='account-select']/div/form/div/div[3]/button/div")
        self.assert_text("Powered by",
                         "//div[@id='account-select']/div/div[2]/p")
        self.assert_element("//div[@id='account-select']/div/div[2]")
        self.click("//div[@id='account-select']/div/form/div/div[3]/button/div")
        time.sleep(5)
        self.click("//div[@id='account-select']/div/form/button")
        time.sleep(15)
        self.assert_text("Security Question",
                         "//div[@id='security-question']/div/form/div/p")
        self.assert_text("Please enter your PIN, to complete transacton",
                         "//div[@id='security-question']/div/form/div/p[3]")
        time.sleep(15)
        self.assert_text("Powered by",
                         "//div[@id='security-question']/div/div[2]/p")
        self.assert_element("//div[@id='security-question']/div/div[2]/img")
        self.assert_element("#otp")
        self.type('#otp', '8912')
        time.sleep(5)
        self.click("//div[@id='security-question']/div/form/button")
        time.sleep(35)
        self.click("//div[@id='success']/div/form/div/p[2]")
        time.sleep(15)
