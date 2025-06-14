from pageObjects.HomePage import HomePage
from pageObjects.ProductPage import ProductPage


def test_verify_all_products_and_product_detail_page(lancerNavigateur):
    home_page = HomePage(lancerNavigateur)
    product_page = ProductPage(lancerNavigateur)

    # Accueil
    home_page.verifier_titre_home_page()

    #Click on 'Products' button
    home_page.cliquer_sur_boutton_product()
    product_page.verifier_que_All_PRODUCTS_is_visible()

    # Verify user is navigated to ALL PRODUCTS page successfully
    product_page.verifier_que_les_produits_sont_visibles()

    #Click on 'View Product' of first product
    product_page.cliquer_sur_view_product()