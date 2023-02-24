possible_birthdays = (('May', '15'),
                      ('May', '16'),
                      ('May', '19'),
                      ('June', '17'),
                      ('June', '18'),
                      ('July', '14'),
                      ('July', '16'),
                      ('August', '14'),
                      ('August', '15'),
                      ('August', '17'))

# Albert and Bernard just became friends with Cheryl,
# and they want to know when her birthday is.
# Cheryl gave Albert and Bernard a tuple of 10 possible dates.

#############
# Task 1(a) #
#############
# albert month
# bernard day
def unique_day(day, possible_birthdays): return len(tuple(d for m,d in possible_birthdays if d==day))==1
def unique_month(month, possible_birthdays): return len(tuple(m for m,d in possible_birthdays if m==month))==1
def contains_unique_day(month, possible_birthdays):
    return len(tuple(d for m,d in possible_birthdays if m == month and unique_day(d,possible_birthdays)))>0
#############
# Task 2(a) #
#############
def get_month(bday): return bday[0]
def get_day(bday): return bday[1]
# Albert (given month):
# I don't know Cheryl's birthday, but I know that Bernard doesn't know too.

def statement1(bday, possible_bdays):
    m = get_month(bday)
    return not unique_month(m,possible_bdays) and not contains_unique_day(m,possible_bdays)

# print("\n## Task 2a ##")
# print(statement1(('May', '19'), possible_birthdays)) # False
# print(statement1(('August', '14'), possible_birthdays)) # True

#############
# Task 2(b) #
#############

# Bernard (given day):
# At first I didn't know when Cheryl's birthday is, but I know now.

def statement2(birthday, possible_birthdays):
    return birthday in possible_birthdays and unique_day(get_day(birthday),possible_birthdays)

# print("\n## Task 2b ##")
# print(statement2(('May', '19'), possible_birthdays)) # True
# print(statement2(('August', '14'), possible_birthdays)) # False
# print(statement2(('August', '17'), possible_birthdays)) # False
# print(statement2(('July', '16'), possible_birthdays)) # False

#############
# Task 2(c) #
#############

# Albert (given month):
# Then I also know when Cheryl's birthday is.

def statement3(birthday, possible_birthdays):
    return birthday in possible_birthdays and unique_month(get_month(birthday), possible_birthdays)
    
# print("\n## Task 2c ##")
# print(statement3(('May', '19'), possible_birthdays)) # False
# print(statement3(('August', '14'), (('August', '14'),))) # True

##########
# Task 3 #
##########

# Based on statement 1, we can filter out some birthdays.
# From statement 2, we can filter out some more birthdays.
# Finally, using statement 3, we can filter out the remaining wrong birthdays.

def get_birthday(possible_birthdays):
    print("poss birthdays:",possible_birthdays)
    reduced_bday_set =  tuple(filter(lambda bday: statement1(bday,possible_birthdays),
                      possible_birthdays))
    print("statement1 reduc:",reduced_bday_set)
    reduced_bday_set_2 = tuple(filter(lambda bday: statement2(bday, reduced_bday_set),
                                      reduced_bday_set))
    print("statement2 reduc:",reduced_bday_set_2)
    reduced_bday_set_3 = tuple(filter(lambda bday: statement3(bday, reduced_bday_set_2),
                                      reduced_bday_set_2))
    print("statement3 reduc:",reduced_bday_set_3)
    return reduced_bday_set_3

# print("\n## Task 3 ##")
# print(get_birthday(possible_birthdays)) # (('July', '16'),)
