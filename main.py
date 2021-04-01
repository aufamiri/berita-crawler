from taskModel import TaskModel

import source
import dest
import json
import datetime


def load_task():
    f = open('main.json',)
    data = json.load(f)

    tasks = []
    output = data["output"]["type"]
    file_name = data["output"].get("name")

    for item in data['tasks']:
        start_date = item.get("start_date")
        end_date = item.get("end_date")

        if(start_date is not None):
            start_date = parse_date(start_date)

        if(end_date is not None):
            end_date = parse_date(end_date)

        tasks.append(TaskModel(
            item["src"],
            item["target_length"],
            start_date,
            end_date
        ))

    run(tasks, output, file_name)


def parse_date(date):
    return datetime.datetime.strptime(date, "%d/%m/%Y")


def run(tasks, output, file_name):
    result = []

    for task in tasks:
        tempResult = source.init(task.src, task.target_length,
                                 task.start_date, task.end_date)

        result = result + tempResult

    dest.init(output, result, file_name)


if __name__ == '__main__':
    load_task()
