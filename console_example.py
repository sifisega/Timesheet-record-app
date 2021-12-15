EMPLOYEES = {
    'Kane':[],
    'Allan':[],
    'Fraser':[]
}
JOBS = {'0':[], }

class Job():
    # defines a job that is a collection of shifts
    def __init__(self, key):
        self.shifts = []
        JOBS[key] = self

    def add_shift(self, shift):
        self.shifts.append(shift)


class Shift():
    # defines a period of time an employee worked towards a specific job
    def __init__(self, start_time=0, end_time=0, date=0, job=False, employee=''):
        if job == False:
            self.prompt()
        else:
            self.start_time = start_time
            self.end_time = end_time
            self.length = end_time - start_time
            self.date = date
            self.employee = employee
            self.job = job
        try:
            JOBS[job].add_shift(self)
        except Exception as e:
            return('ERROR on ' + self + 'into ' + job)
        finally:
            EMPLOYEES[employee].append(self)

    def prompt(self):
        start_time = int(input('Start of shift? in 0700 format'))
        end_time = int(input('End of shift? In 1530 format'))
        date = input('Date of shift?')
        employee = input('Who worked the shift?')
        self.start_time = start_time
        self.end_time = end_time
        self.length = end_time - start_time
        self.date = date
        self.employee = employee
        self.job = self.ask_for_job()

    def ask_for_job(self):
        while True:
            job = input('Job number?')
            if job in JOBS.keys():
                return job






def new_job():
    job_num = input('Job number? in format 2295T')
    Job(job_num)

def new_shift():
 shift = Shift()

def main():
    while True:
        action = input("New Job?   |   New Shift?\n     J     |      S      ")
        actioin = action.lower()
        if action == 'e' or action == 'exit' or action == 'stop':
            return
        elif action == 'j':
            new_job()
        elif action == 's':
            new_shift()
        else:
            print('Sorry, unknown input, please try again :/')


main()
