import json

with open("universities.json") as f:
    data = json.load(f)


import time

# your code...
start = time.time()

for university in data:
    if "iub.edu.pk" in university["domains"]:
        print(university["name"])
end = time.time()
print(end - start, "time elapsed")  # t
