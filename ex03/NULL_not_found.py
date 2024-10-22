def NULL_not_found(object: any) -> int:
    """
    Function that identifies and prints different types of null-like values in Python.
    """
    if object is None:
        print(f"Nothing: {object} {type(object)}")
        return 0
    elif isinstance(object, float) and str(object) == 'nan':
        print(f"Cheese: {object} {type(object)}")
        return 0
    elif isinstance(object, int) and object == 0:
        print(f"Zero: {object} {type(object)}")
        return 0
    elif isinstance(object, str) and not object:
        print(f"Empty: {type(object)}")
        return 0
    elif isinstance(object, bool) and not object:
        print(f"Fake: {object} {type(object)}")
        return 0
    else:
        print("Type not Found")
        return 1

if __name__ == "__main__":
    pass
