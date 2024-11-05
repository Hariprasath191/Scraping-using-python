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


### Part 2: LinkedIn Profile Scraping with Streamlit (`scraping_using_streamlit`)
This part adds a user interface using Streamlit, enabling users to enter a search query and view the scraped profiles in a table format within the Streamlit app. This is useful for quick, interactive data retrieval based on user input.

### Files and Folders
- **`linkedin_query_scraping_streamlite.py`**: Streamlit app that takes a search query from the user and displays the scraped profiles in a table format.
- **`linkedin_profiles.csv`**: CSV file where the scraped LinkedIn profile data is stored.
- **`output.PNG`**: Screenshot of the scraped output (sample).
- **`streamlite.PNG`**: Screenshot of the Streamlit UI (sample).

## Setup and Installation
Install the required libraries:
    

    pip install requirements.txt

1.Intall the required libraries inside the virtual environment

2.Download ChromeDriver and specify its path in linkedin_query_scraping_streamlite.py
    
3.Open linkedin_query_scraping_streamlite.py and update your linkedin id and your password 
    
Run the Streamlit app:
    

    streamlit run linkedin_query_scraping_streamlite.py

### Example Queries
    Some sample queries you can try in the Streamlit app:

    1."Software Engineers in New York"
    2."Data Analysts in Berlin"
    3."Machine Learning Experts in India"
    4."Project Managers in London"
    5."Business Decision Makers Australia"
    6."Hariprasath"
    7."Bala"

### Screenshots
1. Output of Scraped Data

2. Streamlit Interface

