import requests

url = "https://be-shopee-project.onrender.com/api/products/ping"

try:
    response = requests.head(url, timeout=10)  # dùng HEAD cho nhẹ
    print(f"Ping status code: {response.status_code}")
    if response.status_code == 200:
        print("✅ Server is UP")
    else:
        print("⚠ Server responded but not 200 OK")
except Exception as e:
    print(f"❌ Ping failed: {e}")