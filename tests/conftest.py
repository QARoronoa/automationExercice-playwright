import os

import pytest
from playwright.sync_api import Playwright
from data.data_payment import payment

@pytest.fixture(scope="function")
def lancerNavigateur(playwright, request):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto("http://www.automationexercise.com/")
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button", name= "Autoriser").click()
    yield page

    trace_dir = "traces"
    os.makedirs(trace_dir, exist_ok=True)
    trace_path = os.path.join(trace_dir, f"trace_{request.node.name}.zip")
    context.tracing.stop(path=trace_path)

    context.close()
    browser.close()

@pytest.fixture(scope="function")
def formulaire_de_payment():
    return payment.payment_information()