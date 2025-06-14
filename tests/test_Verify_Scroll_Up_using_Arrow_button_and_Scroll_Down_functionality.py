import time

import pytest
from pageObjects.HomePage import HomePage

@pytest.mark.skip
def test_Verify_Scroll_Up_using_Arrow_button_and_Scroll_Down_functionality(lancerNavigateur):
    home_page = HomePage(lancerNavigateur)


    # Accueil
    home_page.verifier_titre_home_page()

    #Scroll down page to bottom and  Verify 'SUBSCRIPTION' is visible
    home_page.scroller_vers_subscription()

    #Click on arrow at bottom right side to move upward
    home_page.click_on_scrollUp_button()

    #Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen

    time.sleep(3)