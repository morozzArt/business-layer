import json


class TaskLoader:

    def __init__(self, filename='tasks.json'):
        """
        Constructor which opens file with tasks and parses it.

        :param filename: str, optional(default='commands.json').
            Name of the json file with tasks.
        """
        self._filename = filename
        with open(filename, 'r', encoding='utf-8') as infile:
            self._parsed_json_tasks = json.loads(infile.read())

    def __getitem__(self, item):
        """
        Add dict-like interface: loader[item]

        :param item: str.
            Task name in file.
        :return: int, float, str, dict, list, bool, None.
            Task with all parameters from file.
        """
        with open(self._filename, 'r', encoding='utf-8') as infile:
            self._parsed_json_tasks = json.loads(infile.read())
        return self._parsed_json_tasks[item]

    def is_exist(self, task):
        return task['name'] not in self._parsed_json_tasks

    def load_task(self, task_name):
        return self[task_name]

    def save_task(self, task):
        if not task['name']:
            return

        if self.is_exist(task):
            self._parsed_json_tasks[task['name']] = task

            # TODO: need to avoid rewriting all file but append at the end.
            with open(self._filename, 'w', encoding='utf-8') as outfile:
                json.dump(self._parsed_json_tasks, outfile)
