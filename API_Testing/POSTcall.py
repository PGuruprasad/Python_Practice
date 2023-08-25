import requests

head = {
"accept" : "text/plain",
"Content-Type": "application/json"
}
payload = {
  "id": 10,
  "title": "string",
  "dueDate": "2023-07-03T02:38:52.571Z",
  "completed": True
}

response=requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities", headers=head,json=payload)
print(response.status_code)
print(response.json())

assert response.status_code == 200