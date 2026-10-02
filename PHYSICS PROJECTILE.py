import math
import matplotlib.pyplot as pt
def draw_graph(total_velocity,angle_d):
    g=9.8
    t=0
    h=0
    x_coordinate=[]
    y_coordinate=[]
    angle=math.radians(angle_d)
    forward_velocity=total_velocity*math.cos(angle)
    upward_velocity=total_velocity*math.sin(angle)

    time_of_flight = (2 * total_velocity * math.sin(angle)) / g
    max_height = ((total_velocity ** 2) * (math.sin(angle) ** 2)) / (2 * g)
    total_range = ((total_velocity ** 2) * math.sin(2 * angle)) / g
    
    while h>=0:
        h=(upward_velocity*t)-(0.5*g*(t**2))
        forward_distance=forward_velocity*t
        if h>=0:
            x_coordinate.append(forward_distance)
            y_coordinate.append(h)
        t+=0.01
    pt.plot(x_coordinate,y_coordinate,color='green')
    pt.text(0, 5, f"Time: {time_of_flight:.2f}s")
    pt.text(0, 4, f"Max Height: {max_height:.2f}m")
    pt.text(0, 3, f"Range: {total_range:.2f}m")   
    pt.title("PHYSICS PROJECTILE")
    pt.xlabel("FORWARD DISTANCE IN METRE")
    pt.ylabel("UPWARD DISTANCE IN METRE")
    pt.show()

print("--- PHYSICS PROJECTILE MOTION SIMULATOR ---")

velocity=float(input("Enter velocity (u) (in m/s): "))
user_angle=float(input("Enter angle (degree): "))
draw_graph(velocity,user_angle)