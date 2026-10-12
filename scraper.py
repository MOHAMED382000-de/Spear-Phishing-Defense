import requests
from bs4 import BeautifulSoup

def scrape_target_profile(target_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    
    try:
        print(f"Connecting to URL: {target_url}...")
        response = requests.get(target_url, headers=headers)
        
        if response.status_code == 200:
            print("[+] Connection successful and page content retrieved!")
            soup = BeautifulSoup(response.text, 'html.parser')
            
            extracted_keywords = []
            for heading in soup.find_all(['h1', 'h2', 'p']):
                text = heading.get_text(strip=True)
                if text:
                    extracted_keywords.append(text)
                    
            return extracted_keywords
        else:
            print(f"[-] Connection failed. Status code: {response.status_code}")
            return []
            
    except Exception as e:
        print(f"[-] An unexpected error occurred: {e}")
        return []

if __name__ == "__main__":
    target = "https://example.com" 
    data = scrape_target_profile(target)
    
    print("\n--- Extracted Data ---")
    if data:
        for index, info in enumerate(data[:10], 1):
            print(f"{index}. {info}")
    else:
        print("No data found.")