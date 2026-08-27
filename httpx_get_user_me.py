import httpx


payload = {
    "email": "test@mail.ru",
    "password": "11111111"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload)

print(login_response.json())
print(login_response.status_code)

access_token = login_response.json()["token"]["accessToken"]

headers = {
    "Authorization": f"Bearer {access_token}"
}

users_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

print(users_me_response.json())
print(users_me_response.status_code)