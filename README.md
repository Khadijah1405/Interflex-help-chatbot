# Interflex Chatbot Doc Scraper 🤖📄

This project extracts help documentation from the **Interflex 6020 WebClient (v1.91)**, which is only available through offline HTML files or NTLM-protected intranet URLs. It converts the data into structured JSON or plain text and uses it as input for a **Microsoft Copilot Studio chatbot**.

---

## 📚 Sections

- [Features](#features)
- [Technologies Used](#technologies-used)
- [How to Use](#how-to-use)
  - [Option 1: Local File Scraper (Selenium)](#option-1-local-file-scraper-selenium)
  - [Option 2: Remote NTLM Web Scraper](#option-2-remote-ntlm-web-scraper)
- [Output Formats](#output-formats)
- [Repository Structure](#repository-structure)
- [Use Case](#use-case)
- [License](#license)
- [Author](#author)

---

## ✅ Features

- Extracts local help docs from `inhalt.html` using Selenium
- Authenticated scraping of protected intranet content via NTLM
- Handles JavaScript-rendered content (headless browser)
- Detects and fixes encoding issues (e.g., German Umlaute)
- Outputs chatbot-ready JSON and clean TXT
- Used to train a working chatbot in Microsoft Copilot Studio

---

## 🛠 Technologies Used

- Python 3
- Selenium + WebDriver Manager
- BeautifulSoup
- Requests + `requests_ntlm`
- `chardet` (character encoding)
- Microsoft Copilot Studio

---
## 🧑‍💻 How to Use

### ▶️ Option 1: Local File Scraper (Selenium)

**Setup:**

```bash
pip install selenium beautifulsoup4 webdriver-manager
```

**Edit and run `extract_interflex_docs.py`:**

```python
toc_url = "file:///C:/Users/YourName/.../inhalt.html"
base_folder = "C:/Users/YourName/.../WebClient_files/"
output_file = "C:/Users/YourName/.../interflex_data.json"
```

**This script will:**
- Open the TOC
- Navigate and extract rendered content
- Save results to JSON

---

### ▶️ Option 2: Remote NTLM Web Scraper

**Setup:**

```bash
pip install requests requests-ntlm beautifulsoup4 chardet
```

**Edit and run `extract_interflex_from_server.py`:**

```python
BASE_URL = "http://srv-interflex/WebClient/iflx/help/de/"
USERNAME = "your_username"
PASSWORD = "your_password"
```

**This script:**
- Authenticates to NTLM intranet site
- Parses frameset and TOC
- Extracts and cleans help text
- Outputs `interflex_help_fixed.txt`

---

## 📦 Output Formats

### JSON (for chatbot ingestion)

```json
{
  "title": "Interflex Documentation",
  "topics": [
    {
      "topic_url": "file:///...",
      "headings": ["..."],
      "content": ["..."]
    }
  ]
}
```

### TXT (for human-readable reference)

```txt
### topic1.htm ###
Interflex login process...

### topic2.htm ###
How to manage user roles...
```

---

## 📁 Repository Structure

```bash
├── extract_interflex_docs.py             # Local scraping via Selenium
├── extract_interflex_from_server.py      # NTLM web scraper
├── interflex_data.json                   # Structured chatbot data
├── interflex_help_fixed.txt              # Cleaned plain text output
└── README.md                             # Project documentation
```

---

## 💡 Use Case

This project was used to create a **Microsoft Copilot Studio chatbot** that answers questions about Interflex software based on internal documentation that isn't accessible via public URLs.

---

## 📜 License

MIT

---

## 🙋‍♀️ Author

Created by [@Khadijah1405](https://github.com/Khadijah1405)  
Based on the Interflex 6020 WebClient (v1.91)  
Built using open source tools and automation frameworks

