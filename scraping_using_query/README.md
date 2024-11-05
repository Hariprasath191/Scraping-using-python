# LinkedIn Profile Scraping Project

This project allows for LinkedIn profile scraping based on search queries, with two main parts:
1. **Basic LinkedIn Profile Scraping** using Selenium and BeautifulSoup, which saves data to a CSV file.
2. **LinkedIn Profile Scraping with User Interface** using Streamlit, where users can input a query and view the scraped profiles in a CSV format.

---

## Part 1: Basic LinkedIn Profile Scraping (`scraping_one`)

This part of the project focuses on scraping LinkedIn profiles based on a specified search query. The script uses Selenium to automate the login and search processes, BeautifulSoup to parse the page, and saves the data in a CSV file.

### Files and Folders
- **`linkedin_scraping_query.py`**: Python script that scrapes LinkedIn profiles based on a search query.
- **`linkedin_scrping_query.csv`**: CSV file where the scraped LinkedIn profile data is saved.
- **`README.md`**: Documentation for this section of the project.

### Prerequisites

- **Python 3.x**
- **Selenium** for browser automation
- **BeautifulSoup** for HTML parsing
- **ChromeDriver**: Ensure the path to ChromeDriver is correctly set in the script.

### Setup and Installation

1. Install the required libraries:
   ```bash
   pip install selenium beautifulsoup4 pandas
Download ChromeDriver and specify its path in the linkedin_scraping_query.py script:
driver_path = "path/to/chromedriver"
Usage
Open linkedin_scraping_query.py and update the following lines with your LinkedIn credentials:

username.send_keys("your_email")  # Replace with your LinkedIn email
password.send_keys("your_password")  # Replace with your LinkedIn password
Run the script:
```bash
Copy code

python linkedin_scraping_query.py
After running, the scraped data will be saved to linkedin_scrping_query.csv.

###Important Note
LinkedIn has strict policies against automated scraping. This script is for educational purposes only. Please respect LinkedIn's Terms of Service and avoid unauthorized data scraping.

Part 2: LinkedIn Profile Scraping with Streamlit (scraping_using_streamlit)
This part adds a user interface using Streamlit, enabling users to enter a search query and view the scraped profiles in a table format within the Streamlit app. This is useful for quick, interactive data retrieval based on user input.

Files and Folders
linkedin_query_scraping_streamlite.py: Streamlit app that takes a search query from the user and displays the scraped profiles in a table format.
linkedin_profiles.csv: CSV file where the scraped LinkedIn profile data is stored.
output.PNG: Screenshot of the scraped output (sample).
streamlite.PNG: Screenshot of the Streamlit UI (sample).
README.md: Documentation for this section of the project.
Prerequisites
Python 3.x
Selenium for browser automation
BeautifulSoup for HTML parsing
Streamlit for creating a web interface
ChromeDriver: Ensure the path to ChromeDriver is correctly set in the script.
Setup and Installation
Install the required libraries:
bash
Copy code
pip install selenium beautifulsoup4 pandas streamlit
Download ChromeDriver and specify its path in linkedin_query_scraping_streamlite.py:
python
Copy code
driver_path = "path/to/chromedriver"
Usage
Open linkedin_query_scraping_streamlite.py and update the following lines with your LinkedIn credentials:
python
Copy code
username.send_keys("your_email")  # Replace with your LinkedIn email
password.send_keys("your_password")  # Replace with your LinkedIn password
Run the Streamlit app:
bash
Copy code
streamlit run linkedin_query_scraping_streamlite.py
Enter a search query (e.g., "Data Scientists in San Francisco") in the app's text box and view the results in a table format.
Optionally, save the displayed data to linkedin_profiles.csv.
Example Queries
Some sample queries you can try in the Streamlit app:

"Software Engineers in New York"
"Data Analysts in Berlin"
"Machine Learning Experts in India"
"Project Managers in London"
"Business Decision Makers Australia"
Screenshots
1. Output of Scraped Data

2. Streamlit Interface

Disclaimers and Legal
This project is for educational purposes only. LinkedIn has strict guidelines regarding automated access to their data. Unauthorized data scraping may lead to legal repercussions and is against LinkedIn's Terms of Service. Use this tool responsibly and respect privacy policies.

Project Structure

LinkedIn_Profile_Scraping_Project/
├── scraping_using_query/
│   ├── scraping_one/
│   │   ├── linkedin_scraping_query.py
│   │   ├── linkedin_scrping_query.csv
│   │   └── README.md
├── scraping_using_streamlit/
│   ├── linkedin_query_scraping_streamlite.py
│   ├── linkedin_profiles.csv
│   ├── output.PNG
│   ├── streamlite.PNG
│   └── README.md
└── README.md (This document)
