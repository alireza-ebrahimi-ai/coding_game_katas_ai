import math


class Point:
    x = None
    y = None

    def __init__(self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y

    def distance_to(self, point):
        return math.hypot(abs(self.x - point.x), abs(self.y - point.y))


class Unit(Point):
    id = None
    radius = None
    vx = None
    vy = None


class Checkpoint(Unit):
    def bounce(self):
        pass


class Pod(Unit):
    angle = None
    next_checkpoint_id = None
    checked = None
    timeout = False
    shield = False

    def get_angle(self, point):
        # 0 - east, 90 - south, 180 - west, 270 - north

        distance = self.distance_to(point)
        dx = (point.x - self.x) / distance
        dy = (point.y - self.y) / distance

        # we multiply by 180.0 / PI to convert radians to degrees.
        a = math.acos(dx) * 180.0 / math.pi

        # if the point below - shift the angle
        if dy < 0:
            a = 360.0 - a

        return a

    def diff_angle(self, point):
        pass

    def rotate(self, point):
        pass

    def boost(self, thrust):
        pass

    def move(self, thrust):
        pass

    def output(self):
        pass

    def bounce(self):
        pass


class Emulator:

    simulated_pod_hero = None
    simulated_pod_enemy = None
    checkpoint = None

    def __init__(self, pod_1, pod_2, checkpoints):
        self.simulated_pod_hero = pod_1
        self.simulated_pod_enemy = pod_2

    def emulate(self):
        pass





















