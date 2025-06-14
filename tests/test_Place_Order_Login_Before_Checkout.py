import pytest
from data.data_login import Login
from pageObjects.CartPage import CartPage
from pageObjects.HomePage import HomePage
from pageObjects.ProductPage import ProductPage
from pageObjects.LoginPage import LoginPage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.PaymentPage import PaymentPage
from tests.test_add_product_in_cart import test_add_product_in_cart

@pytest.fixture(params=Login.user_correct_credentials)
def se_connecter(request):
    return request.param

def test_Place_Order_Login_Before_Checkout(lancerNavigateur,se_connecter, formulaire_de_payment):
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

    # Fill email, password and click 'Login' button
    login_page.saisir_email_et_password(se_connecter["email"], se_connecter["password"])

    #Verify 'Logged in as username' at top
    home_page.verifier_user_est_connecté()

    # Add products to cart
    test_add_product_in_cart(lancerNavigateur)

    #Click Proceed To Checkout
    cart_page.cliquer_sur_proceed_to_checkout()

    #Verify Address Details and Review Your Order
    # checkout_page.comparer_les_adresses()
    checkout_page.cliquer_sur_checkout()

    # Enter payment details: Name on Card, Card Number, CVC, Expiration date
    payment_page.saisir_les_informations_de_la_CB(**formulaire_de_payment)

    # Click 'Pay and Confirm Order' button #Verify success message 'Your order has been placed successfully!'
    payment_page.cliquer_sur_continue()
