import time


class Constants:
    MAP_SIZE = [16000, 900]
    CHECKPOINT_RADIUS = 600
    TIME_LIMIT_FIRST_TURN = 1000
    TIME_LIMIT = 150
    THRUST_MAX = 100
    POD_RADIUS = 400


class Profiler:
    start = None
    full_time = None
    profiler = 0

    def __init__(self):
        self.start = time.time()

    def start_timer(self):
        self.start = time.time()

    def stop_timer(self):
        self.full_time = time.time() - self.start

    def get_time(self, round_value=5):
        return round(time.time() - self.start, round_value)

    def add_timer(self):
        self.profiler += time.time() - self.start





