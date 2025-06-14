from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page

        #locators
        self.btn_proceed_to_checkout = page.locator(".check_out")
        self.link_register_popin_Checkout = page.get_by_role("link", name="Register / Login")
        self.btn_X = page.locator(".cart_quantity_delete")
        self.mess_cart_empty = page.locator("p[style='font-size: 18px;']")
        #methodes
    def verifier_que_les_articles_sont_presents(self):
        expect(self.page.locator("tr")).to_contain_text(["Blue Top", "Men Tshirt"])

    def verifier_que_l_article_Blue_Top_present(self, article):
        expect(self.page.locator(".cart_description")).to_contain_text(article)

    def verifier_la_quantity(self):
        expect(self.page.locator(".disabled")).to_have_text("4")

    def cliquer_sur_proceed_to_checkout(self):
        expect(self.btn_proceed_to_checkout).to_be_enabled()
        self.btn_proceed_to_checkout.click()

    def cliquer_sur_register_login_popin_checkout(self):
        expect(self.link_register_popin_Checkout).to_be_enabled()
        self.link_register_popin_Checkout.click()

    def supprimer_article_panier(self):
        self.btn_X.click()

    def verifier_que_le_panier_est_vide(self):
        expect(self.mess_cart_empty).to_contain_text("Cart is empty!")