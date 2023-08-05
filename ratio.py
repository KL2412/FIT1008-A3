from __future__ import annotations
from typing import Generic, TypeVar
from math import ceil
from bst import BinarySearchTree

T = TypeVar("T")
I = TypeVar("I")


class Percentiles(Generic[T]):

    def __init__(self) -> None:
        """
        Time Complexity:
        - Best case = Worst case: O(1)
        """
        self.bst = BinarySearchTree()

    def add_point(self, item: T):
        """
        Time Complexity:
        - Worst case: O(log(N) <- O(comp * d) where comp is the complexity for comparing keys, where d is the depth of the tree
        - Best case: O(comp), where comp is the complexity for comparing keys, when root is None
        """
        self.bst[item] = 0

    def remove_point(self, item: T):
        """
        Time Complexity:
        - Worst case: O(log(N) <- O(comp * d) where comp is the complexity for comparing keys, where d is the depth of the tree
        - Best case: O(comp), where comp is the complexity for comparing keys, when root is None
        """
        del self.bst[item]

    def ratio(self, x, y) -> list[T]:
        """
        Time Complexity:
        - Worst case: O(log(N)+O) where O is the number of points returned by the function
        - Best case = O(1), no operation needed when x+y is bigger equal than 100
        """
        #not possible to have anything
        if x + y >= 100:
            return []
        
        n_nodes = self.bst.root.subtree_size
        lower_bound = ceil(n_nodes * x / 100) + 1
        upper_bound = n_nodes - ceil(n_nodes * y / 100)

        lower = self.bst.kth_smallest(lower_bound, self.bst.root).key
        upper = self.bst.kth_smallest(upper_bound, self.bst.root).key

        return self.bst.sorted_splice(lower, upper)


if __name__ == "__main__":
    points = list(range(50))
    import random

    random.shuffle(points)
    p = Percentiles()
    for point in points:
        p.add_point(point)
    # Numbers from 8 to 16.
    print(p.ratio(15, 66))