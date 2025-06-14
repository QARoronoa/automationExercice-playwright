import time
import pytest
from data.data_login import Login
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage


@pytest.fixture(params=Login.new_user_signup)
def senregistrer(request):
    return request.param


@pytest.fixture(params=Login.account_information)
def formulaire_information(request):
    return request.param


def test_register_user(lancerNavigateur, senregistrer, formulaire_information):
    # Accueil
    home_page = HomePage(lancerNavigateur)
    login_page = LoginPage(lancerNavigateur)
    home_page.verifier_titre_home_page()

    # Aller à la page d'inscription/login
    home_page.cliquer_sur_signupLogin()
    login_page.verifier_titre_page_login()

    # Saisie de nom + email pour créer un compte
    login_page.enter_credentials_new_user(senregistrer["name"], senregistrer["email"])

    # Remplir les infos personnelles du formulaire
    login_page.remplir_formulaire_info(
        formulaire_information["password"],
        formulaire_information["dayBirth"],
        formulaire_information["monthBirth"],
        formulaire_information["yearBirth"],
        formulaire_information["firstName"],
        formulaire_information["lastName"],
        formulaire_information["adress"],
        formulaire_information["state"],
        formulaire_information["city"],
        formulaire_information["zipCode"],
        formulaire_information["mobileNumer"])

    # Soumettre le formulaire
    login_page.cliquer_sur_le_bouton_create_account()

    # verifier user est connecté
    home_page.verifier_user_est_connecté()

    # supprimé le compte
    home_page.cliquer_sur_delete_accont()
