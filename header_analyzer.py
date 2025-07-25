# http_header_analyzer.py

import requests
from urllib.parse import urlparse

def analyze_headers(url):
    """
    Fetches HTTP headers for a given URL and provides basic security analysis.
    """
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'https://' + url # Default to HTTPS if no scheme is provided

    try:
        response = requests.get(url, timeout=5) # 5-second timeout for request
        headers = response.headers
        print(f"\n--- HTTP Headers for {url} ---")
        for key, value in headers.items():
            print(f"{key}: {value}")

        print("\n--- Security Header Analysis ---")
        
        # Check for common security headers
        security_headers = {
            "Strict-Transport-Security": "HSTS helps protect against man-in-the-middle attacks by enforcing HTTPS. Recommended!",
            "Content-Security-Policy": "CSP helps prevent XSS and data injection attacks by controlling resources the browser can load. Highly Recommended!",
            "X-Content-Type-Options": "Prevents MIME sniffing attacks. Recommended!",
            "X-Frame-Options": "Prevents clickjacking attacks by controlling if a page can be put in a frame. Recommended!",
            "Referrer-Policy": "Controls how much referrer information is sent with requests. Recommended!",
            "Permissions-Policy": "Allows or disallows the use of browser features. Recommended!",
            "Set-Cookie": "Check for 'Secure', 'HttpOnly' flags on cookies for better security."
        }

        found_security_headers = []
        missing_security_headers = []
        
        for header, description in security_headers.items():
            if header in headers:
                print(f"[+] {header} Found: {description}")
                found_security_headers.append(header)
                if header == "Set-Cookie" and "Set-Cookie" in headers:
                    cookie_value = headers["Set-Cookie"]
                    if "Secure" not in cookie_value:
                        print("    [!] 'Secure' flag missing in Set-Cookie. Cookie might be sent over HTTP.")
                    if "HttpOnly" not in cookie_value:
                        print("    [!] 'HttpOnly' flag missing in Set-Cookie. Cookie might be accessible via client-side scripts (XSS).")
            else:
                print(f"[-] {header} Missing: {description}")
                missing_security_headers.append(header)
        
        if not found_security_headers:
            print("[!] No common security headers found. This site might be vulnerable.")
        
    except requests.exceptions.MissingSchema:
        print(f"Error: Invalid URL format. Please include http:// or https:// or make sure it's a valid domain.")
    except requests.exceptions.ConnectionError:
        print(f"Error: Could not connect to {url}. Check the URL or your internet connection.")
    except requests.exceptions.Timeout:
        print(f"Error: Request to {url} timed out. The server might be slow or unresponsive.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("\n--- Simple HTTP Header Analyzer ---")
    print("Enter 'q' to quit.")

    while True:
        target_url = input("\nEnter a URL (e.g., example.com, https://google.com): ")
        if target_url.lower() == 'q':
            print("Exiting Header Analyzer. Goodbye!")
            break
        
        if not target_url:
            print("URL cannot be empty. Please try again.")
            continue
            
        analyze_headers(target_url)
        print("\n-------------------------------------\n")