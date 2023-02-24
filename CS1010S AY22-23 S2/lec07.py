list1 = [1] * 4
list2 = [5, 5, 5]
while True:
    list1[0] += 1
    if list1[0] == 5: 
         break
    list1[2] += 3
5,1,10,1
5,5,5
print(list1 < list2)
print(list2 == (5, 5, 5))

def remove_extras(l):
    if l == []: return []
    lst = l[-1]
    b4_lst = l[:-1]
    if lst in b4_lst: return remove_extras(b4_lst)
    else: return remove_extras(b4_lst) + [lst]

def remove_extras(l):
    new = list(set(l))
    l.clear()
    l.extend(new)
    return l

def count_occurrences(lst, num):
    if type(lst) is not list: return 1 if lst == num else 0
    return sum(count_occurrences(i) for i in lst)

def sort(l,comparator=(lambda x,y: x<y):, key=lambda x:x):
    
def sort_age(l):
    
