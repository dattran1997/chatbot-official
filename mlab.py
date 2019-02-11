import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds243054.mlab.com:43054/demochatbot


host = "ds243054.mlab.com"
port = 43054
db_name = "demochatbot"
user_name = "admin"
password = "admin123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
