from playwright.sync_api import Page

class AccountSuccessPage:
    def __init__(self, page: Page):
        self.page = page

        # =====Locators=====
        self.btn_continue = page.locator("a:has-text('Continue')")
        self.msg_confirmation = page.locator("h1:has-text('Your Account Has Been Created!')")

    # =====Action Methods======
    def get_confirmation_msg(self):
        return self.msg_confirmation

    def click_continue(self):
        self.btn_continue.click()
