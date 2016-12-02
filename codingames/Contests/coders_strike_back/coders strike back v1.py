import sys
import math

#MAGIC CONSTANTS:
ANGLE_ROTATION = 18
SPEED_DECREASE = 0.85
MINIMUM_SPEED_FOR_BRAKE_PATH = 44
THRUSTER_TO_1 = 3.9
STOP_ANGLE = 18
FIELD_ACTIVATE = 1000
FIELD_ANGLE = 90
SPEED_DEL = 0.5 

#--------------------------------
#linear -OK
def distance(x, y, pod_x, pod_y): 
    return round(math.sqrt((x-pod_x)*(x-pod_x) + (y-pod_y)*(y-pod_y)))

#angle to checkpoint -OK   
def angle_to_checkpoint(pod_x, pod_y, checkpoint_x, checkpoint_y):
    d = distance(checkpoint_x, checkpoint_y, pod_x, pod_y)
    raw_angle = abs(round(math.degrees(math.asin(abs(pod_y - checkpoint_y) / d))))
    if (pod_x - checkpoint_x) < 0 and (pod_y - checkpoint_y) < 0:
        return raw_angle
    if (pod_x - checkpoint_x) >= 0 and (pod_y - checkpoint_y) < 0:
        return 180 - raw_angle
    if (pod_x - checkpoint_x) >= 0 and (pod_y - checkpoint_y) >= 0:
        return raw_angle + 180
    if (pod_x - checkpoint_x) < 0 and (pod_y - checkpoint_y) >= 0:
        return 360 - raw_angle
              
# brake path seems -OK        
def path_to_stop(vx, vy):
    #print >> sys.stderr, "Current VX: " + str(vx)
    #print >> sys.std   err, "Current VY: " + str(vy)
    
    vr = math.sqrt(abs(vx * vx) + abs(vy * vy)  + 2 * abs(vx) * abs(vy))
    #print >> sys.stderr, "Current VR: " + str(vr)
    
    path = 0
    while vr > MINIMUM_SPEED_FOR_BRAKE_PATH:
        path = path + vr
        vr = vr * SPEED_DECREASE
    return round(path)            
#no    
def x_correction(angle, pod_x, pod_y, checkpoint_x, checkpoint_y):
    angle_target = angle_to_checkpoint(pod_x, pod_y, checkpoint_x, checkpoint_y)
    angle_diff = angle_target - angle
    angle_diff = (angle_diff + 180) % 360 - 180
    
    #print >> sys.stderr, "Angle difference: " + str(angle_diff)
    
    if angle_diff < -15:
        return 350
    if angle_diff > 15:
        return -350
    return 0


#no         
def y_correction(angle, pod_x, pod_y, checkpoint_x, checkpoint_y):
    angle_target = angle_to_checkpoint(pod_x, pod_y, checkpoint_x, checkpoint_y)
    angle_diff = angle_target - angle
    angle_diff = (angle_diff + 180) % 360 - 180
    
    if angle_diff < -15:
        return 350
    if angle_diff > 15:
        return -350
    return 0

# -OK
def touch_down(pod_x, pod_y, checkpoint_x, checkpoint_y, angle, vx, vy):
    distance_to_checkpoint = distance(checkpoint_x, checkpoint_y, pod_x, pod_y)
    stops_in = path_to_stop(vx, vy)
    angle_checkpoint = angle_to_checkpoint(pod_x, pod_y, checkpoint_x, checkpoint_y)
    
    if distance_to_checkpoint < (stops_in / THRUSTER_TO_1):
        if (abs(angle - angle_checkpoint) < 18) or (abs(angle - angle_checkpoint) > 342):
            return True 
        
    return False

# only coordinats check and simply speed check here 
def collision(x, y, enemy_x, enemy_y, vx, vy, enemy_vx, enemy_vy, angle, enemy_angle):
    next_enemy_x = enemy_vx + enemy_x
    next_enemy_y = enemy_vy + enemy_y
    my_next_x = x + vx
    my_next_y = y + vy
    if abs(vx + vy) < 2:
        return False
    if (abs(angle - enemy_angle) > 45):
        if (abs(my_next_x - next_enemy_x) < 800) and (abs(my_next_y - next_enemy_y) < 800):
            return True    
   
    return False

#-------------------------------------
laps = int(raw_input())
checkpoint_count = int(raw_input())
checkpoints = 0

my_checkpoint_x = []
my_checkpoint_y = []

for i in xrange(checkpoint_count):
    checkpoint_x, checkpoint_y = [int(j) for j in raw_input().split()]
    my_checkpoint_x.append(checkpoint_x)
    my_checkpoint_y.append(checkpoint_y)

while True:
    my_pod_x = []
    my_pod_y = [] 
    my_pod_vx = []
    my_pod_vy = []
    my_pod_angle = []
    pods_checkpoint = []
    enemy_pod_x = []
    enemy_pod_y = []
    enemy_pod_vx = []
    enemy_pod_vy = []
    enemy_pod_angle = []
    
    for i in xrange(2):
        x, y, vx, vy, angle, nextCheckPointId = [int(j) for j in raw_input().split()]
        my_pod_x.append(x)
        my_pod_y.append(y)
        my_pod_vx.append(vx)
        my_pod_vy.append(vy)
        my_pod_angle.append(angle)
        pods_checkpoint.append(nextCheckPointId)        
    for i in xrange(2):
        x, y, vx, vy, angle, next_check_point_id = [int(j) for j in raw_input().split()]
        enemy_pod_x.append(x)
        enemy_pod_y.append(y)
        enemy_pod_vx.append(vx)
        enemy_pod_vy.append(vy)
        enemy_pod_angle.append(angle)
        
    #print >> sys.stderr, "Angle to checkpoint: " + str(angle_to_checkpoint(my_pod_x[0], my_pod_y[0], my_checkpoint_x[pods_checkpoint[0]], my_checkpoint_y[pods_checkpoint[0]]))
    #print >> sys.stderr, "My pod[0] angle: " + str(my_pod_angle[0])
    #print >> sys.stderr, "Brake path for pod[0]: " + str(path_to_stop(my_pod_vx[0], my_pod_vy[0]))
    #print >> sys.stderr, "----------------------"  
    
