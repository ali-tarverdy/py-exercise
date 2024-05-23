import sys


def yes():
    try:
        if len(sys.argv) > 1:
            while True:
                print(sys.argv[1])
        else:
            while True:
                print("y")
    except KeyboardInterrupt:
        pass


yes()
