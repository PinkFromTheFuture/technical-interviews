def union(names1, names2):
    # concatenate the arrays
    concatenation = names1 + names2

    # get the set of the concatenated array and return 
    return set(concatenation)


if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]

    print(union(names1, names2))
