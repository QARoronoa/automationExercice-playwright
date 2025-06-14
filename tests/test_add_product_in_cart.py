from pageObjects.HomePage import HomePage
from pageObjects.CartPage import CartPage
from pageObjects.ProductPage import ProductPage



def test_add_product_in_cart(lancerNavigateur):
    home_page = HomePage(lancerNavigateur)
    product_page = ProductPage(lancerNavigateur)
    cart_page = CartPage(lancerNavigateur)

    # Accueil
    home_page.verifier_titre_home_page()

    #Click 'Products' button
    home_page.cliquer_sur_boutton_product()

    #Hover over first product and click 'Add to cart'
    product_page.cliquer_sur_premier_add_to_cart()

    #Click 'Continue Shopping' button
    product_page.cliquer_sur_Continue_Shopping()

    #Hover over second product and click 'Add to cart'
    product_page.cliquer_sur_second_add_to_cart()

    #Click 'View Cart' button
    product_page.cliquer_sur_view_cart()

    #Verify both products are added to Cart
    cart_page.verifier_que_les_articles_sont_presents()

