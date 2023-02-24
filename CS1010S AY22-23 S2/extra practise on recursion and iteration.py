
def occurrence(s1, s2):
    """Counts the number of occurrences of s2 in s1"""
    print(s1)
    if s1 == "": return 0
    l2 = len(s2)
    if s2 == s1[:l2]: return 1 + occurrence(s1[l2:],s2)
    return occurrence(s1[1:],s2)



def star_wars_recursive(num_enemy_ships):
    """Take down enemy ships!!"""
    def pew(n):
        if n<=0: return ''
        return '*-' + peew(n-1)
    def peew(n):
        if n<=0: return ''
        return '*--' + pew(n-1)
    return pew(num_enemy_ships)
    
