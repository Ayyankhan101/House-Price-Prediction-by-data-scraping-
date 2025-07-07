import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup

base_url = "https://www.zameen.com/Houses_Property/Pakistan-1521-{}.html"
start_page = 1
max_pages = 3  # Set a limit for testing purposes. You can increase this later.

# Set up Firefox options
firefox_options = Options()
firefox_options.add_argument(
    "--headless"
)  # Run Firefox in headless mode (without a UI)
firefox_options.add_argument(
    "--disable-dev-shm-usage"
)  # Overcome limited resource problems

# Set up Firefox WebDriver
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=firefox_options)

# Set page load timeout
driver.set_page_load_timeout(30)  # Increased timeout to 30 seconds

all_properties_data = []
current_page = start_page

try:
    while current_page <= max_pages:
        url = base_url.format(current_page)
        print(f"Navigating to: {url}")
        try:
            driver.get(url)
            # Give the page more time to load dynamic content after initial load
            time.sleep(5)  # Adjust this value if needed
        except TimeoutException:
            print(f"Timeout while loading page {url}. Skipping this page.")
            current_page += 1
            continue

        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")

        # Find all property listings (main container is now b22b6883)
        property_listings = soup.find_all("div", class_="b22b6883")

        if not property_listings:
            print(
                f"No property listings found with class b22b6883 on page "
                f"{current_page}. Exiting."
            )
            break

        print(
            f"Found {len(property_listings)} property listings on page "
            f"{current_page}."
        )
        for i, listing in enumerate(property_listings):
            property_data = {
                "Price": "N/A",
                "Location": "N/A",
                "Beds": "N/A",
                "Baths": "N/A",
                "Area": "N/A",
            }

            # Extract Price (now directly within the listing div)
            price_tag = listing.find(
                "span", class_="dc381b54", attrs={"aria-label": "Price"}
            )
            if price_tag:
                property_data["Price"] = price_tag.get_text(strip=True)
            else:
                print(f"  Listing {i+1}: Price tag not found.")

            # Find the container for location, beds, baths, area (_52d0f124)
            location_beds_baths_area_container = listing.find("div", class_="_52d0f124")

            if location_beds_baths_area_container:
                # Extract Location
                location_tag = location_beds_baths_area_container.find(
                    "div", class_="db1aca2f", attrs={"aria-label": "Location"}
                )
                if location_tag:
                    property_data["Location"] = location_tag.get_text(strip=True)
                else:
                    print(f"  Listing {i+1}: Location tag not found.")

                # Extract Beds
                beds_tag = location_beds_baths_area_container.find(
                    "span", class_="_6d9b9b83", attrs={"aria-label": "Beds"}
                )
                if beds_tag:
                    property_data["Beds"] = beds_tag.get_text(strip=True)
                else:
                    print(f"  Listing {i+1}: Beds tag not found.")

                # Extract Baths
                baths_tag = location_beds_baths_area_container.find(
                    "span", class_="_6d9b9b83", attrs={"aria-label": "Baths"}
                )
                if baths_tag:
                    property_data["Baths"] = baths_tag.get_text(strip=True)
                else:
                    print(f"  Listing {i+1}: Baths tag not found.")

                # Extract Area - This is nested deeper, so we need to get the text of the innermost span
                area_span_with_aria_label = location_beds_baths_area_container.find(
                    "span",
                    class_="_6d9b9b83",
                    attrs={"aria-label": "Area"},
                )
                if area_span_with_aria_label:
                    # The actual area text is inside a <span> within a <div> within the aria-label span
                    inner_area_span = area_span_with_aria_label.find("span")
                    if inner_area_span:
                        property_data["Area"] = inner_area_span.get_text(strip=True)
                    else:
                        property_data["Area"] = area_span_with_aria_label.get_text(
                            strip=True
                        )  # Fallback
                else:
                    print(f"  Listing {i+1}: Area tag not found.")
            else:
                print(
                    f"  Listing {i+1}: Location/Beds/Baths/Area container (_52d0f124) not found."
                )

            all_properties_data.append(property_data)

        # Check for the next page button using Selenium's find_element
        try:
            # The 'Next' button has class '_95dd93c1' and title 'Next'
            next_button = driver.find_element(
                By.CSS_SELECTOR, 'a._95dd93c1[title="Next"]'
            )
            # If found, increment page number to continue loop
            current_page += 1
            time.sleep(2)  # Small delay before navigating to the next page
        except NoSuchElementException:
            print("No 'Next' button found. End of pagination.")
            break  # Exit loop if no next button

finally:
    driver.quit()  # Ensure the browser is closed

# Create a pandas DataFrame and save to CSV
if all_properties_data:
    df = pd.DataFrame(all_properties_data)
    csv_path = "/home/ayyan/the-current news  website project/zameen_properties.csv"
    df.to_csv(csv_path, index=False)
    print(
        f"\nSuccessfully scraped {len(all_properties_data)} properties and saved to {csv_path}"
    )
else:
    print("No data scraped.")
