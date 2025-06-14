from playwright.sync_api import Page, expect


class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page

    #locators
        self.adressLivraison = page.locator("#address_delivery li:not(.address_title)")
        self.adressFacturation = page.locator(" #address_invoice li:not(.address_title)")
        self.btn_place_order = page.locator(".check_out")
        self.text_aera = page.locator('.form-control')

    #methodes

    def comparer_les_adresses(self):
        delevery_address = self.adressLivraison.all_inner_texts()
        billing_address = self.adressFacturation.all_inner_texts()
        assert delevery_address == billing_address

    def cliquer_sur_checkout(self):
        self.btn_place_order.click()

    def write_a_comment_in_aera_text(self):
        expect(self.text_aera).to_be_visible()
        self.text_aera.fill("fkllkkdjfkldjfkjd")

    def click_on_place_order_button(self):
        expect(self.btn_place_order).to_be_enabled()
        self.btn_place_order.click()
