import json

a = r".encode('unicode_escape')"
x = a.encode('unicode_escape')

y = json.dumps(a)
print(y)