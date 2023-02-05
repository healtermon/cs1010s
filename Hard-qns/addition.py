# {'A':8,'C':1,'L':9}
# "ANT","MAN","COOL"
# addition_puzzle("PEN","PINE","APPLE","APPLE","PEN","PLANE")
# addition_puzzle("SAVE","MORE", "MONEY")
def pp(x): [print(i) for i in x]
def addition_puzzle(*all_words):
    words = all_words[:-1]
    last_word = all_words[-1]
    unique_chars = list(set(''.join(all_words)))
    initials = {w[0] for w in all_words}
    possible_vals = range(10)


    print(f"words = {words}\nlast_word = {last_word}\nunique_chars={unique_chars}\n"
          + f"initials={initials}\npossible_vals={possible_vals}")
    
    def check_final_equality(d):
        def word_value(word, d):
            return eval(''.join([str(d[letter]) for letter in word]))
        def word_value_alternate(word, d):
            """because I misinterpreted the question, I have an alternate one here"""
            return sum([d[letter] for letter in word])
        return sum([word_value(w,d) for w in words]) == word_value(last_word,d)
    
    
    def is_valid_item(val,letter,d):
        def cond1(letter,val):
            """ Condition 1: The leftmost letter cannot be zero in any word """
            return not (val == 0 and letter in initials)
        def cond2(val,d):
            """
            Condition 2: There must be a one-to-one-mapping between letters and digits.
            In other words, if you choose the digit 6 for the letter M,
            then all the M's in the puzzle must be 6 and no other letter can be a 6
            """
            return not val in d.values()
        
        # c1 = cond1(letter,val)
        # c2 = cond2(val,d)
        #print(f"c1={c1},c2={c2}")
        return cond1(letter,val) and cond2(val,d)

    def solve(cs,d):
        solve.counter+=1
        if cs == []:
            if check_final_equality(d):
                #print(f"solution found! d={d}")
                return d
            #print(f"wrong solution:{d}")
            return False
                
        #print(f"starting, cs={cs}----------------------- d={d}") 
        c = cs[0]
        #print(f"c={c},d={d}")
        for val in possible_vals:
            #print(f"checking for val={val}:")
            if is_valid_item(val,c,d):
                d[c] = val
                #print(f"valid! modified d={d}")
                solution = solve(cs[1:],d)
                if solution:
                    print(f"solution received! c={c}, passing on...")
                    return solution
                
                #print("no solution found, next val")
                del d[c]        # undo
        return False # nothing found, return

    solve.counter = 0
    sol = solve(unique_chars, dict())
    left = list(''.join(words))
    left.sort()
    left = ''.join(left)
    right = list(last_word)
    right.sort()
    right = ''.join(right)
    print(f"{left}={right}")
    print(f"number of iterations: {solve.counter}")
    return sol


        
