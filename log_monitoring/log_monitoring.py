import datetime


def l_m(t, e, log):
    interval = datetime.timedelta(seconds=t)
    result = -1
    error_times = []
    for line in log:
        status = line[22:27]
        if status == "ERROR":
            date = datetime.datetime.strptime(line[1:20], "%Y-%m-%d %H:%M:%S")
            error_times.append(date)
            if len(error_times) == e:
                if error_times[-1] < error_times[0] + interval:
                    result = date
                    break
                error_times.pop(0)
    return str(result)
