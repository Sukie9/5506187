if __name__ == '__main__':
    # Initialize an empty list
    my_list = []

    # Read the number of commands
    n = int(input())

    # Iterate through each command
    for _ in range(n):
        command = input().split()

        # Perform the corresponding operation based on the command
        if command[0] == "insert":
            # Insert integer at position
            i, e = map(int, command[1:])
            my_list.insert(i, e)
        elif command[0] == "print":
            # Print the list
            print(my_list)
        elif command[0] == "remove":
            # Delete the first occurrence of integer
            e = int(command[1])
            my_list.remove(e)
        elif command[0] == "append":
            # Insert integer at the end of the list
            e = int(command[1])
            my_list.append(e)
        elif command[0] == "sort":
            # Sort the list
            my_list.sort()
        elif command[0] == "pop":
            # Pop the last element from the list
            my_list.pop()
        elif command[0] == "reverse":
            # Reverse the list
            my_list.reverse()