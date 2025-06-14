import time

from pageObjects.HomePage import HomePage
from pageObjects.CartPage import CartPage
from pageObjects.ProductPage import ProductPage



def test_View_Category_Products(lancerNavigateur):
    home_page = HomePage(lancerNavigateur)
    product_page = ProductPage(lancerNavigateur)
    cart_page = CartPage(lancerNavigateur)

    # Accueil
    home_page.verifier_titre_home_page()

    #Click on 'Products' button
    home_page.cliquer_sur_boutton_product()

    #Verify that Brands are visible on left side bar
    product_page.verifier_les_marques_sont_visibles()

    #Click on any brand name
    product_page.cliquer_sur_une_marque("Allen Solly Junior")
    product_page.verifier_title_brands_page("Brand - Allen Solly Junior Products")

    #On left side bar, click on any other brand link
    product_page.cliquer_sur_une_marque("Biba")
    product_page.verifier_title_brands_page("Brand - Biba Products")





