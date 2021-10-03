"""
The full-form of JSON is JavaScript Object Notation. 
It means that a script (executable) file which is made of text in a programming language, is used to store and transfer the data. 
Python supports JSON through a built-in package called json. 
To use this feature, we import the json package in Python script. 
The text in JSON is done through quoted string which contains the value in key-value mapping within { }.
"""

"""
Reading From JSON
It’s pretty easy to load a JSON object in Python. 
Python has a built-in package called json, which can be used to work with JSON data. 
It’s done by using the json module, which provides us with a lot of methods which among loads() and load() methods are gonna help us to read the JSON file.
"""

"""
Deserialization of JSON
The Deserialization of JSON means the conversion of JSON objects into their respective Python objects. 
The load()/loads() method is used for it. 
If you have used JSON data from another program or obtained as a string format of JSON, then it can easily be deserialized with load()/loads(), which is usually used to load from string, otherwise the root object is in list or dict. 
"""

"""
json.load(): json.load() accepts file object, parses the JSON data, populates a Python dictionary with the data and returns it back to you.
"""

import json
 
with open(r"resources\sample_data\test.json", mode="r") as f:
    # returns JSON object as a dictionary
    data = json.load(f)
  
print(f"{data} --> {type(data)}")
print('***************************')

"""
json.loads(): If you have a JSON string, you can parse it by using the json.loads() method.
json.loads() does not take the file path, but the file contents as a string, using fileobject.read() with json.loads() we can return the content of the file.
"""

# JSON string
string_format_json = '{"name": "Bob", "languages": "English"}'

# deserializes into dict and returns dict.
dict_format = json.loads(string_format_json)
print(f"Json string to Dictionary:: {dict_format} --> {type(dict_format)}")

# JSON file
with open(r"resources\sample_data\test.json", mode='r') as f:
    # Reading from file
    data = json.loads(f.read())

print(f"Json file reading to Dictionary:: {data} --> {type(data)}")
print('***************************')


"""
json.loads() takes in a string and returns a json/dict object.
Whereas json.dump() takes in a json/dict object and returns a string.
As you can see, json.dumps() and json.loads() are opposite of one another.
"""

# creating a dictionary/json object
dict_format = {'name':'John', 'languages':['Python', 'AWS']}

# dumping the dict object into a string format
string_format = json.dumps(dict_format)

print(f"{string_format} --> {type(string_format)}")
