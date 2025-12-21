from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://ozh.github.io/cookieclicker/")
time.sleep(5) # Wait for the page to load

langEn = driver.find_element(By.ID, "langSelect-EN")
langEn.click() # Select English
time.sleep(3)
cookie = driver.find_element(By.ID, "bigCookie")

try:
    cycle = 0
    while True:  # Keep going forever
        cycle += 1
        
        # Click the cookie 100+ times per cycle
        for _ in range(100+cycle*20):
            cookie.click()
            time.sleep(0.05)
        
        # Try to buy upgrades
        upgrades = driver.find_elements(By.CLASS_NAME, "upgrade")
        for upgrade in reversed(upgrades):
            try:
                upgrade.click()
            except:
                pass

        # Try to buy buildings
        buildings = driver.find_elements(By.CLASS_NAME, "product")
        for building in reversed(buildings):
            try:
                building.click()
            except:
                pass

        print(f"Cycle {cycle} complete. Your cookies are accumulating rapidly.")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nBot stopped. Check your cookie count - it's probably ridiculous now.")
finally:
    input("Press Enter to quit... ")
    print("Quitting...")
    driver.quit()
