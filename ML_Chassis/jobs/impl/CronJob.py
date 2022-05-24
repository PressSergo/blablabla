from jobs import JobBatcher
import json

class CronJob(JobBatcher):
    def execute(self):
        return json.load(open('../resources/user.json'))