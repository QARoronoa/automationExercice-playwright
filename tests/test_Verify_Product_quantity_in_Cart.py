from pageObjects.HomePage import HomePage
from pageObjects.CartPage import CartPage
from pageObjects.ProductPage import ProductPage
from pageObjects.ProductDetailPage import ProductDetailPage



def test_Verify_Product_quantity_in_Cart(lancerNavigateur):
    home_page = HomePage(lancerNavigateur)
    product_page = ProductPage(lancerNavigateur)
    cart_page = CartPage(lancerNavigateur)
    productDetail_page = ProductDetailPage(lancerNavigateur)

    # Accueil
    home_page.verifier_titre_home_page()

    #Click 'View Product' for any product on home page
    product_page.cliquer_sur_view_product()

    #Increase quantity to 4
    productDetail_page.augmenter_la_quantite_a_4()

    #Click 'Add to cart' button et sur view cart
    productDetail_page.cliquer_sur_add_to_cart()
    product_page.cliquer_sur_view_cart()

    #Verify that product is displayed in cart page with exact quantity
    cart_page.verifier_que_l_article_Blue_Top_present("Blue Top")
    cart_page.verifier_la_quantity()