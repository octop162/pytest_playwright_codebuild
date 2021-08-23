# test_my_application.py
from playwright.sync_api import Page

def test_wikipedia_title(page: Page):
    page.goto("https://wikipedia.org")
    page.screenshot(path="screenshots/test.png")
    assert "Wikipedia" in page.title()