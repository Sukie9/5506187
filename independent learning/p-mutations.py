def mutate_string(string, position, character):
    s_list = list(s)

    # Update the character at the specified position
    s_list[position] = character

    # Join the list back into a string
    modified_string = "".join(s_list)

    return modified_string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)