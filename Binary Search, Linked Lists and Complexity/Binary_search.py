"""
QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table.
 She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. 
Write a function to help Bob locate the card.
"""

# cars.sort(reverse=True) sort in descending order


test = {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 13}, 'output': 3}
test1 = {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6,6,2,2,2,0,0,0], 'query': 6}, 'output': 3}

def test_location(cards, query, mid):
    if cards[mid] == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif cards[mid] < query:
        return 'left'
    else:
        return 'right'

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        print("low:",lo,"High:",hi)
        
        mid = (lo + hi) // 2
        print("Mid:",mid)
        result = test_location(cards, query, mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1

result = locate_card(test['input']['cards'],test['input']['query'])
print(result)

# Analysing complexity
# Initial length - N
# Iteration 1 - N/2
# Iteration 2 - N/2^2
# Iteration 3 - N/2^3
# Iteration k - N/2^k
# N / 2^k =1
# N = 2^k
# k = log N
