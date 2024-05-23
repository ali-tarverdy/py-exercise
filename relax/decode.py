import pickle

with open("data.dat", "rb")as f:
    data = pickle.load(f)
    print(data)
