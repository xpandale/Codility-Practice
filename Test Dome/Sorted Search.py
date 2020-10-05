'''
Implement function count_numbers that accepts a sorted list of unique integers and, efficiently with respect to time used, counts the number of list elements that are less than the parameter less_than.

For example, count_numbers([1, 3, 5, 7], 4) should return 2 because there are two list elements less than 4.
'''

def count_numbers(sorted_list, less_than):
    left, right = 0, len(sorted_list) - 1
    middle = 0
    while left <= right:
        middle = (left + right) // 2
        print(f"middle: {middle}")
        if sorted_list[middle] < less_than:
            if middle < len(sorted_list) -1 and sorted_list[middle + 1] < less_than:
                left = middle + 1
                continue
            else:
                return middle + 1
        if sorted_list[middle] >= less_than:
            right = middle - 1
        else:
            left = middle + 1

    return 0    

if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7]
    print(count_numbers(sorted_list, 4)) # should print 2
    print(count_numbers(sorted_list, 8)) # should print 4
    print(count_numbers(sorted_list, 0)) # should print 0
    print(count_numbers(sorted_list, 1)) # should print 0
