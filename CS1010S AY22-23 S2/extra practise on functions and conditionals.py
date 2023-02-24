

# Predefined helper functions. Do not edit them.
def time_to_seconds(time):
    x = list(map(int, time.split(":")))
    return x[0] * 3600 + x[1]*60 + x[2]

def make_time_string(hours, mins, seconds):
    return "{:02d}:{:02d}:{:02d}".format(hours, mins, seconds)



def time_difference(time1, time2):
    raw_diff = time_to_seconds(time2)-time_to_seconds(time1)
    h = raw_diff//3600
    ms = raw_diff%3600
    m = ms//60
    s = ms%60
    return make_time_string(h,m,s)
    
    