#---------------------- POD 1 ----------------------            

    x0 = my_checkpoint_x[pods_checkpoint[0]]
    y0 = my_checkpoint_y[pods_checkpoint[0]]
    coordinate_x_diff = 0
    coordinate_y_diff = 0
    
    if my_checkpoint_x[pods_checkpoint[0]] == my_checkpoint_x[checkpoint_count - 1]:
        next_x0 = my_checkpoint_x[0]
        next_y0 = my_checkpoint_y[0]
    else:
        next_x0 = my_checkpoint_x[pods_checkpoint[0] + 1]
        next_y0 = my_checkpoint_y[pods_checkpoint[0] + 1]   
    
    distance_pod0 = distance(my_checkpoint_x[pods_checkpoint[0]], my_checkpoint_y[pods_checkpoint[0]], my_pod_x[0], my_pod_y[0])
    thruster1 = 200
            
    coordinate_x_diff = x_correction(my_pod_angle[0], my_pod_x[0], my_pod_y[0], my_checkpoint_x[pods_checkpoint[0]], my_checkpoint_y[pods_checkpoint[0]])
    coordinate_y_diff = y_correction(my_pod_angle[0], my_pod_x[0], my_pod_y[0], my_checkpoint_x[pods_checkpoint[0]], my_checkpoint_y[pods_checkpoint[0]])
    
    #print >> sys.stderr, "Current X_change: " + str(coordinate_x_diff)
    #print >> sys.stderr, "Current Y_change: " + str(coordinate_y_diff)
    
    #x0 = x0 + coordinate_x_diff
    #y0 = y0 + coordinate_y_diff
    
    if abs(my_pod_angle[0] - angle_to_checkpoint(my_pod_x[0], my_pod_y[0], my_checkpoint_x[pods_checkpoint[0]], my_checkpoint_y[pods_checkpoint[0]])) > STOP_ANGLE:
        thruster1 = 10
        
    if touch_down(my_pod_x[0], my_pod_y[0], my_checkpoint_x[pods_checkpoint[0]], my_checkpoint_y[pods_checkpoint[0]], my_pod_angle[0], my_pod_vx[0], my_pod_vy[0]):
        thruster1 = 25
        x0 = next_x0
        y0 = next_y0    
        
    if collision(my_pod_x[0], my_pod_y[0], enemy_pod_x[0], enemy_pod_y[0], my_pod_vx[0], my_pod_vy[0], enemy_pod_vx[0], enemy_pod_vy[0], my_pod_angle[0],  enemy_pod_angle[0]):
        thruster1 = "SHIELD BOOM"
    if collision(my_pod_x[0], my_pod_y[0], enemy_pod_x[1], enemy_pod_y[1], my_pod_vx[0], my_pod_vy[0], enemy_pod_vx[1], enemy_pod_vy[1], my_pod_angle[0],  enemy_pod_angle[1]):
        thruster1 = "SHIELD BOOM"

    print str(x0) + " " +  str(y0) + " " + str(thruster1)
    
   
#---------------------- POD 2 ----------------------    

    x1 = my_checkpoint_x[pods_checkpoint[1]]
    y1 = my_checkpoint_y[pods_checkpoint[1]]
    
    if my_checkpoint_x[pods_checkpoint[1]] == my_checkpoint_x[checkpoint_count - 1]:
        next_x1 = my_checkpoint_x[1]
        next_y1 = my_checkpoint_y[1]
    else:
        next_x1 = my_checkpoint_x[pods_checkpoint[1] + 1]
        next_y1 = my_checkpoint_y[pods_checkpoint[1] + 1]   
    
    distance_pod1 = distance(my_checkpoint_x[pods_checkpoint[1]], my_checkpoint_y[pods_checkpoint[1]], my_pod_x[1], my_pod_y[1])
    thruster2 = 200
            
    if abs(my_pod_angle[1] - angle_to_checkpoint(my_pod_x[1], my_pod_y[1], my_checkpoint_x[pods_checkpoint[1]], my_checkpoint_y[pods_checkpoint[1]])) > STOP_ANGLE:
        thruster2 = 10
        
    if touch_down(my_pod_x[1], my_pod_y[1], my_checkpoint_x[pods_checkpoint[1]], my_checkpoint_y[pods_checkpoint[1]], my_pod_angle[1], my_pod_vx[1], my_pod_vy[1]):
        thruster2 = 25
        x1 = next_x1
        y1 = next_y1  
        
    if collision(my_pod_x[1], my_pod_y[1], enemy_pod_x[0], enemy_pod_y[0], my_pod_vx[1], my_pod_vy[1], enemy_pod_vx[0], enemy_pod_vy[0], my_pod_angle[1],  enemy_pod_angle[0]):
        thruster2 = "SHIELD BOOM"
    if collision(my_pod_x[1], my_pod_y[1], enemy_pod_x[1], enemy_pod_y[1], my_pod_vx[1], my_pod_vy[1], enemy_pod_vx[1], enemy_pod_vy[1], my_pod_angle[1],  enemy_pod_angle[1]):
        thruster2 = "SHIELD BOOM"

    print str(x1) + " " +  str(y1) + " " + str(thruster2)

     
          