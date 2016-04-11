from workingday import working_day
from work import work
from mytime import my_time

class working():
    @staticmethod
    def create_from_json(json_dict):
        work = working()
        work.token = json_dict["token"]
        work.working_day = working.extract_working_day_from_json(json_dict)
        work.work_list = []
        for w in json_dict["work"]:
            work.work_list.append(working.extract_work_from_json(w))
        return work

    @staticmethod
    def extract_working_day_from_json(working_day_as_list):
        return working_day(working_day_as_list["working_day"]["year"], working_day_as_list["working_day"]["month"], working_day_as_list["working_day"]["day"])

    @staticmethod
    def extract_work_from_json(work_object_as_tuble):
        start_time = my_time(work_object_as_tuble["start_time"]["hour"], work_object_as_tuble["start_time"]["minute"])
        end_time = my_time(work_object_as_tuble["end_time"]["hour"], work_object_as_tuble["end_time"]["minute"])
        break_time = work_object_as_tuble["break_time"]

        my_work = work(start_time, end_time, break_time)
        return my_work
