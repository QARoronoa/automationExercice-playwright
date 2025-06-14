import time

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.Contact_usPage import ContactUsPage


def test_contact_us_form(lancerNavigateur):
    # Accueil
    home_page = HomePage(lancerNavigateur)
    contactUs_page = ContactUsPage(lancerNavigateur)
    home_page.verifier_titre_home_page()

    #cliquer sur contact us
    home_page.cliquer_sur_contact_us()

    #Verify 'GET IN TOUCH' is visible
    contactUs_page.verifier_que_get_in_touch_est_visible()

    #Enter name, email, subject and message
    contactUs_page.remplir_formulaire_contact()

    #Upload file et cliquer sur submit
    contactUs_page.upload_un_fichier()

    #Verify success message 'Success! Your details have been submitted successfully.' is visible
    contactUs_page.verifier_la_presence_du_message_succes()

    #Click 'Home' button and verify that landed to home page successfully
    contactUs_page.cliquer_sur_home()
    # home_page.verifier_titre_home_page()


