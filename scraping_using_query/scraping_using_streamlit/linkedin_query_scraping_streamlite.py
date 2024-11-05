import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import pandas as pd

# Define the ChromeDriver path
driver_path = "C:/Users/shari/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe"

# Initialize Chrome driver with the Service class
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Open LinkedIn and Login
def login_to_linkedin():
    driver.get("https://www.linkedin.com/login")
    
    # Wait until the login fields appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    
    # Enter your LinkedIn credentials here
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    
    # Replace these with your LinkedIn login credentials
    username.send_keys("...........@gmail.com")  # Replace with your email
    password.send_keys("*********************")            # Replace with your password
    
    # Submit login form
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Wait for the page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "search-global-typeahead__input"))
    )

# Function to scrape LinkedIn profiles based on a search query
def scrape_linkedin_profiles(query):
    # Go to LinkedIn search page with the query
    search_url = f"https://www.linkedin.com/search/results/people/?keywords={query}"
    driver.get(search_url)
    
    # Scroll down the page to load more profiles
    for _ in range(2):  # Adjust range for more scrolling if needed
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
    
    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    profiles = soup.select('ul.reusable-search__entity-result-list li.reusable-search__result-container')

    data = []
    for profile in profiles:
        try:
            # Extract profile name
            name_tag = profile.select_one('span.entity-result__title-text')
            name = name_tag.get_text(strip=True) if name_tag else "N/A"
            
            # Extract job title
            job_title_tag = profile.select_one('div.entity-result__primary-subtitle')
            job_title = job_title_tag.get_text(strip=True) if job_title_tag else "N/A"
            
            # Extract location
            location_tag = profile.select_one('div.entity-result__secondary-subtitle')
            location = location_tag.get_text(strip=True) if location_tag else "N/A"
            
            # Extract LinkedIn profile URL
            linkedin_url_tag = profile.select_one('a.app-aware-link')
            linkedin_url = linkedin_url_tag['href'] if linkedin_url_tag else "N/A"
            
            data.append({
                'Name': name,
                'Job Title': job_title,
                'Location': location,
                'LinkedIn URL': linkedin_url
            })
        except AttributeError:
            continue  # Skip if any field is missing
    
    return data

# Streamlit app
def main():
    st.title("LinkedIn Profile Scraper")
    st.write("Enter a query to search LinkedIn profiles and view the results in a downloadable CSV file.")
    
    # Input for search query
    query = st.text_input("Enter LinkedIn search query", "")
    
    if st.button("Search LinkedIn"):
        if query:
            # Login and scrape data
            login_to_linkedin()
            profile_data = scrape_linkedin_profiles(query)
            
            # Save data to a DataFrame
            df = pd.DataFrame(profile_data)
            
            # Display the DataFrame
            st.write("Scraped Data:")
            st.dataframe(df)
            
            # Create a downloadable CSV
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name="linkedin_profiles.csv",
                mime="text/csv"
            )
            
            st.success("Scraping complete. You can download the CSV file above.")
        else:
            st.warning("Please enter a query to search.")

if __name__ == "__main__":
    main()
    driver.quit()  # Close the browser once done
