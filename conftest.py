try:
    import pytest  # type: ignore[import]
except ImportError:
    pytest = None
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def base_url_api():
    return "https://petstore.swagger.io/v2"

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()