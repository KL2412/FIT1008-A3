from __future__ import annotations
from threedeebeetree import Point
from ratio import Percentiles


def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:
    """
    Time Complexity:
    - Worst case: O(O(N*log(N)*log(N)), where N is the length of my_coordinate_list
    - Best case: O(len(points)), when the length of the my_coordinate_list is less than or equal to 6
    """
    def _octant_index(point, root):
        """
        This function returns the octant index of a point that
        represents the region in which the point resides in a space.
        If octant_index > 0, the point is in the positive half of the axis.

        Time Complexity:
        - Best case = Worst case: O(1)
        """
        octant_index = 0
        if point[0] > root[0]:
            octant_index += 1
        if point[1] > root[1]:
            octant_index += 2
        if point[2] > root[2]:
            octant_index += 4
        return octant_index

    def ordering_aux(points, result):
        """
        Auxiliary method for ordering the list in a balance way

        Time Complexity:
        - Worst case: O(N*log(N)*log(N)), where N is the length of my_coordinate_list
                N : when iterating through points to add them into percentile objects
                log N: when checking for the common points in three lists created by ratio method
                log N: recursion for log N times

        - Best case: O(len(points)), when the length of the my_coordinate_list is less than or equal to 6
        """
        if len(points) <= 17:  # Base case: return the points with its pointers
            result.extend(points)  # O(k), where k is the length of list
            return points

        x_percentile = Percentiles()
        y_percentile = Percentiles()
        z_percentile = Percentiles()

        for point in points:
            x_percentile.add_point((point[0], point))
            y_percentile.add_point((point[1], point))
            z_percentile.add_point((point[2], point))

        ratio = (1 / 7) * 100
        x_list = x_percentile.ratio(ratio, ratio)
        y_list = y_percentile.ratio(ratio, ratio)
        z_list = z_percentile.ratio(ratio, ratio)
        
        root = points[0]
        for point in points:
            if (point[0], point) in x_list and (point[1], point) in y_list and (point[2], point) in z_list:
                root = point
                result.append(root)
                points.remove(root)
                break
        
        octants = [[] for _ in range(8)]
        for point in points:
            octants[_octant_index(point, root)].append(point)

        for i in range(8):
            ordering_aux(octants[i], result)

    result = []
    ordering_aux(my_coordinate_list, result)
    return result