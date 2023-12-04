import requests
import re

def get_h3_headlines(url):
    my_req = requests.get(url)
    pattern = r'<h3[^>]*>(.*?)</h3>'
    headlines = re.findall(pattern, my_req.text)

    return "Список пуст" if len(headlines) == 0 else headlines