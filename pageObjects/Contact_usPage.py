from playwright.sync_api import Page, expect


class ContactUsPage:

    def __init__(self, page: Page):
        self.page = page

    #locators
        self.champ_name = page.get_by_placeholder("Name")
        self.champ_email = page.locator("input[name='email']")
        self.champ_subject = page.get_by_placeholder("Subject")
        self.champ_message = page.get_by_placeholder("Your Message Here")
        self.btn_submit = page.locator(".btn-primary")
        self.sucess_message = page.locator(".status")
        self.btn_home = page.locator(".btn-success")


    #methodes

    def verifier_que_get_in_touch_est_visible(self):
        expect(self.page.locator("h2[class='title text-center']:nth-child(2)")).to_be_visible()

    def remplir_formulaire_contact(self):
        self.champ_name.fill("kfjdfk")
        self.champ_email.fill("issak92@msn.com")
        self.champ_subject.fill("test")
        self.champ_message.fill("testtettsttettstettts")

    def upload_un_fichier(self):
        self.page.locator("input[type='file']").set_input_files(r"C:\Users\Administrateur\Downloads\invoice (31).txt")
        self.btn_submit.click()

    def verifier_la_presence_du_message_succes(self):
        expect(self.sucess_message).to_be_visible()

    def cliquer_sur_home(self):
        self.btn_home.click()