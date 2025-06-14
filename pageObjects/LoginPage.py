from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page:Page):
        self.page = page

    #locators
        self.nameNewUserSignup = page.get_by_placeholder("Name")
        self.emailNewUserSignup = page.get_by_placeholder("Email Address").nth(1)
        self.signup_button = page.get_by_role("button", name="Signup")
        self.gender = page.locator("#id_gender1")
        self.champ_pwd = page.locator("#password")
        self.day_birth = page.locator("#days")
        self.month_birth = page.locator("#months")
        self.year_birth = page.locator("#years")
        self.newsletter = page.locator("#newsletter")
        self.special_offers = page.locator("#optin")
        self.first_name = page.locator("#first_name")
        self.last_name = page.locator("#last_name")
        self.adress = page.locator("#address1")
        self.country = page.locator("#country")
        self.state = page.locator("#state")
        self.city = page.locator("#city")
        self.zipcode = page.locator("#zipcode")
        self.mobile_number = page.locator("#mobile_number")
        self.btn_create_aacount = page.get_by_role("button", name="Create Account")
        self.login_email = page.locator("input[data-qa='login-email']")
        self.login_password = page.get_by_placeholder("Password")
        self.btn_login = page.get_by_role("button", name="Login")



    #methodes
    def verifier_titre_page_login(self):
        expect(self.page).to_have_title("Automation Exercise - Signup / Login")

    def enter_credentials_new_user(self,name, email):
        self.nameNewUserSignup.fill(name)
        self.emailNewUserSignup.fill(email)
        self.signup_button.click()

    def remplir_formulaire_info(self, pwd,day, month, year, firstname, lastname, adress, state, city, cp, mobilenumber ):
        self.gender.click()
        self.champ_pwd.fill(pwd)
        self.day_birth.select_option(day)
        self.month_birth.select_option(month)
        self.year_birth.select_option(year)
        self.newsletter.check()
        self.special_offers.check()
        self.first_name.fill(firstname)
        self.last_name.fill(lastname)
        self.adress.fill(adress)
        self.country.select_option("United States")
        self.state.fill(state)
        self.city.fill(city)
        self.zipcode.fill(cp)
        self.mobile_number.fill(mobilenumber)

    def cliquer_sur_le_bouton_create_account(self):
        expect(self.btn_create_aacount).to_be_enabled()
        self.btn_create_aacount.click()
        expect(self.page.locator(".title")).to_have_text("Account Created!")
        self.page.locator(".btn-primary").click()

    def saisir_email_et_password(self, email, password):
        self.login_email.fill(email)
        self.login_password.fill(password)
        self.btn_login.click()

    def verifier_message_error(self):
        expect(self.page.locator("text=Your email or password is incorrect!")).to_be_visible()

    def verifier_presence_message_erreur_email(self):
        expect(self.page.locator("text=Email Address already exist!")).to_be_visible()



