from playwright.sync_api import Page, expect


class ProductPage:
    def __init__(self, page: Page):
        self.page = page

        #locators
        self.btn_view_product = page.get_by_role("link", name="View Product")
        self.search_barre = page.locator("#search_product")
        self.btn_search = page.locator("#submit_search")
        self.btn_add_to_cart = page.locator(".add-to-cart")
        self.btn_Continue_Shopping = page.get_by_role("button", name="Continue Shopping")
        self.btn_View_Cart = page.get_by_role("link", name="View Cart")
        self.btn_categorie_men = page.locator("a[href='#Men']")
        self.btn_sous_categorie_jeans = page.locator('a[href="/category_products/6"]')
        self.marques = page.locator(".brands-name")
        self.title_brand = page.locator(".title.text-center")


        #methodes

    def verifier_que_All_PRODUCTS_is_visible(self):
        expect(self.page.locator(".title")).to_be_visible()

    def verifier_que_les_produits_sont_visibles(self):
       expect(self.page.locator(".product-image-wrapper")).to_have_count(34)

    def cliquer_sur_view_product(self):
        self.btn_view_product.first.click()
        expect(self.page).to_have_title("Automation Exercise - Product Details")

    def rechercher_un_article(self):
        self.search_barre.fill("Blue Top")
        self.btn_search.click()

    def veririfer_que_larticle_rechercher_est_visible(self):
        expect(self.page.locator(".title")).to_be_visible()
        expect(self.page.locator(".single-products")).to_contain_text("Blue Top")

    def cliquer_sur_premier_add_to_cart(self):
        self.btn_add_to_cart.first.click()

    def cliquer_sur_second_add_to_cart(self):
        self.page.locator("a[data-product-id*='2']").first.click()

    def cliquer_sur_Continue_Shopping(self):
        self.btn_Continue_Shopping.click()

    def cliquer_sur_view_cart(self):
        self.btn_View_Cart.click()

    def verifier_que_tops_products_est_visible(self, titre):
        expect(self.page.locator(".features_items")).to_contain_text(titre)

    def cliquer_sur_une_sous_categories_homme(self):
        self.btn_categorie_men.click()
        self.btn_sous_categorie_jeans.click()

    def verifier_les_marques_sont_visibles(self):
        self.marques.all_inner_texts()

    def cliquer_sur_une_marque(self,brand):
        self.page.locator(f'a[href*="/brand_products/{brand}"]').click()

    def verifier_title_brands_page(self,brands_title):
        expect(self.title_brand).to_have_text(brands_title)
