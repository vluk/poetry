import json

with open("delimited.txt", "r") as poems:
    with open("delimited.json", "w") as json_poems:
        poem_list = poems.read().split("<|endoftext|>\n<|startoftext|>")
        print(len(poem_list))
        json.dump(
            poem_list,
            json_poems,
            indent=4,
        )

