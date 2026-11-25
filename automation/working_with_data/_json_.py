import json

student_data = {
    "name": "Taofeek",
    "course": "Computer Science",
    "level": 300,
    "skills": [
        "Python",
        "Linux",
        "Networking",
    ]
}

with open("student.json", "w") as file:
    json.dump(student_data, file, indent=4, sort_keys=True, ensure_ascii=False)


with open("student.json", "r") as file:
    deserialized_json_file = json.load(file)

student = deserialized_json_file

data_1 = '{"name": "Taofeek", "age": 23, "course": "computer-science"}'
deserialized_json_data = json.loads(data_1)


# Json doesn't have a set type, convert to list first.
# A common JSON error is JSONDecodeError


server = {
    "host": "127.0.0.1",
    "port": 8080,
    "services": [
        "HTTPS",
        "SSH",
        "FTP",
        ],
    "online": False,
    
}

serialised_string = json.dumps(server, indent=4)
print(serialised_string)

deserialized_string = json.loads(serialised_string)
print(type(deserialized_string))
print(deserialized_string["host"])
print(deserialized_string["services"][1])
print(deserialized_string["online"])


# JSON, the language of applications
# create, return = [json.dump, json.load]
