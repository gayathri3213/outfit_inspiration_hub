
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Fixture for setting up and tearing down the driver
@pytest.fixture
def setup_teardown():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


# Test 1: Verify that the entered name matches the greeting
def test_user_greeting(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")

    driver.find_element(By.NAME, "name").send_keys("Gayathri")
    driver.find_element(By.NAME, "name").submit()

    time.sleep(2)

    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert "Gayathri" in body_text, f"Greeting not found or incorrect: {body_text}"


# Test 2: Click Formal Wear and verify the page body text
def test_formal_wear(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")

    driver.find_element(By.NAME, "name").send_keys("Gayathri")
    driver.find_element(By.NAME, "name").submit()

    time.sleep(1)

    driver.find_element(
        By.XPATH, "//a[contains(@href, '/occasion/formal')]"
    ).click()

    time.sleep(1)

    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert "Formal Wear" in body_text, f"Formal Wear page text not found: {body_text}"


# Test 3: Click College Casual and verify the page body text
def test_college_casual(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")

    driver.find_element(By.NAME, "name").send_keys("Gayathri")
    driver.find_element(By.NAME, "name").submit()

    time.sleep(1)

    driver.find_element(
        By.XPATH, "//a[contains(@href, '/occasion/college-casual')]"
    ).click()

    time.sleep(1)

    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert "College Casual" in body_text, f"College Casual page text not found: {body_text}"


# Test 4: Click Party Wear and verify the page body text
def test_party_wear(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")

    driver.find_element(By.NAME, "name").send_keys("Gayathri")
    driver.find_element(By.NAME, "name").submit()

    time.sleep(1)

    driver.find_element(
        By.XPATH, "//a[contains(@href, '/occasion/party')]"
    ).click()

    time.sleep(1)

    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert "Party Wear" in body_text, f"Party Wear page text not found: {body_text}"
