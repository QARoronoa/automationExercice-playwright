import time

import pytest
from data.data_login import Login
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage


@pytest.fixture(params=Login.user_correct_credentials)
def se_connecter(request):
    return request.param


def test_login_with_correct_credentials(lancerNavigateur, se_connecter):
    # Accueil
    home_page = HomePage(lancerNavigateur)
    login_page = LoginPage(lancerNavigateur)
    home_page.verifier_titre_home_page()

    # Aller à la page d'inscription/login
    home_page.cliquer_sur_signupLogin()
    login_page.verifier_titre_page_login()

    # se connecter
    login_page.saisir_email_et_password(se_connecter["email"], se_connecter["password"])
    home_page.verifier_user_est_connecté()

