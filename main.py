import json
import random


class VenueDistribution:
    venue_day_time_b50 = []

    venue_day_time_a50 = []

    venue_day_time_a120 = []

    venue_day_time_b120 = []

    table_time = []

    w_v_d_t = ""

    days = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
    ]

    weeks = ["w"]

    b50_taken = []
    a50_taken = []
    b120_taken = []
    a120_taken = []

    def assign_venue(self, size):
        size = int(size)
        if size < 40:
            data = self.venue_day_time_b50
            rnd_venue_list = random.randint(0, len(data) - 1)
            w_v_d_t = random.choice(data[rnd_venue_list])
            while self.b50_taken.count(w_v_d_t.strip().split(";")[1]) > 19:
                rnd_venue_list = random.randint(0, len(data) - 1)
                w_v_d_t = random.choice(data[rnd_venue_list])
                print("error 21 b50")
            self.b50_taken.append(w_v_d_t.strip().split(";")[1])
            data[rnd_venue_list].remove(w_v_d_t)
            self.w_v_d_t = w_v_d_t
        elif size <= 70:
            data = self.venue_day_time_a50
            rnd_venue_list = random.randint(0, len(data) - 1)
            w_v_d_t = random.choice(data[rnd_venue_list])
            while self.a50_taken.count(w_v_d_t.strip().split(";")[1]) > 19:
                rnd_venue_list = random.randint(0, len(data) - 1)
                w_v_d_t = random.choice(data[rnd_venue_list])
                print("error 21 a50")
            self.a50_taken.append(w_v_d_t.strip().split(";")[1])
            data[rnd_venue_list].remove(w_v_d_t)
            self.w_v_d_t = w_v_d_t

        elif size <= 150:
            data = self.venue_day_time_b120
            rnd_venue_list = random.randint(0, len(data) - 1)
            w_v_d_t = random.choice(data[rnd_venue_list])
            while self.b120_taken.count(w_v_d_t.strip().split(";")[1]) > 19:
                rnd_venue_list = random.randint(0, len(data) - 1)
                w_v_d_t = random.choice(data[rnd_venue_list])
                print("error 21 b120")
            self.b120_taken.append(w_v_d_t.strip().split(";")[1])
            data[rnd_venue_list].remove(w_v_d_t)
            self.w_v_d_t = w_v_d_t

        elif size > 150:
            data = self.venue_day_time_a120
            rnd_venue_list = random.randint(0, len(data) - 1)
            w_v_d_t = random.choice(data[rnd_venue_list])
            while self.a120_taken.count(w_v_d_t.strip().split(";")[1]) > 19:
                rnd_venue_list = random.randint(0, len(data) - 1)
                w_v_d_t = random.choice(data[rnd_venue_list])
                print("error 21 a120")
            self.a120_taken.append(w_v_d_t.strip().split(";")[1])
            data[rnd_venue_list].remove(w_v_d_t)
            self.w_v_d_t = w_v_d_t

    def get_wvdt(self, wvdt):
        return wvdt

    def set_venues(self):
        self.venue_b50()
        self.venue_a50()
        self.venue_b120()
        self.venue_a120()

    def venue_b50(self):
        vnb50 = self.load("venueb50.json")
        venuesb50 = [i for i in vnb50.keys()]
        self.venue_day_time_b50 = [[f"{h};{i};{k};{j}" for j in self.get_time(7, 21, 3)] for k in self.days
                                   for i in venuesb50 for h in self.weeks]
        return self.venue_day_time_b50

    def venue_a50(self):
        vna50 = self.load("venuea50.json")
        venuea50 = [i for i in vna50.keys()]
        self.venue_day_time_a50 = [[f"{h};{i};{k};{j}" for j in self.get_time(7, 21, 3)] for k in self.days
                                   for i in venuea50 for h in self.weeks]

        return self.venue_day_time_a50

    def venue_a120(self):
        vna120 = self.load("venuea120.json")
        venuea120 = [i for i in vna120.keys()]
        self.venue_day_time_a120 = [[f"{h};{i};{k};{j}" for j in self.get_time(7, 21, 3)] for k in self.days
                                    for i in venuea120 for h in self.weeks]

        return self.venue_day_time_a120

    def venue_b120(self):
        vnb120 = self.load("venueb120.json")
        venueb120 = [i for i in vnb120.keys()]
        self.venue_day_time_b120 = [[f"{h};{i};{k};{j}" for j in self.get_time(7, 21, 3)] for k in self.days
                                    for i in venueb120 for h in self.weeks]

        return self.venue_day_time_b120

    def get_time(self, time_in, time_out, ranges):
        ti_di = time_out - time_in
        for i in range(int(ti_di / (ranges - 1))):
            times = f"{time_in}:00"
            for j in range(ranges - 1):
                time_in += 1
            times = f"{times}-{time_in}:00"

            self.table_time.append(times)

        return self.table_time

    def load(self, name):
        with open(name, "r") as file:
            initial_data = json.load(file)
        return initial_data


