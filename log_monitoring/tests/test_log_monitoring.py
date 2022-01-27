import log_monitoring.log_monitoring


def test_log():

    for i in range(1, 4):
        path = f"log_monitoring/tests/fixtures/input_{i}.txt"
        with open(path, "r") as log_file:
            correct = log_file.readline()[:-1]
            t, e = list(map(int, log_file.readline().split()))
            log = log_file.read().split("\n")
        assert log_monitoring.log_monitoring.l_m(t, e, log) == correct
