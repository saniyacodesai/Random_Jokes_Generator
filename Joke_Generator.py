import requests

print("😂 Welcome to the Random Joke Generator!")

url = "https://icanhazdadjoke.com/"
headers = {"Accept": "application/json"}

print("📡 Sending request to the API...")

try:
    response = requests.get(url, headers=headers)
    print(f"✅ Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        print(f"\nHere's your joke: {data['joke']}\n")
    else:
        print("❌ Failed to fetch a joke. API might be down.")
except requests.exceptions.RequestException as e:
    print(f"🌐 Network error: {e}")