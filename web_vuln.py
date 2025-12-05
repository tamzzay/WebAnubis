import requests
from urllib.parse import urljoin, urlencode
from bs4 import BeautifulSoup

print("\n🌐 Advanced Web Vulnerability Scanner — V2")
print("--------------------------------------------------")

target = input("Enter website URL (e.g., https://example.com): ").strip()

if not target.startswith("http"):
    target = "https://" + target

# -------------------------------
# Security Headers to Check
# -------------------------------
security_headers = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]


# -------------------------------
# Fetch URL Safely
# -------------------------------
def safe_get(url):
    try:
        return requests.get(url, timeout=6, verify=True, allow_redirects=True)
    except requests.exceptions.RequestException:
        return None


# -------------------------------
# Check Security Headers
# -------------------------------
def check_headers(response):
    missing = [h for h in security_headers if h not in response.headers]
    return missing


# -------------------------------
# SQL Injection Test
# -------------------------------
def scan_sqli(url):
    payloads = [
        "' OR '1'='1",
        "'; DROP TABLE users;--",
        "\" OR \"1\"=\"1",
        "1' ORDER BY 1--"
    ]

    for payload in payloads:
        test_url = url + payload
        resp = safe_get(test_url)
        if not resp:
            continue

        errors = ["sql", "mysql", "syntax", "database", "warning", "odbc"]
        if any(err in resp.text.lower() for err in errors):
            return True

    return False


# -------------------------------
# XSS Test
# -------------------------------
def scan_xss(url):
    payload = "<script>alert('XSS')</script>"
    test_url = url + "?" + urlencode({"q": payload})
    resp = safe_get(test_url)

    if not resp:
        return False

    return payload in resp.text


# -------------------------------
# Clickjacking Test
# -------------------------------
def scan_clickjacking(response):
    return "X-Frame-Options" not in response.headers


# -------------------------------
# Directory Listing Test
# -------------------------------
def scan_directory_listing(url):
    resp = safe_get(url)
    if not resp:
        return False

    signs = ["Index of /", "Directory listing for"]
    return any(s in resp.text for s in signs)


# -------------------------------
# Server Info Exposure Test
# -------------------------------
def scan_server_info(response):
    return response.headers.get("Server", None)


# =====================================================
# 📌 MAIN LOGIC
# =====================================================

print("\n🔎 Fetching Website...")

response = safe_get(target)
if not response:
    print("❌ Unable to reach the website.")
    exit()

print("✔ Target reachable.\n")

# 1️⃣ Security Headers
print("🔐 Checking Security Headers...")
missing = check_headers(response)
if missing:
    print("⚠ Missing Important Headers:")
    for h in missing:
        print(f"  - {h}")
else:
    print("✔ All critical headers are present.")

# 2️⃣ SQL Injection
print("\n💉 Testing for SQL Injection...")
print("⚠ Possible SQL Injection vulnerability!" if scan_sqli(target) else "✔ No SQLi detected.")

# 3️⃣ XSS
print("\n🧪 Testing for XSS...")
print("⚠ Possible XSS Vulnerability!" if scan_xss(target) else "✔ No XSS found.")

# 4️⃣ Clickjacking
print("\n🪟 Testing for Clickjacking...")
print("⚠ No X-Frame-Options header — page may be vulnerable!" if scan_clickjacking(response) else "✔ Protected by X-Frame-Options.")

# 5️⃣ Directory Listing
print("\n📂 Testing for Directory Listing...")
print("⚠ Directory listing enabled!" if scan_directory_listing(target) else "✔ No open directory listing detected.")

# 6️⃣ Server Info Leak
print("\n🛰 Checking Server Information Exposure...")
server_header = scan_server_info(response)
if server_header:
    print(f"⚠ Server Info Leaked: {server_header}")
else:
    print("✔ No server version exposed.")

print("\n✅ Scan Complete.")
print("--------------------------------------------------")