class Timetable:
    timetable = {}

    days = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
    ]

    weeks = []

    table_time = []

    venue_day_time_100 = []

    venue_day_time_10 = []

    venue_day_time_b50 = []

    venue_day_time_a50 = []

    venue_day_time_a120 = []

    venue_day_time_b120 = []

    taken_venue_day_list = []

    taken_programme_day = []

    day_time_id = []

    default_table = {}

    def get_code(self):
        pass

    def get_size(self, text):
        import re

        pattern = r'^(.*?)\s*\((\d+)\)$'

        match = re.match(pattern, text)

        if match:
            extracted_text = match.group(1).strip()
            extracted_number = match.group(2)

            return extracted_number
        else:
            print("No match found.")

    def load(self, name):
        with open(name, "r") as file:
            initial_data = json.load(file)
        return initial_data

    def write(self, data):
        with open("tble.json", "w") as file:
            initial_data = json.dumps(data, indent=4)
            file.write(initial_data)

    def venue_b50(self):
        vnb50 = self.load("venueb50.json")
        venuesb50 = [i for i in vnb50.keys()]
        self.venue_day_time_b50 = [[f"{h};{i};{k};{j}" for j in self.table_time] for k in self.days
                                   for i in venuesb50 for h in self.weeks]
        return self.venue_day_time_b50

    def venue_a50(self):
        vna50 = self.load("venuea50.json")
        venuea50 = [i for i in vna50.keys()]
        self.venue_day_time_a50 = [[f"{h};{i};{k};{j}" for j in self.table_time] for k in self.days
                                   for i in venuea50 for h in self.weeks]

        return self.venue_day_time_a50

    def venue_a120(self):
        vna120 = self.load("venuea120.json")
        venuea120 = [i for i in vna120.keys()]
        venue_day_time_a120 = [[f"{h};{i};{k};{j}" for j in self.table_time] for k in self.days
                               for i in venuea120 for h in self.weeks]

        return venue_day_time_a120

    def venue_b120(self):
        vnb120 = self.load("venueb120.json")
        venueb120 = [i for i in vnb120.keys()]
        self.venue_day_time_b120 = [[f"{h};{i};{k};{j}" for j in self.table_time] for k in self.days
                                    for i in venueb120 for h in self.weeks]

        return self.venue_day_time_b120

    def get_programmes(self):
        programes = self.load("module.json")
        programmes = [i for i in
                      programes.keys()]

        return programmes

    def get_modules(self):
        modules = self.load("module.json")

        modules_lits = [[modules[i][j].strip() for j in modules[i]]
                        for i in modules]

        return modules_lits

    def get_time(self, time_in, time_out, ranges):
        ti_di = time_out - time_in
        for i in range(int(ti_di / (ranges - 1))):
            times = f"{time_in}:00"
            for j in range(ranges - 1):
                time_in += 1
            times = f"{times}-{time_in}:00"

            self.table_time.append(times)

        return self.table_time

    def get_default_table(self):
        default_table = self.load("ble.json")

        return default_table

    def set_venue_day(self):

        self.day_time_id = [f"{i};{j}" for j in self.get_time(7, 21, 3) for i in self.days]

        return self.day_time_id

    def set_venue_day_time(self, venue, programme):

        day_time = random.choice(self.set_venue_day())
        venue_day_time = f"{venue};{day_time}"

        programme_day = f"{programme}{day_time.strip().split(';')[0]}"

        while self.taken_programme_day.count(programme_day) > 3:
            day_time = random.choice(self.set_venue_day())
            venue_day_time = f"{venue};{day_time}"
            programme_day = f"{programme}{day_time.strip().split(';')[0]}"
            # print("pro error")

        self.taken_venue_day_list.append(venue_day_time)
        self.taken_programme_day.append(programme_day)

        return venue_day_time

    def set_venue_b21(self):
        venue_distri = VenueDistribution()
        venue_distri.set_venues()
        self.default_table = self.load("tble.json")
        for i in self.default_table:
            # print(i)
            programme_size = self.get_size(i)
            for j in self.default_table[i]:
                venue_distri.assign_venue(programme_size)
                module_venue = venue_distri.w_v_d_t.strip().split(";")[1]
                if i not in self.timetable:
                    self.timetable[i] = {}

                self.timetable[i][j] = {
                    "venue": module_venue,
                    "module": j,
                    "program": i,
                }

        self.write(self.timetable)
        print(venue_distri.a120_taken.count("CLASS VIII"))

    def generate_table(self):
        self.set_venue_b21()
        self.default_table = self.load("tble.json")
        for i in self.default_table:
            for j in self.default_table[i]:
                venue = self.default_table[i][j]["venue"]
                period_one = self.set_venue_day_time(venue, i)
                period_two = self.set_venue_day_time(venue, i)


Timetable.generate_table(Timetable())
