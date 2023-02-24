SIZE = 9

board = ((5, 3, 4, 6, 7, 8, 9, 1, 2),
(6, 0, 2, 1, 9, 0, 3, 4, 0),
(1, 9, 8, 3, 4, 2, 0, 6, 7),
(8, 5, 9, 7, 6, 1, 4, 2, 3),
(4, 2, 0, 8, 5, 3, 7, 9, 1),
(7, 1, 3, 9, 2, 4, 8, 5, 6),
(9, 6, 1, 0, 3, 7, 2, 8, 4),
(2, 8, 7, 4, 1, 9, 6, 0, 5),
(3, 4, 5, 2, 8, 6, 1, 7, 9))


def get_column(board,col):
        full_c = []
        for row in board:
            full_c.append(row[col])
        return full_c
def easy_sudoku(x, y, n):
    if n in board[x-1] + tuple(get_column(board,y-1)): return "Violation"
    return "No violation"


def car(odo,dists):
    final_odometer_value = round(sum(dists+(odo,))%1000,1) # bruh to past test case, u need to modulo by 1000 instead of 999.9?!??!
    total_number_of_trips = len(dists)
    avg_dist_per_trip = round(sum(dists)/total_number_of_trips,1) if total_number_of_trips>0 else 0
    max_diff_between_two_consecutive_trips = round(max(abs(dists[i+1]-dists[i]) for i in range(total_number_of_trips-1)), 1) if total_number_of_trips>=2 else 0
    return (final_odometer_value,
            total_number_of_trips,
            avg_dist_per_trip,
            max_diff_between_two_consecutive_trips)


def flatten_tuple(tup):
    if type(tup) is not tuple: return (tup,)
    return sum(tuple(flatten_tuple(i) for i in tup),())
        
def check_matrix(matrix):
    flat = list(flatten_tuple(matrix))
    return flat == sorted(flat)
