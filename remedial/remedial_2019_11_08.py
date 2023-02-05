#******************************************************
#*
#*  CS1010S Make Up Practical Exam
#*  AY2014/2015, Semester 2
#*  Name: <fill in your name here>
#*
#*
#*  This template is to be used if Coursemology fails.
#*  Otherwise, answers should be uploaded to Coursemology
#*  directly. 
#*
#******************************************************

###
### Question 1
###

### Your answer here.


# Tests
def test_q1a():
    print(are_anagrams('dictionary', 'indicatory'))
    print(are_anagrams('listen', 'silent'))
    print(are_anagrams('test', 'exam'))
    print(are_anagrams('melon', 'watermelon'))

def test_q1b():
    print(has_anagrams(['apple', 'banana', 'pear', 'reap']))
    print(has_anagrams(['apple', 'banana', 'pear', 'papaya']))

def test_q1c():
    print(find_anagrams(['actress', 'grudge', 'recasts', 'rugged',
                         'casters', 'apple', 'pear', 'reap']))
    print(find_anagrams(['these', 'aren\'t', 'the', 'anagrams',
                         'you\'re', 'looking', 'for']))

    
# Uncomment to test question 1
#test_q1a()
#test_q1b()
#test_q1c()


###
### Question 2
###

### Your answer here.

