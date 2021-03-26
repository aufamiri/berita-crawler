from taskModel import TaskModel

import source
import dest
import json


def load_task():
    f = open('main.json',)
    data = json.load(f)

    tasks = []
    output = data["output"]["type"]
    file_name = data["output"]["name"]

    for item in data['tasks']:
        tasks.append(TaskModel(
            item["src"],
            item["target_length"],
            item.get("start_date"),
            item.get("end_date")))

    run(tasks, output, file_name)


def run(tasks, output, file_name):
    result = []

    for task in tasks:
        tempResult = source.init(task.src, task.target_length,
                                 task.start_date, task.end_date)

        result = result + tempResult

    dest.init(output, result, file_name)


if __name__ == '__main__':
    load_task()
