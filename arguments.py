import argparse

def demo() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(help="Input a string", dest="string", type=str)
    parser.add_argument(help="Input an integer", dest="integers", type=int)
    parser.add_argument(help="Input a float", dest="float", type=float)

    args = parser.parse_args()

    string = args.string
    integer = args.integers
    floats = args.float

    print("String is: ", string)
    print("Integer is: ", integer)
    print("Float is: ", floats)

if __name__ == "__main__":
    demo()