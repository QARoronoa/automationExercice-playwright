from pageObjects.HomePage import HomePage
from pageObjects.CartPage import CartPage
from pageObjects.ProductPage import ProductPage
from pageObjects.ProductDetailPage import ProductDetailPage

def test_add_review_on_product(lancerNavigateur):
    home_page = HomePage(lancerNavigateur)
    product_page = ProductPage(lancerNavigateur)
    cart_page = CartPage(lancerNavigateur)
    productDetail_page = ProductDetailPage(lancerNavigateur)

    # Accueil
    home_page.verifier_titre_home_page()

    # Click on 'Products' button
    home_page.cliquer_sur_boutton_product()

    #Verify user is navigated to ALL PRODUCTS page successfully
    product_page.verifier_que_All_PRODUCTS_is_visible()

    #Click on 'View Product' button
    product_page.cliquer_sur_view_product()

    #Verify 'Write Your Review' is visible
    productDetail_page.verify_write_your_review_is_visible()

    #Enter name, email and review
    productDetail_page.fill_review_form()

    # Click 'Submit' button
    productDetail_page.click_on_submit_button()

    #Verify success message 'Thank you for your review.'
    productDetail_page.verify_review_success_message_is_vsible()