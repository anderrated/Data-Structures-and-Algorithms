from flask import app
from flask_migrate import current


class Appointment:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __repr__(self) -> str:
        return f"Appointment(start={self.start}, end={self.end})"

class Solution:
    def __init__(self, appointment_list):
        self.appointment_list = appointment_list
        
    def sort_appoinments(self):
       self.appointment_list.sort(key=lambda appointment: appointment.start)
       return self.appointment_list
    
    # def find_max_interval(self):
    #     self.sort_appoinments()
    #     max_current = 0
    #     max_next = 0
    #     max_time_difference = 0
    #     for i in range(len(self.appointment_list)-1):
    #         current_appointment =  self.appointment_list[i]
    #         next_appointment = self.appointment_list[i+1]

    #         if next_appointment.start - current_appointment.end > max_time_difference:
    #             max_time_difference = next_appointment.start - current_appointment.end
    #             max_current = current_appointment.end
    #             max_next = next_appointment.start
            
    #     return max_current, max_next

    def find_max_interval(self):
        self.sort_appoinments()
        current_start = 10
        max_gap = 0
        max_gap_start = -1
        max_gap_end = -1
        for appointment in self.appointment_list:
            current_end = appointment.start
            current_gap = current_end - current_start
            if (current_gap > max_gap):
                max_gap_start = current_start
                max_gap_end = current_end
                max_gap = current_gap
            current_start = appointment.end

        current_end = 18
        current_gap = current_end - current_start
        if (current_gap > max_gap):
            max_gap = current_gap
            max_gap_start = current_start
            max_gap_end = current_end

        return max_gap_start, max_gap_end

def main():
    num_test_cases = int(input())
    final_output = []
    for _ in range(num_test_cases):
        num_appointments = int(input())
        appointment_list = []
        for _ in range(num_appointments):
            appointment = input()
            start, end = appointment.split()
            appointment_list.append(Appointment(float(start), float(end)))

        formatted_interval = "{:.2f} {:.2f}".format(*Solution(appointment_list).find_max_interval())
        final_output.append(formatted_interval)
    print("\n".join(final_output))
    
main()