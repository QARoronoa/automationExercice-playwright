import pytest
from data.data_login import Login
from pageObjects.CartPage import CartPage
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.ProductPage import ProductPage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.PaymentPage import PaymentPage
from tests.test_add_product_in_cart import test_add_product_in_cart


@pytest.fixture(params=Login.new_user_signup)
def senregistrer(request):
    return request.param

@pytest.fixture(params=Login.account_information)
def formulaire_information(request):
    return request.param

def test_download_invoice_after_purcharse_order(lancerNavigateur, senregistrer, formulaire_information, formulaire_de_payment):
    home_page = HomePage(lancerNavigateur)
    product_page = ProductPage(lancerNavigateur)
    cart_page = CartPage(lancerNavigateur)
    login_page = LoginPage(lancerNavigateur)
    checkout_page = CheckoutPage(lancerNavigateur)
    payment_page = PaymentPage(lancerNavigateur)

    #Accueil
    home_page.verifier_titre_home_page()

    #Add products to cart
    test_add_product_in_cart(lancerNavigateur)

    #Click Proceed To Checkout
    cart_page.cliquer_sur_proceed_to_checkout()

    #Click 'Register / Login' button
    cart_page.cliquer_sur_register_login_popin_checkout()

    # Fill all details in Signup and create account
    login_page.enter_credentials_new_user(senregistrer["name"], senregistrer["email"])
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
    login_page.cliquer_sur_le_bouton_create_account()

    #Verify ' Logged in as username' at top
    home_page.verifier_user_est_connecté()

    #Click 'Cart' button
    home_page.cliquer_sur_boutton_cart()

    #Click 'Proceed To Checkout' button
    cart_page.cliquer_sur_proceed_to_checkout()

    #Enter description in comment text area and click 'Place Order'
    checkout_page.write_a_comment_in_aera_text()
    checkout_page.click_on_place_order_button()

    #Enter payment details: Name on Card, Card Number, CVC, Expiration date
    payment_page.saisir_les_informations_de_la_CB(**formulaire_de_payment)

    #Click 'Pay and Confirm Order' button
    payment_page.cliquer_sur_continue()

    #Click 'Delete Account' button
    home_page.cliquer_sur_delete_accont()



