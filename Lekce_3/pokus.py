def plus_one(x):
    """
    informace o proměnné x
    """
    print("hodnata:", x)
    print("typ: ", type(x))
    print("Identita: ", id(x))
    print(x, "plus jedna je", (x+1))
x = 13
plus_one(x)