from dataclasses import dataclass
from heap import MaxHeap


@dataclass
class Beehive:
    """A beehive has a position in 3d space, and some stats."""

    x: int
    y: int
    z: int

    capacity: int
    nutrient_factor: int
    volume: int = 0

    def __lt__(self, beehive) -> bool:
        """
        Time Complexity:
        - Best case = Worst case: O(1), only performing arithmetic operations
        """
        return (self.nutrient_factor * min(self.capacity, self.volume)) < (
                    beehive.nutrient_factor * min(beehive.capacity, beehive.volume))

    def __le__(self, beehive) -> bool:
        """
        Time Complexity:
        - Best case = Worst case: O(1), only performing arithmetic operations
        """
        return (self.nutrient_factor * min(self.capacity, self.volume)) <= (
                    beehive.nutrient_factor * min(beehive.capacity, beehive.volume))

    def __gt__(self, beehive) -> bool:
        """
        Time Complexity:
        - Best case = Worst case: O(1), only performing arithmetic operations
        """
        return (self.nutrient_factor * min(self.capacity, self.volume)) > (
                    beehive.nutrient_factor * min(beehive.capacity, beehive.volume))

    def __ge__(self, beehive) -> bool:
        """
        Time Complexity:
        - Best case = Worst case: O(1), only performing arithmetic operations
        """
        return (self.nutrient_factor * min(self.capacity, self.volume)) >= (
                    beehive.nutrient_factor * min(beehive.capacity, beehive.volume))

    def __eq__(self, beehive) -> bool:
        """
        Time Complexity:
        - Best case = Worst case: O(1), only performing arithmetic operations
        """
        return (self.nutrient_factor * min(self.capacity, self.volume)) == (
                    beehive.nutrient_factor * min(beehive.capacity, beehive.volume))

class BeehiveSelector:

    def __init__(self, max_beehives: int) -> None:
        """
        Time Complexity:
        - Best case = Worst case: O(max_beehives), create ArrayR of size max_beehive in init of MaxHeap
        """
        self.max_beehives = max_beehives
        self.beehives = MaxHeap(max_beehives)

    def set_all_beehives(self, hive_list: list[Beehive]) -> None:
        """
        Time Complexity:
        - Best case = Worst case: O(M), where M is the len(hive_list)
        """
        self.beehives = MaxHeap(self.max_beehives)
        for hive in hive_list:
            self.beehives.add(hive)

    def add_beehive(self, hive: Beehive) -> None:
        """
        Time Complexity:
        - Worst case: O(log(N)) where N is the number of elements in heap, when the added hive have to rise to its position
        - Best case: O(1) when the added hive have lower key than all other keys in the heap
        """
        self.beehives.add(hive)

    def harvest_best_beehive(self) -> float:
        """
        -> Assume complexity of sink() is O(log(N)), where N is the number of elements in the heap,
           thus worst case for get_max() is O(log(N))

        Overall Time Complexity:
        - Best case = Worst case: O(log(N)), where N is the number of elements in the heap
        """
        hive = self.beehives.get_max()
        quantity = min(hive.volume, hive.capacity)
        hive.volume -= quantity
        self.add_beehive(hive)
        return quantity * hive.nutrient_factor