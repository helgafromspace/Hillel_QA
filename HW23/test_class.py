import sys
import pytest

sys.path.append('/home/helga/Hillel_QA/')

from HW23.structure_without_list import StructureWithoutList, Item
def test_object_initial_length(default_structure):
    assert default_structure.length == 0

    # assert default_structure._current_item.prev_item.value == default_structure.get(2)
@pytest.mark.parametrize('value',['','string', 1, [], (), {}, None, True])
def test_structure_length_after_adding_item(value, default_structure):
    default_structure.add(value)
    assert default_structure.length == 1

def test_values_of_added_items_are_correct(default_structure, add_three_items):
    item1 = default_structure.get(1)
    item2 = default_structure.get(2)
    item3 = default_structure.get(3)
    assert item1 == 'one'
    assert item2 == 'two'
    assert item3 == 'three'

@pytest.mark.parametrize('index',[0,2])
def test_get_item_with_index_out_of_range_causes_exception(index, default_structure):
    with pytest.raises(IndexError) as ind:
        default_structure.get(index)
def test_delete_item_if_length_equals_1(default_structure):
    default_structure.add('one')
    default_structure.delete(1)
    assert default_structure.length == 0

def test_delete_first_item_from_list_of_3_items(default_structure, add_three_items):
    default_structure.delete(1)
    assert default_structure.length == 2
    assert default_structure.get(1) == 'two'
    assert default_structure.get(2) == 'three'

def test_delete_last_item_from_list_of_3_items(default_structure, add_three_items):
    default_structure.delete(3)
    assert default_structure.length == 2
    assert default_structure.get(1) == 'one'
    assert default_structure.get(2) == 'two'

def test_delete_middle_item_from_list_of_3_items(default_structure, add_three_items):
    default_structure.delete(2)
    assert default_structure.length == 2
    assert default_structure.get(1) == 'one'
    assert default_structure.get(2) == 'three'
@pytest.mark.parametrize('index',[0, 1, 2])
def test_delete_item_with_index_out_of_range_causes_exception(index, default_structure):
    with pytest.raises(IndexError) as ind:
        default_structure.delete(index)
@pytest.mark.xfail(reason = 'Bug: incorrect element insertion after deleting first element in collection')
def test_add_item_after_deleting_first_item_in_collection(default_structure, add_three_items):
    default_structure.delete(1)
    default_structure.add('four')
    assert default_structure.length == 3
    assert default_structure.get(1) == 'two'
    assert default_structure.get(2) == 'three'
    assert default_structure.get(3) == 'four'

def test_add_item_after_deleting_last_item_in_collection_of_3_element(default_structure, add_three_items):
    default_structure.delete(3)
    default_structure.add('four')
    assert default_structure.length == 3
    assert default_structure.get(1) == 'one'
    assert default_structure.get(2) == 'two'
    assert default_structure.get(3) == 'four'

@pytest.mark.xfail(reason = 'Bug: incorrect element insertion after deleting middle element in collection')
def test_add_item_after_deleting_middle_item_in_collection_of_3_element(default_structure, add_three_items):
    default_structure.delete(2)
    default_structure.add('four')
    assert default_structure.length == 3
    assert default_structure.get(1) == 'one'
    assert default_structure.get(2) == 'three'
    assert default_structure.get(3) == 'four'





