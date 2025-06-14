from pageObjects.HomePage import HomePage
from pageObjects.CartPage import CartPage
from pageObjects.ProductPage import ProductPage



def test_remove_products_from_cart(lancerNavigateur):
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

    #Click 'Cart' button
    home_page.cliquer_sur_boutton_cart()

    # Verify that cart page is displayed
    cart_page.verifier_que_l_article_Blue_Top_present("Blue Top")

    #Click 'X' button corresponding to particular product
    cart_page.supprimer_article_panier()

    #Verify that product is removed from the cart
    cart_page.verifier_que_le_panier_est_vide()




