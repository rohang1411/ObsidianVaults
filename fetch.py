import urllib.request
url = 'https://raw.githubusercontent.com/TfTHacker/DashboardPlusPlus/master/.obsidian/snippets/dashboard.css'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        css = response.read().decode('utf-8')
        with open('dashboard_raw.css', 'w', encoding='utf-8') as f:
            f.write(css)
    print("Success")
except Exception as e:
    print(f"Error: {e}")
