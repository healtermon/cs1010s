
def make_dolls(names):
    return (0, names)

def name_of(doll):
    return doll[1][doll[0]]

def daughter_of(doll):
    next_index = doll[0]+1
    if next_index > len(doll[1])-1:
       next_index = len(doll[1])-1
    return(next_index,doll[1])

def daughter_of(doll):
    return(min(doll[0]+1,len(doll[1])-1),doll[1])

def mother_of(doll):
    next_index = doll[0]-1
    if next_index < 0:
       next_index = 0
    return(next_index,doll[1])

a = make_dolls(('Alice', 'Betty', 'Clara'))
b = daughter_of(a)
c = daughter_of(b)

def contains(d1, d2):
    d = d1
    while d != daughter_of(d):
        d=daughter_of(d)   
        if d==d2:
            return True
    return False

def is_same_set(d1, d2): # Wrong - break abstraction
    return d1[1] == d2[1]


def is_same_set(d1, d2):
    return d1==d2 or contains(d1,d2) or contains(d2,d1)

def num_dolls(doll): # Wrong - break abstraction
    return len(doll[1])

def num_dolls(doll):
    count = 1
    d = doll
    while d != daughter_of(d):
        count += 1
        d = daughter_of(d)
    d = doll
    while d != mother_of(d):
        count += 1
        d = mother_of(d)
    return count


def make_star(name,mass):
    return (name,mass)

def star_name(star):
    return star[0]

def star_mass(star):
    return star[1]

def make_cons(name):
    return (name, (), ()) # (name, stars, const)

def add_star(star, cons):
    return (cons[0], cons[1] + (star,), cons[2])

def add_cons(child, parent):
    return (parent[0], parent[1], parent[1]+(child,))

def get_stars(cons)
    result = cons[1]
    for con in cons[2]:
        stars = get_stars(cons)
        for star in stars:
            if star not in result:
                result += (star,)
    return result

def get_cons(cons):
    result = cons[2]
    for con in cons[2]:
        cons = get_cons(cons)
        for c in cons:
            if c not in result:
                result += (c,)
    return result

def total_mass(cons): # Wrong - cos stars can repeat!! 
    total = 0
    for star in cons[1]:
        total += star_mass(star)
    for con in cons[2]:
        total += total_mass(con)
    return total

def total_mass(cons): 
    total = 0
    for star in get_stars(cons):
        total += star_mass(star)
    return total







        

    
