import os

current = os.getcwd()

for i in range(10, 200):
    if i == 148:
        continue
    with open(f"{current}/random_files/file{i}", "rb") as f:
        delete = False
        content = f.read().hex()
        if content[:6] == "ffd8ff":
            os.rename(f"{current}/random_files/file{i}", f"{current}/random_files/file{i}.jpeg")
        else:
            delete = True
    if delete:
        os.remove(f"{current}/random_files/file{i}")
