import heapq
from dataclasses import dataclass

@dataclass
class Mission:
    name: str
    day_of_arrival: int
    length: int
    remaining_time: int
    first_execution: int = -1
    completion_time: int = -1

    def __lt__(self, other):
        return self.remaining_time < other.remaining_time


def pop_missions(missions: list[Mission]) -> list[Mission]:
    first = missions[-1]
    res = []
    while missions and missions[-1].day_of_arrival == first.day_of_arrival:
        res.append(missions.pop())
    return res


def simulate_mission(missions: list[Mission]):
    assert len(missions) > 0
    
    missions.sort(key=lambda m: m.day_of_arrival, reverse=True)
    day = missions[-1].day_of_arrival
    heap: list[Mission] = pop_missions(missions)
    heapq.heapify(heap)
    executed_order = []
    
    while heap:
        if missions and day == missions[-1].day_of_arrival:
            for mission in pop_missions(missions):
                heapq.heappush(heap, mission)
        
        current_mission = heapq.heappop(heap)
        
        if current_mission.first_execution == -1:
            current_mission.first_execution = day
        
        current_mission.remaining_time -= 1
        executed_order.append(current_mission.name)
        
        if current_mission.remaining_time > 0:
            heapq.heappush(heap, current_mission)
        else:
            current_mission.completion_time = day + 1
        
        day += 1
    
    return executed_order, heap


def main():
    n = int(input("Enter number of test cases: "))
    for _ in range(n):
        m = int(input("Enter number of missions: "))
        missions = []
        mission_dict = {}
        
        for _ in range(m):
            name, arrival, length = input("Enter mission name, day of arrival, length: ").split()
            arrival, length = int(arrival), int(length)
            mission = Mission(name, arrival, length, length)
            missions.append(mission)
            mission_dict[name] = mission
        
        executed_order, _ = simulate_mission(missions)
        print("Execution order:", executed_order)
        
        print("Mission Times:")
        for mission in mission_dict.values():
            turnaround_time = mission.completion_time - mission.day_of_arrival
            pounce_time = mission.first_execution - mission.day_of_arrival
            nap_time = turnaround_time - mission.length
            print(f"{mission.name}: Turnaround = {turnaround_time}, Pounce = {pounce_time}, Nap = {nap_time}")

main()
