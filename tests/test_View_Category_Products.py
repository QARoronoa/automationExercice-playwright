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

    #Click on 'Women' category
    home_page.cliquer_sur_la_categorie_women()

    #Click on any category link under 'Women' category, for example: Dress
    home_page.cliquer_sur_sous_categorie()

    # Verify that category page is displayed and confirm text 'WOMEN - TOPS PRODUCTS'
    product_page.verifier_que_tops_products_est_visible("Women - Dress Products")

    #On left side bar, click on any sub-category link of 'Men' category
    product_page.cliquer_sur_une_sous_categories_homme()

    #Verify that user is navigated to that category page
    product_page.verifier_que_tops_products_est_visible("Men - Jeans Products")






