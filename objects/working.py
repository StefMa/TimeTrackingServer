from workingday import working_day
from work import work
from mytime import my_time

class working():
    @staticmethod
    def create_from_json(json_dict):
        work = working()
        work.token = json_dict["token"]
        work.working_day = working_day(json_dict["working_day"]["year"], json_dict["working_day"]["month"], json_dict["working_day"]["day"])
        work.double_working = json_dict["double_working"]
        work.first_work = working.extract_work_from_json(json_dict, "first_work")
        work.second_work = working.extract_work_from_json(json_dict, "second_work")
        return work

    @staticmethod
    def extract_work_from_json(json_dict, which_work):
        start_time = my_time(json_dict[which_work]["start_time"]["hour"], json_dict[which_work]["start_time"]["minute"])
        end_time = my_time(json_dict[which_work]["end_time"]["hour"], json_dict[which_work]["end_time"]["minute"])
        break_time = json_dict[which_work]["break_time"]

        my_work = work(start_time, end_time, break_time)
        return my_work
