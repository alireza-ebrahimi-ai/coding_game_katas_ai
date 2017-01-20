from codingame.multiplayer.CSB.src.server import Server
from codingame.multiplayer.CSB.src.emulator import Emulator, Pod, Point

csb_server = Server()
csb_pod = Pod(3200, 3200)
# csb_emulator = Emulator()

def test_001():
    assert 1 == 1


def test_pod_get_angle():
    # 0 - east, 90 - south, 180 - west, 270 - north
    test_point = Point(3400, 3200)
    assert csb_pod.get_angle(test_point) == 0
    test_point = Point(3000, 3200)
    assert csb_pod.get_angle(test_point) == 270
    test_point = Point(3200, 3200)
    assert csb_pod.get_angle(test_point) == 270
