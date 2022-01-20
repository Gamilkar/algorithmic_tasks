import datetime


def log_monitoring(t, e, log):
    interval = datetime.timedelta(seconds=t)
    result = -1
    errors = []
    for line in log:
        status = line[22:27]
        if status == "ERROR":
            date = datetime.datetime.strptime(line[1:20], "%Y-%m-%d %H:%M:%S")
            errors.append(date)
            if len(errors) == e:
                if errors[-1] < errors[0] + interval:
                    result = date
                    break
                errors.pop(0)
    return str(result)


with open("test_2.txt", "r") as log_file:
    t, e = list(map(int, log_file.readline().split()))
    log = log_file.read().split("\n")


print(log_monitoring(t, e, log))
