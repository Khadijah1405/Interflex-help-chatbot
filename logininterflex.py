
import requests
from bs4 import BeautifulSoup
from requests_ntlm import HttpNtlmAuth

# Base URL for Interflex help documentation
BASE_URL = "http://srv-interflex/WebClient/iflx/help/en/"

# NTLM Authentication Credentials (Update these)
USERNAME = "..." #enter your username
PASSWORD = "..." #enter your password

# Start a session with NTLM authentication
session = requests.Session()
session.auth = HttpNtlmAuth(USERNAME, PASSWORD)

# Step 1: Access the main frameset page
frameset_url = BASE_URL + "index.htm"
frameset_response = session.get(frameset_url)

if frameset_response.status_code == 200:
    soup = BeautifulSoup(frameset_response.text, "html.parser")

    # Step 2: Extract TOC frame link (where help topics are listed)
    toc_frame = soup.find("frame", {"name": "TOC"})
    if toc_frame:
        toc_url = BASE_URL + toc_frame["src"]
        print(f"TOC URL found: {toc_url}")

        # Step 3: Extract links to individual help pages from TOC
        toc_response = session.get(toc_url)
        toc_soup = BeautifulSoup(toc_response.text, "html.parser")

        # Collect all help topic links
        help_links = [a["href"] for a in toc_soup.find_all("a", href=True)]

        extracted_content = ""

        # Step 4: Visit each help topic page and extract content
        for link in help_links:
            help_page_url = BASE_URL + link
            page_response = session.get(help_page_url)

            if page_response.status_code == 200:
                page_soup = BeautifulSoup(page_response.text, "html.parser")
                text_content = page_soup.get_text()
                extracted_content += f"\n\n### {link} ###\n{text_content}"
            else:
                print(f"Failed to load {help_page_url}")

        # Step 5: Save extracted content
        with open("interflex_help.txt", "w", encoding="utf-8") as file:
            file.write(extracted_content)

        print("Help documentation extracted successfully!")

    else:
        print("TOC frame not found.")
else:
    print(f"Failed to load frameset page: {frameset_response.status_code}")
