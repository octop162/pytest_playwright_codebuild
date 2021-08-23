# test_my_application.py
from playwright.sync_api import Page

def test_wikipedia_title(page: Page):
    page.goto("https://wikipedia.org")
    page.screenshot(path="screenshots/wikipedia.png")
    assert "Wikipedia" in page.title()

def test_google_title(page: Page):
    page.goto("https://google.com")
    page.screenshot(path="screenshots/google.png")
    assert "Wikipedia" in page.title()