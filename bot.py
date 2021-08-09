import pytest

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

    while (is_energy_enough_for_next_jump(min_energy_needed, last_hurdle, starting_energy - 1)):
        # I can probably optimise this to calculate the exact min starting energy I need
        starting_energy = starting_energy -1

    return min_energy_acc(heights[:-1], starting_energy)

def is_energy_enough_for_next_jump(min_energy_needed, prev_hurdle, starting_energy):
    if (starting_energy < prev_hurdle):
        return False

    boost = starting_energy - prev_hurdle
    if (starting_energy + boost >= min_energy_needed):
        return True
    else:
        return False
    

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

def test_starting_energy_thing():
    assert(is_energy_enough_for_next_jump(4, 3, 4) == True)
    assert(is_energy_enough_for_next_jump(4, 3, 3) == False)
    assert(is_energy_enough_for_next_jump(4, 2, 3) == True)
    assert(is_energy_enough_for_next_jump(4, 2, 2) == False)
    assert(is_energy_enough_for_next_jump(4, 4, 4) == True)


