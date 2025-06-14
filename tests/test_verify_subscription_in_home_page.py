import pytest
from data.data_login import Login
from pageObjects.HomePage import HomePage
from pageObjects.ProductPage import ProductPage

@pytest.fixture(params=Login.new_user_signup)
def subscription(request):
    return request.param

def test_verify_subscription_in_home_page(lancerNavigateur, subscription):
    home_page = HomePage(lancerNavigateur)

    # Accueil
    home_page.verifier_titre_home_page()

    #Scroll down to footer
    home_page.scroller_vers_subscription()

    # Enter email address in input and click arrow button
    home_page.inserer_un_mail_dans_subscription_et_envoyer(subscription["email"])

    #Verify success message 'You have been successfully subscribed!' is visible
    home_page.capturer_message_alert()


