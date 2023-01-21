import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file) -> list[dict]:
    with open(file) as f:
        list_ = f.readlines()
    list_new = [i[:-1].split(sep=",") for i in list_]
    return [{list_new[0][value]: item for value, item in enumerate(list_new[i])} for i in range(1, len(list_new))]


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

