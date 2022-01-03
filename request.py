import time
import requests

URL = "http://127.0.0.1:5000/predict"
requests.get("http://127.0.0.1:5000/")    
        
response = requests.post(URL, json='{"text":"Ужасно, просто отвратительно!"}')
print("Текст: Ужасно, просто отвратительно! Результат: ", response.json()["answer"][1:-1])
    
response = requests.post(URL, json='{"text":"Все сделали быстро, я рад!"}')
print("Текст: Все сделали быстро, я рад! Результат: ", response.json()["answer"][1:-1])

time.sleep(100)
