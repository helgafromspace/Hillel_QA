import sys
import pytest

sys.path.append('/home/helga/Hillel_QA/')

from HW23.structure_without_list import StructureWithoutList, Item

def test_object_initial_length(default_structure):
    assert default_structure.length == 0

@pytest.mark.parametrize('value',['','string', 1, [], (), {}, None, True])
def test_structure_length_after_adding_item(value, default_structure):
    default_structure.add(value)
    assert default_structure.length == 1

def test_values_of_added_items_are_correct(structure_with_three_items):
    item1 = structure_with_three_items.get(1)
    item2 = structure_with_three_items.get(2)
    item3 = structure_with_three_items.get(3)
    assert item1 == 'one'
    assert item2 == 'two'
    assert item3 == 'three'

@pytest.mark.parametrize('index',[0,2])
def test_get_item_with_index_out_of_range_causes_exception(index, default_structure):
    with pytest.raises(IndexError) as ind:
        default_structure.get(index)

def test_delete_first_item_from_list_of_3_items(structure_with_three_items):
    structure_with_three_items.delete(1)
    assert structure_with_three_items.length == 2
    assert structure_with_three_items.get(1) == 'two'
    assert structure_with_three_items.get(2) == 'three'

def test_delete_last_item_from_list_of_3_items(structure_with_three_items):
    structure_with_three_items.delete(3)
    assert structure_with_three_items.length == 2
    assert structure_with_three_items.get(1) == 'one'
    assert structure_with_three_items.get(2) == 'two'

def test_delete_middle_item_from_list_of_3_items(structure_with_three_items):
    structure_with_three_items.delete(2)
    assert structure_with_three_items.length == 2
    assert structure_with_three_items.get(1) == 'one'
    assert structure_with_three_items.get(2) == 'three'

def test_delete_all_items_in_order_from_three_to_one(structure_with_three_items):
    structure_with_three_items.delete(3)
    structure_with_three_items.delete(2)
    structure_with_three_items.delete(1)
    assert structure_with_three_items.length == 0

@pytest.mark.parametrize('index',[0, 1, 2])
def test_delete_item_with_index_out_of_range_causes_exception(index, default_structure):
    with pytest.raises(IndexError):
        default_structure.delete(index)

@pytest.mark.xfail(reason = 'Bug: incorrect element insertion after deleting first element in collection')
def test_add_item_after_deleting_first_item_in_collection(structure_with_three_items):
    structure_with_three_items.delete(1)
    structure_with_three_items.add('four')
    assert structure_with_three_items.length == 3
    assert structure_with_three_items.get(1) == 'two'
    assert structure_with_three_items.get(2) == 'three'
    assert structure_with_three_items.get(3) == 'four'

def test_add_item_after_deleting_last_item_in_collection_of_3_element(structure_with_three_items):
    structure_with_three_items.delete(3)
    structure_with_three_items.add('four')
    assert structure_with_three_items.length == 3
    assert structure_with_three_items.get(1) == 'one'
    assert structure_with_three_items.get(2) == 'two'
    assert structure_with_three_items.get(3) == 'four'

@pytest.mark.xfail(reason = 'Bug: incorrect element insertion after deleting middle element in collection')
def test_add_item_after_deleting_middle_item_in_collection_of_3_element(structure_with_three_items):
    structure_with_three_items.delete(2)
    structure_with_three_items.add('four')
    assert structure_with_three_items.length == 3
    assert structure_with_three_items.get(1) == 'one'
    assert structure_with_three_items.get(2) == 'three'
    assert structure_with_three_items.get(3) == 'four'





