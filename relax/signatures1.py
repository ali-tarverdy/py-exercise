key = 0xFF


def toggle_bits(data):
    res = bytes([item ^ key for item in data])
    return res


with open("heart.gif", "rb") as f:
    content = f.read()
    # print(content)

out = toggle_bits(content)

with open("heart.gif", "wb") as f1:
    f1.write(out)
