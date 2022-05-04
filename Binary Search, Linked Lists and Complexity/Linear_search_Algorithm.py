"""
QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table.
 She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. 
Write a function to help Bob locate the card.
"""



test = {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3}
test1 = {'input': {'cards': [6], 'query': 7}, 'output': 3}

def locate_card(cards,query):
    # Create a variable with position 0
    position = 0
    print("Cards:",cards)
    print("Query:",query)
    # Setup a loop for repetition
    while position< len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

result = locate_card(test1['input']['cards'],test1['input']['query'])
print(result)

# Complexity : O(n)
