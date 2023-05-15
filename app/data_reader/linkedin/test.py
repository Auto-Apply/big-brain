import os

file = "linkedin.query"
path = os.path.abspath(f"../../../data/{file}")
with open(path, "r") as f:
    content = f.readlines()
    content = [x.strip() for x in content]
    search_filter = " ".join(content)
    print(search_filter)
