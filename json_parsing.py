import json

string_as_json_format = '{"answer": "Hello"}'
obj = json.loads(string_as_json_format)
print(obj['answer'])