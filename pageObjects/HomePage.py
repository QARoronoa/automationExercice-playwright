from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page:Page):
        self.page = page

    #locators
        self.btn_signupLogin = page.get_by_role("link", name="Signup / Login")
        self.btn_delete_account = page.get_by_role("link",name=" Delete Account")
        self.btn_continue = page.locator(".btn-primary")
        self.btn_logout = page.get_by_role("link", name="Logout")
        self.btn_contact_us = page.get_by_role("link", name=" Contact us")
        self.btn_test_cases = page.get_by_role("link", name=" Test Cases")
        self.btn_products = page.get_by_role("link", name=" Products")
        self.btn_cart = page.get_by_role("link", name="Cart")
        self.btn_categorie_women = page.locator("a[href='#Women']")
        self.btn_sous_categorie_dress = page.locator('a[href="/category_products/1"]')
        self.recommended_items_bloc = page.locator('.recommended_items')
        self.recommended_items = page.locator("#recommended-item-carousel [data-product-id='4']")
        self.scrollUp_button = page.locator('#scrollUp')


    #methodes
    def verifier_titre_home_page(self):
        expect(self.page).to_have_title("Automation Exercise")

    def cliquer_sur_signupLogin(self):
        self.btn_signupLogin.click()

    def verifier_user_est_connecté(self):
        expect(self.page.locator("text=Logged in as")).to_contain_text("Logged in as")

    def cliquer_sur_delete_accont(self):
        self.btn_delete_account.click()
        expect(self.page.locator("text=Account Deleted!")).to_have_text("Account Deleted!")
        self.btn_continue.click()

    def cliquer_logout(self):
        self.btn_logout.click()
        expect(self.page.locator("text=Login to your account")).to_be_visible()

    def cliquer_sur_contact_us(self):
        expect(self.btn_contact_us).to_be_enabled()
        self.btn_contact_us.click()

    def cliquer_surr_test_cases(self):
        self.btn_test_cases.first.click()
        expect(self.page.locator("span[style='color: red;']")).to_be_visible()
        red_text = self.page.locator("span[style='color: red;']").text_content()
        print(red_text)

    def cliquer_sur_boutton_product(self):
        self.btn_products.click()

    def scroller_vers_subscription(self):
        self.page.locator("#susbscribe_email").scroll_into_view_if_needed()
        expect(self.page.locator(".single-widget")).to_contain_text("Subscription")

    def inserer_un_mail_dans_subscription_et_envoyer(self, email):
        self.page.locator("#susbscribe_email").fill(email)
        self.page.locator("#subscribe").click()

    def capturer_message_alert(self):
        alert_mess = self.page.locator(".alert").text_content()
        print(alert_mess)
        assert "successfully" in alert_mess

    def cliquer_sur_boutton_cart(self):
        self.btn_cart.click()

    def cliquer_sur_la_categorie_women(self):
        self.btn_categorie_women.click()

    def cliquer_sur_sous_categorie(self):
        self.btn_sous_categorie_dress.click()

    def scroller_vers_recommended_items(self):
        self.recommended_items_bloc.scroll_into_view_if_needed()
        expect(self.recommended_items_bloc).to_be_visible()

    def add_a_recommended_items_in_cart(self):
        self.recommended_items.click()

    def click_on_scrollUp_button(self):
        expect(self.scrollUp_button).to_be_visible()
        self.scrollUp_button.click()

    def verify_full_fledge_is_visible(self):
        expect(self.page.locator('h2:has-text("Full-Fledged practice website for Automation Engineers")')).to_be_visible()



