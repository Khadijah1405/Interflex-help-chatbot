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
