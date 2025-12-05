WebAnubis
---
### 🌐 Web Vulnerability Scanner (Python)

WebAnubis is a lightweight yet powerful web vulnerability scanner built in Python.
It performs essential security checks including:

  - Security Header Analysis 
  - SQL Injection Detection 
  - XSS Injection Detection 
  - Clickjacking Protection Check 
  - Directory Listing Exposure 
  - Server Information Leakage

Perfect for students, beginners, red teamers, and anyone who wants a simple and effective web security assessment tool.

---
### 🚀 Features

  -  Detects missing security headers 
  - SQL Injection vulnerability scan 
  - XSS reflection testing 
  - Checks for clickjacking protection 
  - Directory listing exposure check 
  - Server banner leakage detection 
  - Clean, interactive CLI 
  - Works on Linux, Windows, macOS

---
### 📦 Installation

git clone https://github.com/yourusername/WebSpectreScanner.git

cd WebSpectreScanner

pip install -r requirements.txt

---
▶️ Usage

python scanner.py


Enter a target such as:

https://example.com

---
### 🖥 Sample Output (Demo Screenshot Text)

---
🌐  Web Vulnerability Scanner 

--------------------------------------------------
Enter website URL (e.g., https://example.com): https://instagram.com

🔎 Fetching Website...
✔ Target reachable.

🔐 Checking Security Headers...
⚠ Missing Important Headers:
  - Referrer-Policy

💉 Testing for SQL Injection...
✔ No SQLi detected.

🧪 Testing for XSS...
✔ No XSS found.

🪟 Testing for Clickjacking...
✔ Protected by X-Frame-Options.

📂 Testing for Directory Listing...
✔ No open directory listing detected.

🛰 Checking Server Information Exposure...
✔ No server version exposed.

✅ Scan Complete

---
🛠 Tech Stack

  - Python 3
  - requests 
  - BeautifulSoup4

---
### 📚 For Educational Use

This tool is intended for:

  - Learning web security 
  - Enhancing ethical hacking skills 
  - Demonstrating vulnerabilities in controlled environments

---
⚠️ Do NOT scan websites without permission.

---
### ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---
