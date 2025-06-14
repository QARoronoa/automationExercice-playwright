from playwright.sync_api import Page, expect


class ProductDetailPage:
    def __init__(self, page: Page):
        self.page = page

        #locators
        self.btn_add_to_cart = page.locator(".cart")
        self.title_write_your_review = page.locator(".active a")
        self.review_name = page.locator('#name')
        self.review_email = page.locator('#email')
        self.review_section = page.locator('#review')
        self.review_buton_submit = page.locator("#button-review")
        self.review_success_message = page.locator("span[style='font-size: 20px;']")

        #methodes

    def augmenter_la_quantite_a_4(self):
        self.page.locator("#quantity").clear()
        self.page.locator("#quantity").fill("4")

    def cliquer_sur_add_to_cart(self):
        self.btn_add_to_cart.click()

    def verify_write_your_review_is_visible(self):
        expect(self.title_write_your_review).to_be_visible()

    def fill_review_form(self):
        self.review_name.fill("zdjkzfjkzjk")
        self.review_email.fill("isdsk@lsjdl.com")
        self.review_section.fill("cskjksjfksjj")

    def click_on_submit_button(self):
        self.review_buton_submit.click()

    def verify_review_success_message_is_vsible(self):
        expect(self.review_success_message).to_be_visible()