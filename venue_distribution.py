days = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
]

table_time = []

time_dict = {}

days_dict = {}

count = 0


def get_time(time_in, time_out, ranges):
    ti_di = time_out - time_in
    for i in range(int(ti_di / (ranges - 1))):
        times = f"{time_in}:00"
        for j in range(ranges - 1):
            time_in += 1
        times = f"{times}-{time_in}:00"

        table_time.append(times)

    return table_time


get_time(7, 21, 3)

for i in days:
    count += 1
    if i not in time_dict:
        time_dict[i] = {}

    time_dict[i] = f"d{count}"

print(time_dict)
