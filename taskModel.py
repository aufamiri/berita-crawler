class TaskModel:
    def __init__(self, src, target_length, start_date=None, end_date=None):
        self.src = src
        self.target_length = target_length
        self.start_date = start_date
        self.end_date = end_date
