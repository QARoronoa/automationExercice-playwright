from pageObjects.HomePage import HomePage


def test_verify_test_cases_pages(lancerNavigateur):
    # Accueil
    home_page = HomePage(lancerNavigateur)
    home_page.verifier_titre_home_page()

    #Click on 'Test Cases' button & verify user is navigated to test cases page successfully
    home_page.cliquer_surr_test_cases()