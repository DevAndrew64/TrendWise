import requests

BASE_URL = "http://localhost:5000"

def test_api():
    response = requests.get(f"{BASE_URL}/predict/smartphones")
    assert response.status_code == 200
    print("API Test Passed ✅")

if __name__ == "__main__":
    test_api()
