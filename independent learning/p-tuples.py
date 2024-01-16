if __name__ == '__main__':
    # Input: Number of elements in the tuple
    n = int(input())

    # Input: n space-separated integers for the tuple
    Interger_list = map(int, input().split())

    # Create a tuple 't' from the input elements
    t = tuple(Interger_list)

    # Print the result of hash(t)
    print(hash(t))