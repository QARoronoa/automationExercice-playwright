from pageObjects.HomePage import HomePage
from pageObjects.ProductPage import ProductPage


def test_search_product(lancerNavigateur):
    home_page = HomePage(lancerNavigateur)
    product_page = ProductPage(lancerNavigateur)

    # Accueil
    home_page.verifier_titre_home_page()

    #Click on 'Products' button
    home_page.cliquer_sur_boutton_product()
    product_page.verifier_que_All_PRODUCTS_is_visible()

    #Enter product name in search input and click search button
    product_page.rechercher_un_article()

    #Verify 'SEARCHED PRODUCTS' et larticle recherche is visible
    product_page.veririfer_que_larticle_rechercher_est_visible()



