import requests
import json

URL = "http://127.0.0.1:5000/api/people"


def delete(name):
  requests.delete(f"{URL}{name}")


def create(name=None):
    person = {"fname": name[0], "lname": name[1]}
    response = requests.post(URL, json=person)
    if response.ok is True:
        print(response.text)
    else:
        response_json = json.loads(response.text)
        print(response_json.get("detail"))


def update(name):
    path = f'/{name[1]}'
    person = {"fname": name[0], "lname": name[1]}
    response = requests.put(URL + path, json=person)
    if response.ok is True:
        print(f'Person {name} updated successfully')
    else:
        response_json = json.loads(response.text)
        print(response_json.get("detail"))


def get(name):
    response = requests.get(f"{URL}{name}")
    print(response.text)


def get_all():
    response = requests.get(URL)
    response_json = json.loads(response.text)
    for person in response_json:
        for key, value in person.items():
            print(key, value)



get_all()
