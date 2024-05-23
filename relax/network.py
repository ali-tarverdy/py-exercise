import hashlib
import time

while True:

    file_path = "/tmp/test.txt"

    real_digest = "29d6c6097b5fc72a7c99636c07d6995b24b5ef2985b2ada7c68463ddada85624"

    file = open(file_path, "rb").read()

    calculate_digest = hashlib.sha256(file).hexdigest()

    # print(calculate_digest)
    if calculate_digest == real_digest:
        print("file is ok")
    else:
        print("Danger you are hacked")
    time.sleep(5)
