import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def chrome_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = 1920
    browser.config.window_width = 1080

    yield

    browser.quit()
