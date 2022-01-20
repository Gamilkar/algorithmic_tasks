from solutions.log_monitoring import log_monitoring


def test_log():

    for i in range(1, 4):
        path = f"test/log_monitoring_input/input_{i}.txt"
        with open(path, "r") as log_file:
            correct = log_file.readline()[:-1]
            t, e = list(map(int, log_file.readline().split()))
            log = log_file.read().split("\n")
        assert log_monitoring(t, e, log) == correct
