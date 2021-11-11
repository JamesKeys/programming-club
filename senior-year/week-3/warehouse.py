# Created by James Keys at Villanova University for Programming Club
# Solves Kattis problem found here: https://open.kattis.com/problems/warehouse

num_cases = int(input())


def get_next_toy(dict_toys: dict):
    """
    Function which takes in the dictionary of string keys and integer values and returns
    the key with the largest value - ties broken alphabetically.
    :param dict_toys: dictionary holding the toys with their respective counts
    :returns: string key which should be printed and then deleted next
    """
    # dictionary to hold value, key pairs to allow for grouping by counts
    reverse_dict = {}
    # for each toy,
    for key in list(dict_toys.keys()):
        # if we already have it's count stored, append it to the list
        if dict_toys[key] in reverse_dict:
            reverse_dict[dict_toys[key]].append(key)
        # otherwise, we need to create a list to hold all toys with this count value
        else:
            reverse_dict[dict_toys[key]] = [key]
    # variable to hold the next highest count
    next_val = max(reverse_dict)
    # now return the first alphabetical toy with this count
    return min(reverse_dict[next_val])


for case_i in range(num_cases):
    num_shipments = int(input())
    
    # dictionary to hold string, int pairs with toy names and their counts
    toys = {}
    
    for shipment_i in range(num_shipments):
        toy_name, toy_count = input().split()
        toy_count = int(toy_count)
        
        # if we have already seen this toy in a previous shipment, add to value
        if toy_name in toys:
            toys[toy_name] += toy_count
        # else, create new key, value pair
        else:
            toys[toy_name] = toy_count

    print(len(list(toys.keys())))
    # while there are still more toys to be printed,
    while len(list(toys.keys())) > 0:
        # get the next value to be printed, print it, then remove from dictionary
        print_val = get_next_toy(toys)
        print(print_val, toys[print_val])
        del toys[print_val]