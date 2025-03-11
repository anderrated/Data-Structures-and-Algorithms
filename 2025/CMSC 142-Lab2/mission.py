import heapq
from dataclasses import dataclass

@dataclass
class Mission:
    name: str
    day_of_arrival: int
    length: int

    def __lt__(self, other):
        assert isinstance(other, Mission)
        # compare missions with other instances of Missions
        return self.length < other.length

# pop all the missions of the least day_of_arrival
# group mission by day_of_arrival
def pop_missions(missions: list[Mission]) -> list[Mission]:
    first = missions[-1]
    res = []

    '''
    Grouping missions by day_of_arrival ->
    as long as there are missions in the missions list
    and the day_of_arrival of the last mission in the
    list is equal to the day_of_arrival of the first mission,
    pop and add to result list
    '''
    while missions and missions[-1].day_of_arrival == first.day_of_arrival:
        res.append(missions.pop())

    return res


def simulate_mission(missions: list[Mission]) -> list[str]:
    # as long as there are missions in the missions list
    assert len(missions) > 0

    res: list[str] = []

    # we reverse our ArrayLists because popping from the right is constant
    missions.sort(key=lambda m: m.day_of_arrival, reverse=True)

    day = missions[-1].day_of_arrival
    # heapify missions in the same group based on length
    heap: list[Mission] = pop_missions(missions)
    # min heapify the missions in the same group based on length
    heapq.heapify(heap)

    # as long as there are missions in the heap
    while len(heap) > 0:
        '''
        if there are missions in the missions list
        and the day is equal to the day_of_arrival of the last
        mission in the list, pop all missions that have the
        same day of arrival and add them to the heap
        '''
        if missions and day == missions[-1].day_of_arrival:
            for mission in pop_missions(missions):
                # push the popped missions to the heap
                heapq.heappush(heap, mission)

        # pop/get the mission with the shortest length
        current_mission = heapq.heappop(heap)
        current_mission.length -= 1
        # if the mission is not done, push it back to the heap
        if current_mission.length > 0:
            heapq.heappush(heap, current_mission)

        # add the mission name to the result list
        res.append(current_mission.name)
        # next day
        day += 1

    return res

print(
    simulate_mission(
        [Mission("Furry", 0, 24), Mission("Mittens", 2, 3), Mission("Purrington", 3, 3)]
    )
)