import time

from pageObjects.CartPage import CartPage
from pageObjects.HomePage import HomePage
from pageObjects.ProductPage import ProductPage


def test_add_cart_from_recommended_items(lancerNavigateur):
    home_page = HomePage(lancerNavigateur)
    product_page = ProductPage(lancerNavigateur)
    cart_page = CartPage(lancerNavigateur)

    # Accueil
    home_page.verifier_titre_home_page()

    # Scroll to bottom of page
    home_page.scroller_vers_recommended_items()

    # Click on 'Add To Cart' on Recommended product
    home_page.add_a_recommended_items_in_cart()

    #click on view cart button
    product_page.cliquer_sur_view_cart()

    #verify item is displayed in cart
    cart_page.verifier_que_l_article_Blue_Top_present("Stylish Dress")
