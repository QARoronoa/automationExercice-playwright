import time
import pytest
from data.data_login import Login
from pageObjects.HomePage import HomePage
from  pageObjects.LoginPage import LoginPage

@pytest.fixture(params= Login.register_existing_mail)
def senregistrer(request):
    return request.param

def test_register_with_existing_email(lancerNavigateur, senregistrer):
    #Accueil
    home_page = HomePage(lancerNavigateur)
    login_page = LoginPage(lancerNavigateur)
    home_page.verifier_titre_home_page()

    #Aller à la page d'inscription/login
    home_page.cliquer_sur_signupLogin()
    login_page.verifier_titre_page_login()

    #Saisie de nom + email pour créer un compte
    login_page.enter_credentials_new_user(senregistrer["name"], senregistrer["email"])

    #Verify error 'Email Address already exist!' is visible
    login_page.verifier_presence_message_erreur_email()