import time

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.ProductPage import ProductPage
from tests.test_search_product import test_search_product
from pageObjects.CartPage import CartPage
from pageObjects.LoginPage import LoginPage
from data.data_login import Login

@pytest.fixture(params=Login.user_correct_credentials)
def se_connecter(request):
    return request.param

def test_search_products_andverify_cart_after_login(lancerNavigateur, se_connecter):
    home_page = HomePage(lancerNavigateur)
    product_page = ProductPage(lancerNavigateur)
    cart_page = CartPage(lancerNavigateur)
    login_page = LoginPage(lancerNavigateur)


    #Enter product name in search input and click search button
    test_search_product(lancerNavigateur)

    # Add those products to cart
    product_page.cliquer_sur_premier_add_to_cart()
    product_page.cliquer_sur_Continue_Shopping()

    #Click 'Cart' button and verify that products are visible in cart
    home_page.cliquer_sur_boutton_cart()
    cart_page.verifier_que_l_article_Blue_Top_present("Blue Top")

    #Click 'Signup / Login' button and submit login details
    home_page.cliquer_sur_signupLogin()
    login_page.saisir_email_et_password(se_connecter["email"], se_connecter["password"])

    # Again, go to Cart page
    home_page.cliquer_sur_boutton_cart()
    cart_page.verifier_que_l_article_Blue_Top_present("Blue Top")
