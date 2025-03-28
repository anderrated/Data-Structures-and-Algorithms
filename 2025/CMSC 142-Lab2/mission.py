import heapq
from dataclasses import dataclass
from math import e

@dataclass
class Mission:
    name: str
    day_of_arrival: int
    length: int
    remaining: int
    first_execution: int = -1
    completion_day: int = -1

    def __lt__(self, other):
        # we assume that other is an instance of Mission
        assert isinstance(other, Mission)
        # compare missions with other instances of Missions for maintaining heap property
        return self.remaining < other.remaining

# pop all the missions of the least day_of_arrival
# group mission by day_of_arrival
def pop_missions(missions: list[Mission]) -> list[Mission]:
    first = missions[-1]
    res = []
    '''
    grouping missions by day_of_arrival:
    as long as the day_of_arrival of the last mission in the
    list is equal to the day_of_arrival of the first mission,
    pop and add to result list
    '''
    while missions and missions[-1].day_of_arrival == first.day_of_arrival:
        res.append(missions.pop())

    return res


def simulate_mission(original_missions: list[Mission]) -> tuple[list[str], list[Mission]]:
    # as long as there are missions in the missions list
    assert len(original_missions) > 0
    missions = original_missions.copy()
    res: list[str] = []

    # we reverse our ArrayLists because popping from the right is constant
    missions.sort(key=lambda m: m.day_of_arrival, reverse=True)
    # set the day to the day_of_arrival of the last mission in the list
    day = missions[-1].day_of_arrival
    # add missions of the same day to the heap
    heap: list[Mission] = pop_missions(missions)
    # min heapify the missions in the same group based on length
    heapq.heapify(heap)

    # as long as there are missions in the heap
    while len(heap) > 0:
        '''
        if new missions arrive, add them to the heap
        '''
        if missions and day == missions[-1].day_of_arrival:
            for mission in pop_missions(missions):
                # push the popped missions to the heap
                heapq.heappush(heap, mission)

        # pop/get the mission with the shortest length
        current_mission = heapq.heappop(heap)

        # record first execution day
        if current_mission.first_execution == -1:
            current_mission.first_execution = day

        current_mission.remaining -= 1
        # if the mission is not done, push it back to the heap
        if current_mission.remaining > 0:
            heapq.heappush(heap, current_mission)
        else:
            current_mission.completion_day = day + 1
            for original_mission in original_missions:
                if original_mission.name == current_mission.name:
                    original_mission.completion_day = current_mission.completion_day
                    original_mission.first_execution = current_mission.first_execution
                    break
 
        # add the mission name to the result list
        res.append(current_mission.name)
        # next day
        day += 1

    return res, original_missions

def main():
    n = int(input("Enter number of test cases:"))
    test_cases = []

    for i in range(n):
        m = int(input("Enter number of missions:"))
        missions = []

        for j in range(m):
            name, day_of_arrival, length = input("Enter mission name, day of arrival, length:").split()
            missions.append(Mission(name, int(day_of_arrival), int(length), int(length)))

        test_cases.append(missions)

    for missions in test_cases:
        # execution order
        execute_order, completed_missions = simulate_mission(missions)
        print(execute_order)

        for mission in completed_missions: 
            # turnaround times = day of completion - day of arrival
            turnaround_time = mission.completion_day - mission.day_of_arrival
            print(turnaround_time, end=" ")
        print() # new line

        for mission in completed_missions: 
            # pounce times = day first catered  - day of arrival
            pounce_time = mission.first_execution - mission.day_of_arrival
            print(pounce_time, end=" ")
        print() # new line

        for mission in completed_missions: 
            # turnaround times = day of completion - day of arrival
            turnaround_time = mission.completion_day - mission.day_of_arrival
            # nap times = turnaround times - mission length
            nap_time = turnaround_time - mission.length
            print(nap_time, end=" ")
        print()
main()