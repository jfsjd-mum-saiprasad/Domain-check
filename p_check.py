import re
import requests

def is_wordpress(domain):
    try:
        response = requests.get(domain)
        if response.status_code == 200:
            content = response.content.decode('utf-8')
            # Search for the WordPress meta tag in the HTML content
            match = re.search(r'<meta name="generator" content="WordPress', content)
            if match:
                # Search for the WordPress version number in the HTML content
                version_match = re.search(r'content="WordPress ([0-9]+\.[0-9]+)', content)
                if version_match:
                    return "Yes, version " + version_match.group(1)
                else:
                    return "Yes, version unknown"
            else:
                return "No"
    except:
        return "Error: Unable to retrieve the website content"

domain = input("Enter a domain: ")
result = is_wordpress(domain)
print(result)