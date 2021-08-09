import pytest
import math

def min_energy(heights):
    if (heights == []):
        return 0

    # find the max, and work backwards from there
    max_height = max(heights)
    first_max_index = heights.index(max_height)

    return min_energy_acc(heights[:first_max_index], max_height)

def min_energy_acc(heights, min_energy_needed):
    len_heights = len(heights)
    if (len_heights == 0):
        return min_energy_needed

    last_hurdle = heights[len_heights-1]
    starting_energy = min_energy_needed

    # min_starting_energy + boost = min_needed
    # min_starting_energy + (min_starting_energy - hurdle) = min_needed
    # 2*min_starting_energy = min_needed + hurdle
    # min_starting_energy = ceil((min_needed + hurdle) / 2)
    min_starting_energy = math.ceil((min_energy_needed + last_hurdle) /2)

    return min_energy_acc(heights[:-1], starting_energy)

def test_empty():
    m = min_energy([])
    assert(m == 0)

def test_single():
    m = min_energy([3])
    assert(m == 3)

def test_two():
    m = min_energy([3, 4])
    assert(m == 4)

    m = min_energy([3, 4, 3, 2, 4])
    assert(m == 4)

def test_same():
    assert(min_energy([4,4,4]) == 4)


