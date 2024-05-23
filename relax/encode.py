import pickle

name = ["Ali", "Sara", "Reza", "Arezo"]

age = [20, 19, 26, 30]

gender = ["Male", "Female", "Unknown", "Female"]

database = {"Name": name, "Age": age, "gender": gender}

with open("data.dat", "wb") as f:
    pickle.dump(database, f)
