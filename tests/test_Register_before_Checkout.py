import pytest
from data.data_login import Login
from pageObjects.CartPage import CartPage
from pageObjects.HomePage import HomePage
from pageObjects.ProductPage import ProductPage
from pageObjects.LoginPage import LoginPage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.PaymentPage import PaymentPage
from tests.test_add_product_in_cart import test_add_product_in_cart



@pytest.fixture(params= Login.new_user_signup)
def senregistrer(request):
    return request.param

@pytest.fixture(params=Login.account_information)
def formulaire_information(request):
    return request.param

def test_Place_order_Register_while_Checkout(lancerNavigateur, senregistrer, formulaire_information, formulaire_de_payment):
    home_page = HomePage(lancerNavigateur)
    product_page = ProductPage(lancerNavigateur)
    cart_page = CartPage(lancerNavigateur)
    login_page = LoginPage(lancerNavigateur)
    checkout_page = CheckoutPage(lancerNavigateur)
    payment_page = PaymentPage(lancerNavigateur)

    # Accueil
    home_page.verifier_titre_home_page()

    # Click 'Register / Login' button
    home_page.cliquer_sur_signupLogin()
    login_page.enter_credentials_new_user(senregistrer["name"], senregistrer["email"])

    # Fill all details in Signup and create account
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

    # Verify ' Logged in as username' at top
    home_page.verifier_user_est_connecté()

    #Add products to cart
    test_add_product_in_cart(lancerNavigateur)

    #Click Proceed To Checkout
    cart_page.cliquer_sur_proceed_to_checkout()

    #Click 'Cart' button
    home_page.cliquer_sur_boutton_cart()

    #Click 'Proceed To Checkout' button
    cart_page.cliquer_sur_proceed_to_checkout()

    #Verify Address Details and Review Your Order
    checkout_page.comparer_les_adresses()

    # Enter description in comment text area and click 'Place Order'
    checkout_page.cliquer_sur_checkout()

    #Enter payment details: Name on Card, Card Number, CVC, Expiration date
    payment_page.saisir_les_informations_de_la_CB(**formulaire_de_payment)

    #Click 'Pay and Confirm Order' button #Verify success message 'Your order has been placed successfully!'
    payment_page.cliquer_sur_continue()

    #Click 'Delete Account' button and Verify 'ACCOUNT DELETED!' and click 'Continue' button
    home_page.cliquer_sur_delete_accont()

