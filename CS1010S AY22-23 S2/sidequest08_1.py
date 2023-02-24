from planets import *
from math import sin,cos,pi
# Task 1a
# Follows trigonometry angle.
# E.g. 0 degree -> East
# E.g. 90 degree -> North
def get_velocity_component(angle_deg, velocity):
    angle_rad = angle_deg/180 * pi
    return (velocity*cos(angle_rad),velocity*sin(angle_rad))
# print(get_velocity_component(30, 50)) # (43.30127018922194, 24.999999999999996)
# note that the exact values of each component may differ slightly due to differences in precision
# get_velocity_component(90, 10) # (0,10)
# Task 1b
def pythagorean_distance(x,y): return sqrt(x**2 + y**2)
def calculate_total_acceleration(planets, current_x, current_y):
    ax,ay = 0,0
    for planet in planets:
        p_x,p_y = get_position(planet)
        M = get_mass(planet)
        r = pythagorean_distance(current_x-p_x,current_y-p_y)
        ax += G*M*(p_x-current_x)/(r**3)
        ay += G*M*(p_y-current_y)/(r**3)
    return (ax,ay)
# print(calculate_total_acceleration(planets, 0.1, 0.1)) # (-1423.6113504393045, -1425.4297228686778)
# Task 1c
def f(t, Y):
    [rx,ry,vx,vy] = Y
    (ax,ay) = calculate_total_acceleration(planets,rx,ry)
    return np.array([vx, vy, ax, ay]) # Do not change the return statement
np.set_printoptions(precision=5)
# print(f(0.5, [0.1, 0.1, 15.123, 20.211])) # [15.123  20.211  -1423.61135  -1425.42972]

# Task 2, change the input parameters to alter the path of the spacecraft
def mission_results(angle_deg, velocity):
    vx, vy = get_velocity_component(angle_deg,velocity)

    def rungekutta4(f, y0, t):
        n = len(t)
        y = np.zeros((n, len(y0)))
        y[0] = y0
        for i in range(n - 1):
            h = t[i+1] - t[i]
            k1 = f(t[i], y[i])
            k2 = f(t[i] + h / 2., y[i] + k1 * h / 2.)
            k3 = f(t[i] + h / 2., y[i] + k2 * h / 2.)
            k4 = f(t[i] + h, y[i] + k3 * h)
            y[i+1] = y[i] + (h / 6.) * (k1 + 2*k2 + 2*k3 + k4)
        return y

    t0 = 0    # Initial Time
    dt = 1e-3    # Iteration speed

    # Vector with the spacecraft's initial position and speed
    y0 = np.array([0.1, 0, vx, vy])
    t = np.arange(0, 400*dt, dt)
    final_path = rungekutta4(f, y0, t)
    # print(final_path)
    
    mars_passed, earth_reached, moon_compromised = False, False, False
    path_x, path_y = [], []
    counter = 0

    while(1):
        day = round(1000*t0)
        current_x = final_path[counter][0]
        current_y = final_path[counter][1]
        counter += 1
        if day >= 365:
            # print("Simulation stopped! You ran out of time :(")
            break
        elif not (X_RANGE[0] - 0.2 <= current_x <= X_RANGE[1] + 0.2) or not (Y_RANGE[0] - 0.2 <= current_y <= Y_RANGE[1] + 0.2):
            # print("Simulation stopped! You are out of bounds!")
            break
        elif mars_passed and earth_reached and not moon_compromised:
            # print("Simulation finished! Good job!")
            print(f"inputs: are angle_deg,v_i={angle_deg},{velocity}")
            return True
        elif moon_compromised:
            # print("Simulation stopped! You hit the Moon's vicinity!")
            break
        elif (current_x - get_x_coordinate(Mars))**2 + (current_y - get_y_coordinate(Mars))**2 <= 0.034**2:
            # print("Simulation stopped! You crashed on Mars!")
            break
        elif (current_x - get_x_coordinate(Moon))**2 + (current_y - get_y_coordinate(Moon))**2 <= 0.018**2:
            # print("Simulation stopped! You crashed on the Moon!")
            break
        elif not mars_passed and (current_x - get_x_coordinate(Earth))**2 + (current_y - get_y_coordinate(Earth))**2 <= 0.025**2:
            # print("Simulation stopped! You crashed on the Earth!")
            break
        else:
            if not mars_passed and (current_x - get_x_coordinate(Mars))**2 + (current_y - get_y_coordinate(Mars))**2 <= 0.05**2:
                mars_passed = True
            if mars_passed and (current_x - get_x_coordinate(Earth))**2 + (current_y - get_y_coordinate(Earth))**2 <= 0.025**2:
                earth_reached = True
            elif mars_passed and (current_x - get_x_coordinate(Moon))**2 + (current_y - get_y_coordinate(Moon))**2 <= 0.07**2:
                moon_compromised = True
            path_x = (path_x + [current_x])[-50:]
            path_y = (path_y + [current_y])[-50:]
        t0 += dt
    return False

    
    

deg_anglee, initial_velocityy = 295.2,26.4
anim = setup_spacecraft(*get_velocity_component(deg_anglee,initial_velocityy),f)
# anim.save(f"sidequest08_1 {deg_anglee} {initial_velocityy}.gif", fps=30)
plt.show()

angle_deg_start = 180
angle_deg_end = 360
v_i_start = 40
v_i_end = 100
a_n = 1000
v_n = 100
def percentage_of_way_there(percentage,start,end):
    diff = end-start
    return start + diff*percentage 

for a in range(a_n):
    print(a)
    for v in range(v_n):
        mission_results(percentage_of_way_there(a/a_n, angle_deg_start,angle_deg_end),
                        percentage_of_way_there(v/v_n, v_i_start,v_i_end))

# inputs: are angle_deg,v_i=113.76,26.6
# inputs: are angle_deg,v_i=114.12,26.6
# inputs: are angle_deg,v_i=288.36,26.2
# inputs: are angle_deg,v_i=288.36,26.4
# inputs: are angle_deg,v_i=288.72,26.2
# inputs: are angle_deg,v_i=288.72,26.4
# inputs: are angle_deg,v_i=289.08000000000004,26.2
# inputs: are angle_deg,v_i=289.44,26.2
# inputs: are angle_deg,v_i=290.52000000000004,26.2
# inputs: are angle_deg,v_i=291.6,26.2
# inputs: are angle_deg,v_i=291.96000000000004,26.2
# inputs: are angle_deg,v_i=295.2,26.4


# working out the ranges...
# angle_deg,v_i =
#    113.76 to 114.12, 26.6
# OR 288.36, 26.2 to 26.4
# OR 288.72, 26.2 to 26.4
# OR 289.08 to 289.44, 26.2
# OR 290.52,26.2
# OR 291.6 to 291.96,26.2
# OR 295.2,26.4
