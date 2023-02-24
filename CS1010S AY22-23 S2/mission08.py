from ippt import *
import csv

##########
# Task 1 #
##########

# Function read_csv has been given to help you read the csv file.
# The function returns a tuple of tuples containing rows in the csv
# file and its entries.

# Alternatively, you may use your own method.

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows

def read_data(filename):
    rows = read_csv(filename)
    data = tuple(map(lambda x: int(x), row[1:]) for row in rows[1:])
    age_keys = tuple(int(row[0]) for row in rows[1:])
    rep_keys = tuple(int(i) for i in rows[0][1:])
    return create_table(data, age_keys, rep_keys)

pushup_table = read_data("pushup.csv")
situp_table = read_data("situp.csv")
run_table = read_data("run.csv")

ippt_table = make_ippt_table(pushup_table, situp_table, run_table)

##########
# Task 2 #
##########
from math import ceil
def keep_in_range(start,end,x):
    if start<=end:
        if x<start: return start
        elif x>end: return end
        else: return x
    else:
        raise Exception("Wat kind of reverse ranges are u putting in? Increasing order pls!")
def pushup_score(pushup_table,age, pushup):
    return access_cell(pushup_table,keep_in_range(18,60,age),keep_in_range(1,60,pushup))
def situp_score(situp_table, age, situp):
    return access_cell(situp_table,keep_in_range(18,60,age),keep_in_range(1,60,situp))
def run_score(run_table, age, run):
    return access_cell(run_table,keep_in_range(18,60,age),keep_in_range(510,1110,10*ceil(run/10)))

##########
# Task 3 #
##########

def ippt_award(score):
    if   score < 51: return "F"
    elif score < 61: return "P"
    elif score < 75: return "P$"
    elif score < 85: return "S"
    else:            return "G"

##########
# Task 4 #
##########

def ippt_results(ippt_table, age, pushup, situp, run):
    score = pushup_score(get_pushup_table(ippt_table),age,pushup) \
            + situp_score(get_situp_table(ippt_table),age,situp) \
            + run_score(get_run_table(ippt_table),age,run)
    award = ippt_award(score)
    return (score,award)
    

# print("## Q4 ##")
# print(ippt_results(ippt_table, 25, 30, 25, 820))      # (53, 'P')
# print(ippt_results(ippt_table, 28, 56, 60, 530))      # (99, 'G')
# print(ippt_results(ippt_table, 38, 18, 16, 950))      # (36, 'F')
# print(ippt_results(ippt_table, 25, 34, 35, 817))      # (61, 'P$')
# print(ippt_results(ippt_table, 60, 70, 65, 450))      # (100, 'G')


##########
# Task 5 #
##########
def make_training_program(rate_pushup, rate_situp, rate_run):
    def training_program(ippt_table, age, pushup, situp, run, days):
        improved_pushup = pushup + days//rate_pushup if rate_pushup != 0 else pushup
        improved_situp =   situp + days//rate_situp  if rate_situp  != 0 else situp
        improved_run =       run - days//rate_run    if rate_run    != 0 else run
        return (improved_pushup,improved_situp,improved_run,ippt_results(ippt_table,age,improved_pushup,improved_situp,improved_run))

    return training_program

# print("## Q5 ##")
tp = make_training_program(7, 3, 10)
# print(tp(ippt_table, 25, 30, 25, 820, 30))        # (34, 35, 817, (61, 'P$'))


##########
# Bonus  #
##########
# I wouldn't program it anything like with the given data structures at all, hence this is some monster code:
def make_tp_bonus(rate_pushup, rate_situp, rate_run):
    tp_p = make_training_program(rate_pushup,0,0)
    tp_s = make_training_program(0,rate_situp,0)
    tp_r = make_training_program(0,0,rate_run)
    
    def tp_bonus(ippt_table, age, pushup, situp, run, days):
        print(f"new day new me, days={days}")
        p_res,s_res,r_res = 0,0,0
        curr_score,_ = ippt_results(ippt_table,age,pushup,situp,run)
        print("current score:", curr_score)
        for d in range(1,days+1):
            im_p,_,_,(score_p,_) = tp_p(ippt_table,age,pushup,situp,run,d)
            _,im_s,_,(score_s,_) = tp_s(ippt_table,age,pushup,situp,run,d)
            _,_,im_r,(score_r,_) = tp_r(ippt_table,age,pushup,situp,run,d)

            # get number of days invested at the first change of score
            # and the change in score, and calculate time efficiency based on that.
            # I know this may not account for cases where the beginning pushup,situp and run scores are too low.
            if score_p != curr_score and p_res == 0: p_res = ((score_p-curr_score),d,im_p)
            if score_s != curr_score and s_res == 0: s_res = ((score_s-curr_score),d,im_s)
            if score_r != curr_score and r_res == 0: r_res = ((score_r-curr_score),d,im_r)
            
        
        res = (p_res,s_res,r_res)
        eff = map(lambda re:re[0]/re[1] if re != 0 and re[1] != 0 else 0,
                  res)
        print("res:",res,"eff:",eff)
        best_i,best_eff = max(enumerate(eff),key=lambda x:x[1])
        print("best_i:",best_i,"best_eff:",best_eff,"res[best_i]:",res[best_i])
        if tuple(filter(lambda x:x,res)) == (): return (pushup,situp,run,ippt_results(ippt_table,age,pushup,situp,run))
        _,d,im_b = res[best_i]
        if best_i == 0: return tp_bonus(ippt_table,age,im_b,situp,run,days-d)
        if best_i == 1: return tp_bonus(ippt_table,age,pushup,im_b,run,days-d)
        if best_i == 2: return tp_bonus(ippt_table,age,pushup,situp,im_b,days-d)
    return tp_bonus

tp_bonus = make_tp_bonus(7, 3, 10)

# Note: Depending on your implementation, you might get a different number of
# sit-up, push-up, and 2.4km run timing. However, the IPPT score and grade
# should be the same as the sample output.

print(tp_bonus(ippt_table, 25, 20, 30, 800, 30))      # (20, 40, 800, (58, 'P'))
print(tp_bonus(ippt_table, 25, 20, 30, 800, 2))       # (20, 30, 800, (52, 'P'))
