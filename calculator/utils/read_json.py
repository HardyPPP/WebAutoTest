import json


def read_json():
    with open("../data/data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        arr = []
        for d in data.values():
            arr.append((d["a"], d["b"], d["exp_result"]))
        return arr

# print(read_json())