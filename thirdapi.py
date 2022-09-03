import requests
import json

url="http://127.0.0.1:8000/studentdata/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    req=requests.get(url=url,headers={'content-type':'application/json'},data=json_data)
    data=req.json()
    print(data)

#get_data()

def post_data():
    data={
        'id':3,
        'name':'rohit',
        'roll':452,
        'address':'pathankot',
    }
    json_data=json.dumps(data)
    req = requests.post(url=url, headers={'content-type': 'application/json'}, data=json_data)
    data = req.json()
    print(data)

#post_data()

def put_data():
    data={
      'id':3,
     'name':'shantanu',
     'address':'sujanpjur'
    }
    json_data=json.dumps(data)
    req = requests.put(url=url, headers={'content-type': 'application/json'}, data=json_data)
    data = req.json()
    print(data)
#put_data()

def delete_data(id=None):
    data={'id':id}
    json_data=json.dumps(data)
    req = requests.delete(url=url, headers={'content-type': 'application/json'}, data=json_data)
    data = req.json()
    print(data)

delete_data(2)


