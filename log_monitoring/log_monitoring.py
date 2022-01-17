import datetime

result = []
with open("test_3.txt", "r") as log_file:
    line = log_file.readline().split()
    t, e = list(map(int, line))
    interval = datetime.timedelta(seconds=t)
    while True:
        line = log_file.readline()
        if not line:
            print(-1)
            break
        status = line[22:27]
        if status == "ERROR":
            date = datetime.datetime.strptime(line[1:20], "%Y-%m-%d %H:%M:%S")
            result.append(date)
            while result[-1] >= result[0] + interval:
                result.pop(0)
            if len(result) >= e:
                print(str(date))
                break
