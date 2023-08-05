from __future__ import annotations
from typing import Generic, TypeVar, Tuple
from dataclasses import dataclass, field

I = TypeVar('I')
Point = Tuple[int, int, int]


@dataclass
class BeeNode:
    key: Point
    item: I
    subtree_size: int = 1
    child: list[BeeNode | None] = field(default_factory=lambda: [None] * 8)

    def get_child_for_key(self, point: Point) -> BeeNode | None:
        """
        Time Complexity:
        - Best case = Worst case: O(1)
        """
        octant = 0
        if point[0] >= self.key[0]:
            octant += 1
        if point[1] >= self.key[1]:
            octant += 2
        if point[2] >= self.key[2]:
            octant += 4

        return self.child[octant]


class ThreeDeeBeeTree(Generic[I]):
    """ 3️⃣🇩🐝🌳 tree. """

    def __init__(self) -> None:
        """
            Initialises an empty 3DBT
        """
        self.root = None
        self.length = 0

    def is_empty(self) -> bool:
        """
            Checks to see if the 3DBT is empty
        """
        return len(self) == 0

    def __len__(self) -> int:
        """ Returns the number of nodes in the tree. """

        return self.length

    def __contains__(self, key: Point) -> bool:
        """
            Checks to see if the key is in the 3DBT
        """
        try:
            self.get_tree_node_by_key(key)
            return True
        except KeyError:
            return False

    def __getitem__(self, key: Point) -> I:
        """
            Attempts to get an item in the tree, it uses the Key to attempt to find it
        """
        node = self.get_tree_node_by_key(key)
        return node.item

    def get_tree_node_by_key(self, key: Point) -> BeeNode:
        return self.get_tree_node_by_key_aux(self.root, key)

    def get_tree_node_by_key_aux(self, current, key) -> BeeNode:
        """
        Time Complexity:
        - Worst case: O(D), where D is the maximum depth of the tree
        - Best case: O(1), the key to be found is the root
        """
        if current.key == key:
            return current
        else:
            new_node = current.get_child_for_key(key)
            return self.get_tree_node_by_key_aux(new_node, key)

    def __setitem__(self, key: Point, item: I) -> None:
        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: BeeNode, key: Point, item: I) -> BeeNode:
        """
        Attempts to insert an item into the tree, it uses the Key to insert it

        Time Complexity:
        - Worst case: O(d * comp), where d is the maximum depth of the tree, where comp is the comparison of key
        - Best case: O(comp), where comp is the comparison of key, when the tree is empty or when the key existed in the tree
        """
        if current is None:  # base case: at the leaf
            current = BeeNode(key, item=item)
            self.length += 1
        elif current.key == key:
            raise ValueError('Inserting duplicate item')
        else:
            octant = 0
            if key[0] >= current.key[0]:
                octant += 1
            if key[1] >= current.key[1]:
                octant += 2
            if key[2] >= current.key[2]:
                octant += 4
            current.child[octant] = self.insert_aux(current.child[octant], key, item)
            current.subtree_size += 1
        return current

    def is_leaf(self, current: BeeNode) -> bool:
        """ Simple check whether or not the node is a leaf.

        Time Complexity:
        - Worst case: O(1), since the number of iteration of for loop is constant, always 8
        - Best case: O(1), when the current is none
        """
        if current is None:
            return False  # Empty node is not considered a leaf node

        for i in range(8):
            if current.child[i] is not None:  # If any child is present,
                return False  # it's not a leaf node
        return True  # If no children are present, it's a leaf node


if __name__ == "__main__":
    tdbt = ThreeDeeBeeTree()
    tdbt[(3, 3, 3)] = "A"
    tdbt[(1, 5, 2)] = "B"
    tdbt[(4, 3, 1)] = "C"
    tdbt[(5, 4, 0)] = "D"
    print(tdbt.root.get_child_for_key((4, 3, 1)).subtree_size)  # 2