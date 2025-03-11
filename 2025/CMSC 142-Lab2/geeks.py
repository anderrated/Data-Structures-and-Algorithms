class Process:
    def __init__(self, id, arrival_time, burst_time):
        self.id = id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time

def srtf(processes):
    current_time, completed = 0, 0
    while completed < len(processes):
        idx = -1
        for i, p in enumerate(processes):
            if p.arrival_time <= current_time and p.remaining_time > 0 and (idx == -1 or p.remaining_time < processes[idx].remaining_time):
                idx = i
        if idx != -1:
            processes[idx].remaining_time -= 1
            current_time += 1
            if processes[idx].remaining_time == 0:
                processes[idx].completion_time = current_time
                processes[idx].turnaround_time = current_time - processes[idx].arrival_time
                processes[idx].waiting_time = processes[idx].turnaround_time - processes[idx].burst_time
                completed += 1
        else:
            current_time += 1

def print_results(processes):
    total_wt, total_tat = 0, 0
    for p in processes:
        total_wt += p.waiting_time
        total_tat += p.turnaround_time
        print(f"P{p.id} CT: {p.completion_time} WT: {p.waiting_time} TAT: {p.turnaround_time}")
    print(f"Avg WT: {total_wt / len(processes)} Avg TAT: {total_tat / len(processes)}")

n = int(input("Enter number of processes: "))
processes = [Process(i + 1, *map(int, input(f"Enter arrival and burst time for P{i + 1}: ").split())) for i in range(n)]
srtf(processes)
print_results(processes)