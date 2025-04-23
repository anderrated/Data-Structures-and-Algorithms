class Job:
    def __init__(self, name, days_to_complete, daily_penalty):
        self.name = name
        self.days_to_complete = days_to_complete
        self.daily_penalty = daily_penalty

    def __repr__(self):
        return f"Job Name = {self.name}, Days to Complete = {self.days_to_complete}, Daily Penalty = {self.daily_penalty}"
        
    def add_actual_finish(self, value):
        self.actual_finish = value

    def add_late_days(self, value):
        self.late_days = value

class Solution:
    def __init__(self, job_list):
        self.job_list = job_list

    def sequence(self):
        self.job_list.sort(key=lambda job: job.daily_penalty / job.days_to_complete, reverse=True)
        return self.job_list
    
    def actual_finish(self):
        self.sequence()
        actual_finish_day = 0
        for i in range(len(self.job_list)):
            actual_finish_day = actual_finish_day + self.job_list[i].days_to_complete
            self.job_list[i].add_actual_finish(actual_finish_day)
        return self.job_list

    def late_days(self):
        self.actual_finish()
        for i in range(len(self.job_list)):
            num_late_days = self.job_list[i].actual_finish - self.job_list[i].days_to_complete
            self.job_list[i].add_late_days(num_late_days)
        return self.job_list
    
    def calc_penalty(self):
        total_penalty = 0
        for i in range(len(self.job_list)):
            penalty = self.job_list[i].daily_penalty * self.job_list[i].late_days
            total_penalty += penalty
        return total_penalty
        
def main():
    num_test_cases = int(input())
    final_output = []
    for _ in range(num_test_cases):
        num_jobs = int(input())
        job_list = []
        for _ in range(num_jobs):
            job = input()
            customer_name, days_to_complete, daily_penalty = job.split()
            job_list.append(Job(customer_name, int(days_to_complete), int(daily_penalty)))
        
        Solution(job_list).late_days()
        job_sequence = [job.name for job in job_list]
        final_output.append(f"{Solution(job_list).calc_penalty()} {"-".join(job_sequence)}")

    print("\n".join(final_output))
    
main()