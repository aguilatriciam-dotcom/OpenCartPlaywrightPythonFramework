from playwright.sync_api import expect
from pages.homePage import HomePage
from pages.registrationPage import RegistrationPage
from pages.account_success_page import AccountSuccessPage
from pages.myaccountPage import MyAccountPage
from utils.random_data_util import RandomDataUtil

"""
STEPS:
1. Click on 'My Account' Drop menu
2. Click on 'Register' option
3. Enter new Account Details into the Mandatory Fields (First Name, Last Name, E-Mail,Telephone, Password, Password Confirm and  Privacy Policy Fields)
4. Click on 'Continue' button (ER-1)
5. Click on 'Continue' button that is displayed in the 'Account Success' page (ER-2)

EXPECTED RESULT: User should be logged in, and taken to 'My Account' page
"""

def test_user_registration(page):
    # =====create page object instances=====
    home_page = HomePage(page)
    registration_page = RegistrationPage(page)
    account_success_page = AccountSuccessPage(page)
    my_account_page = MyAccountPage(page)

    # =====Steps 1 and 2: Click on My Account > Register=====
    home_page.click_my_account()
    home_page.click_register()

    # =====Step 3: Enter new Account Details into the Mandatory Fields (First Name, Last Name, E-Mail, Password, and confirm Privacy Policy)=====
    random_data = RandomDataUtil()

    registration_page.set_first_name(random_data.get_first_name())
    registration_page.set_last_name(random_data.get_last_name())
    registration_page.set_email(random_data.get_email())
    registration_page.set_password(random_data.get_password())
    registration_page.tgl_policy()

    # =====Step 4: Click on 'Continue' button (ER-1)=====
    registration_page.btn_continue()

    # =====Step 5: Click on 'Continue' button that is displayed in the 'Account Success' page (ER-2)=====
    account_success_page.click_continue()
    # confirmation_msg = account_success_page.get_confirmation_msg()
    # expect(confirmation_msg).to_have_text("Your Account Has Been Created!")

    # =====EXPECTED RESULT: User should be logged in, and taken to 'My Account' page=====
    expect(my_account_page.get_msg_heading()).to_be_visible(timeout=3000)


