def pins_felled(game): # Time: O(n), Space: O(1)
    total = 0          # 1a. variable to store result
    for c in game:     # 2. loop
        total += int(c)
    return total       # 1b. variable to store result

def pins_felled(game):
    total = 0          # 1a. variable to store result
    for i in range(len(game)):     # 2. loop
        total += int(game[i])
    return total       # 1b. variable to store result

def pins_felled(game): # Time: O(n^2), Space: O(n^2)
    if game == "":
        return 0
    else:
        return int(game[0]) + pins_felled(game[1:])

def pins_felled(game): # Time: O(n^2), Space: O(n)
    total = 0          # 1a. variable to store result
    while game != "":  # 2. loop
        total += int(game[0])
        game = game[1:]
    return total       # 1b. variable to store result

print(pins_felled("45678"))
print(pins_felled("450927"))
print(pins_felled("9999999999"))

def compute_score(game): # Time: O(n^2), Space: O(n^2)
    if game == "":
        return 0
    elif game[0] != "9" or len(game)==1:
        return int(game[0]) + compute_score(game[1:])
    else:
        return int(game[0]) + int(game[1]) +compute_score(game[1:])

def compute_score(game): # Time: O(n), Space: O(1)
    total = 0
    for i in range(len(game)):
        if game[i] != "9" or i==len(game)-1:
            total += int(game[i])
        else:
            total += int(game[i]) + int(game[i+1])
    return total

print(compute_score("4927"))
print(compute_score("049090"))








