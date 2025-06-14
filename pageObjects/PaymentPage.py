from playwright.sync_api import Page, expect


class PaymentPage:

    def __init__(self, page: Page):
        self.page = page

    #locators
        self.champNameCard = page.locator("input[name='name_on_card']")
        self.champNumberCard = page.locator("input[name='card_number']")
        self.champCvcCard = page.locator("input[name='cvc']")
        self.champmonthCard = page.locator("input[name='expiry_month']")
        self.champyearCard = page.locator("input[name='expiry_year']")
        self.btn_pay_order = page.locator("#submit")
        self.btn_continue = page.locator(".btn-primary")
        self.message_order_ok = page.locator("text='Congratulations! Your order has been confirmed!'")
        self.download_invoice_button = page.get_by_role("link", name="Download Invoice")

    #methodes
    def saisir_les_informations_de_la_CB(self, nameCard, numberCard, cvc, month,year):
        self.champNameCard.fill(nameCard)
        self.champNumberCard.fill(numberCard)
        self.champCvcCard.fill(cvc)
        self.champmonthCard.fill(month)
        self.champyearCard.fill(year)


    def cliquer_sur_continue(self):
        self.btn_pay_order.click()
        expect(self.message_order_ok).to_be_visible()
        self.download_invoice_button.click()
        self.btn_continue.click()


