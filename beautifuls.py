from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def scrape_hotels():
    # Setup Selenium driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.skinnytaste.com')

    hotels = []
    

    # Select hotel elements
    food_elements = driver.find_elements(By.CLASS_NAME, 'post-grid-post')
    print(len(food_elements))
    print(food_elements[0].text)
    for hotel in food_elements:
        name = hotel.find_element(By.CLASS_NAME, 'post-grid-post-title').text
        print(name)
        # try:
        #     rating = hotel.find_element(By.CLASS_NAME, 'ReviewScore').text
        # except:
        #     rating = 'N/A'
        # price = hotel.find_element(By.CLASS_NAME, 'PropertyCardPrice').text

        # hotels.append({
        #     'name': name,
        #     'rating': rating,
        #     'price': price
        # })

    driver.quit()

    return hotels

hotels = scrape_hotels()
# for hotel in hotels:
    # print(hotel)
