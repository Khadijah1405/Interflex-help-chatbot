from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import json
import os

# ✅ Setup Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--allow-file-access-from-files")  # ✅ Allow local file access

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# ✅ Step 1: Open TOC (Table of Contents) - Now using `inhalt.html`
toc_url = "file:///C:/Users/...//inhalt.html" #enter your user url
driver.get(toc_url)

# ✅ Wait for page to load
time.sleep(5)

# ✅ Extract all documentation links from TOC
soup = BeautifulSoup(driver.page_source, "html.parser")
links = soup.find_all("a")

# ✅ Define base local folder where extracted HTML files exist
base_folder = "C:/Users/...../Interflex 6020 WebClient Version 1.91 Interflex Datensysteme GmbH & Co. KG_files/" #enter your directory

all_text = []

if links:
    print(f"✅ Found {len(links)} topics in `toc.html`. Extracting content...")

    for index, link in enumerate(links):
        href = link.get("href")

        # ✅ Ignore empty and anchor links
        if not href or href.startswith("#"):
            continue

        # ✅ Convert Interflex Server URLs to Local Paths
        if "srv-interflex" in href:
            file_name = href.split("/")[-1]  # Extract filename
            local_file_path = os.path.join(base_folder, file_name).replace("\\", "/")
        else:
            local_file_path = os.path.join(base_folder, href).replace("\\", "/")

        # ✅ Ensure file exists
        if not os.path.exists(local_file_path):
            print(f"⚠️ Skipping missing file: {local_file_path}")
            continue

        local_file_url = f"file:///{local_file_path}"

        print(f"🔄 Opening topic {index}: {local_file_url}")

        try:
            driver.get(local_file_url)  # Open the topic page
            time.sleep(3)  # Allow content to load

            # ✅ Extract fully rendered HTML
            topic_soup = BeautifulSoup(driver.page_source, "html.parser")

            # ✅ Extract headings and text
            headings = [h.text.strip() for h in topic_soup.find_all(["h1", "h2", "h3"])]
            paragraphs = [p.text.strip() for p in topic_soup.find_all("p") if p.text.strip()]

            all_text.append({
                "topic_url": local_file_url,
                "headings": headings,
                "content": paragraphs
            })

            print(f"✅ Extracted content from topic {index}.")

        except Exception as e:
            print(f"⚠️ Failed to extract content from {local_file_url}: {e}")

else:
    print("❌ No topics found in `toc.html`.")

# ✅ Define Output Directory and File
output_folder = "C:/Users/..../" #enter your directory
output_file = os.path.join(output_folder, "interflex_data.json")

# ✅ Ensure the directory exists
if not os.path.exists(output_folder):
    print(f"📂 Creating missing folder: {output_folder}")
    os.makedirs(output_folder, exist_ok=True)

# ✅ Save extracted data
data = {
    "title": "Interflex Documentation",
    "topics": all_text
}

# ✅ Write JSON file safely
try:
    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)
    print(f"✅ Full documentation content extracted and saved to {output_file}")

except Exception as e:
    print(f"❌ Error saving JSON file: {e}")

# ✅ Close browser
driver.quit()