import csv
def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of list
    containing rows in the csv file and its entries.
    """
    rows = []

    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows

def get_diff_or_none(column_num, data):
    roomdata = list(map(lambda row: row[column_num], data))
    roomdata = list(filter(lambda cell: cell.isdigit(), _3roomdata))
    roomdata = list(map(int, roomdata))
    if len(roomdata)>0:
        return max(roomdata) - min(roomdata)
    else:
        return None

def find_increase(filename, townname):
    # initialize dict for 3room, 4room, 5room, exec
    res = {"3room": None, "4room": None, "5room": None, "exec": None}
    # get rows from that particular town.
    data = read_csv(filename)[1:] # drop header
    data = list(filter(lambda row: row[2]==townname, data))
    res['3room'] = get_diff_or_none(3, data)
    res['4room'] = get_diff_or_none(4, data)
    res['5room'] = get_diff_or_none(5, data)
    res['exec'] = get_diff_or_none(6, data)
    return res

def get_town_avg_annual_price(col_num, data):
    town_price_pair = list(map(lambda row: [row[2], row[col_num]], data))
    town_price_pair = list(filter(lambda pair: pair[1].isdigit(), town_price_pair)) # clean up data
    town_price_pair = list(map(lambda pair: [pair[0], int(pair[1])], town_price_pair))
    res = {}
    for town, price in town_price_pair:
        if town not in res:
            res[town] = []
        res[town].append(price)
    # get average
    for town, ls_of_prices in res.items():
        res[town] = sum(ls_of_prices)/len(ls_of_prices)
    return res

def get_min_town(dict_of_town_price):
    minimum = min(dict_of_town_price.values())
    for town, price in dict_of_town_price.items():
        if price == minimum:
            return (town, minimum)

def cheapest_town(filename, year): 
    # initialize dict for each housing type
    res = {"3room": None, "4room": None, "5room": None, "exec": None}
    # get data for that year only (filter)
    data = read_csv(filename)[1:] # drop header
    data = list(filter(lambda row: int(row[0])==year, data))

    res['3room'] = get_min_town(get_town_avg_annual_price(3, data))
    res['4room'] = get_min_town(get_town_avg_annual_price(4, data))
    res['5room'] = get_min_town(get_town_avg_annual_price(5, data))
    res['exec'] = get_min_town(get_town_avg_annual_price(6, data))
    # for each housing type...
    #    get the average_annual_price per town (store as dict?)
    #    get the min average_annual_price
    #    add that tuple (town, annual_price) to dict
    # return dict
    return res

# Tests
def test_q2a():
    print(find_increase('hdb-resale-prices.csv', 'Ang Mo Kio'))
    print(find_increase('hdb-resale-prices.csv', 'Jurong East'))

def test_q2b():
    print(cheapest_town('hdb-resale-prices.csv', 2011))
    #print(cheapest_town('hdb-resale-prices.csv', 2013))


# Uncomment to test question 2
#test_q2a()
test_q2b()

###
### Question 3
###

### Your answer here.
class Trainer:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
        self.dragon = None # stores the dragon object that is currently mounted
        self.dragons = {} # stores the dragons that I have tried to train
        # {dragon1_obj: 0, dragon2_obj: 3}
        # dragon1 is trained, but dragon2 needs 3 more attempts

    def trained_dragons(self):
        # returns a tuple of the names of dragons I trained successfully
        trained = ()
        for dragon_obj, v in self.dragons.items():
            if v == 0:
                trained += (dragon_obj.name,) # get name from dragon object
        return trained

    def dismount(self):
        if self.dragon is None:
            return self.name + " is not mounted"
        else:
            dragon = self.dragon
            self.dragon = None         # set self.dragon to None
            dragon.trainer = None     # set the dragon's trainer to None
            return self.name + " dismounts from " + dragon.name

    def is_trained(self, dragon):
        return dragon in self.dragons and self.dragons[dragon] == 0

    def mount(self, dragon):
        if self.dragon is not None:
            return self.name + " is currently mounted on " + self.dragon.name
        elif dragon.trainer is not None:
            return dragon.trainer.name + " is currently mounted on " + dragon.name
        elif not self.is_trained(dragon):
            return self.name + " has not yet trained " + dragon.name
        else:
            self.dragon = dragon
            dragon.trainer = self
            return self.name + " mounts " + dragon.name

    def train(self, dragon):
        if self.is_trained(dragon):
            return dragon.name + " has already been trained"

        if dragon not in self.dragons:
            self.dragons[dragon] = dragon.skill - self.skill + 1

        self.dragons[dragon] = max(0, self.dragons[dragon]-1)

        if self.dragons[dragon] == 0:
            dragon.trainers.append(self)
            return self.name + " successfully trained " + dragon.name
        else:
            return self.name + " failed to train " + dragon.name

class Dragon:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
        self.trainer = None
        self.trainers = []
        # when i get trained successfully, I need to include that trainer into this list
    def get_trainers(self):
        return tuple(map(lambda t: t.name, self.trainers))
    def fly(self):
        if self.trainer is None:
            return self.name + " does not have a rider"
        else:
            return self.name + " flies around with " + self.trainer.name

# Tests
def test_q3():
        toothless = Dragon("Toothless", 7)
        meatlug = Dragon("Meatlug", 1)
        stormfly = Dragon("Stormfly", 5)
        
        hiccup = Trainer("Hiccup", 4)
        astrid = Trainer("Astrid", 5)
        
        print(astrid.train(stormfly) == 'Astrid successfully trained Stormfly')
        print(astrid.mount(stormfly) == 'Astrid mounts Stormfly')
        print(stormfly.fly() == 'Stormfly flies around with Astrid')

        print(meatlug.fly() == 'Meatlug does not have a rider')
        print(hiccup.mount(meatlug) == 'Hiccup has not yet trained Meatlug')
        print(hiccup.train(meatlug) == 'Hiccup successfully trained Meatlug')
        print(hiccup.train(meatlug) == 'Meatlug has already been trained')
        print(hiccup.mount(meatlug) == 'Hiccup mounts Meatlug')
        print(meatlug.fly() == 'Meatlug flies around with Hiccup')
                      
        print(hiccup.mount(stormfly) == 'Hiccup is currently mounted on Meatlug')
        print(hiccup.dismount() == 'Hiccup dismounts from Meatlug')
        print(hiccup.mount(stormfly) == 'Astrid is currently mounted on Stormfly')
        print(astrid.dismount() == 'Astrid dismounts from Stormfly')
        print(hiccup.mount(stormfly) == 'Hiccup has not yet trained Stormfly')

        print(astrid.trained_dragons() == ('Stormfly',))
        print(hiccup.trained_dragons() == ('Meatlug',))
        print(stormfly.get_trainers() == ('Astrid',))
        print(hiccup.train(stormfly) == 'Hiccup failed to train Stormfly')
        print(hiccup.train(stormfly) == 'Hiccup successfully trained Stormfly')
        print(sorted(stormfly.get_trainers()) == sorted(('Astrid', 'Hiccup')))

        print(hiccup.train(toothless) == 'Hiccup failed to train Toothless')
        print(hiccup.train(toothless) == 'Hiccup failed to train Toothless')
        print(hiccup.train(toothless) == 'Hiccup failed to train Toothless')
        print(hiccup.train(toothless) == 'Hiccup successfully trained Toothless')
        print(hiccup.mount(toothless) == 'Hiccup mounts Toothless')
        print(toothless.fly() == 'Toothless flies around with Hiccup')
        print(sorted(hiccup.trained_dragons()) == sorted(('Meatlug', 'Stormfly', 'Toothless')))

# Uncomment to test question 3
test_q3()

###
### Question 4
###

### Your answer here.


# Tests
def test_q4():
    print(bomb_blast(6, 5,
                     ((1, 1), (3, 1), (3, 3), (5, 4)),
                     ((3, 0), (4, 2), (1, 3)),
                     0) == 12)          
    print(bomb_blast(6, 7,
                     ((1, 1), (4, 1), (1, 5), (4, 5)),
                     ((2, 5),),
                     1) == 12)

# Uncomment to test question 4
#test_q4()
