import sys
import pytest
from HW23.structure_without_list import StructureWithoutList, Item

sys.path.append('/home/helga/Hillel_QA/')


def test_initial_length(default_structure):
    assert default_structure.length == 0

def test_item_values(default_structure):
    default_structure.add('item1')
    num1 = default_structure.get(1)
    default_structure.add('item2')
    num2 = default_structure.get(2)
    default_structure.add('item3')
    num3 = default_structure.get(3)
    assert num1 == default_structure._current_item.prev_item.prev_item.value
    assert num2 == default_structure._current_item.prev_item.value
    assert num3 == default_structure._current_item.value

    # assert default_structure._current_item.prev_item.value == default_structure.get(2)
@pytest.mark.parametrize('value',['','string', 1, [], (), {}, None, True])
def test_structure_length_after_adding_item(value, default_structure):
    default_structure.add(value)
    assert default_structure.length == 1

def test_get_value_by_index(default_structure):
    default_structure.add('item1')
    num = default_structure.get(1)
    assert default_structure._current_item.value == num
    assert default_structure._current_item.prev_item == None
def test_value_of_added_item_is_correct(default_structure):
    default_structure.add('a')
    num = default_structure.get(1)
    assert num == 'a'
@pytest.mark.parametrize('index',[0,2])
def test_get_item_with_index_out_of_range_causes_exception(index, default_structure):
    with pytest.raises(IndexError) as ind:
        default_structure.get(index)
    assert ind.typename == 'IndexError'

def test_delete_item_if_length_equals_1(default_structure):
    default_structure.add('one')
    default_structure.delete(1)
    assert default_structure.length == 0
    assert default_structure._current_item == None
    assert default_structure._current_index == 0
def test_delete_item_from_list_of_3_items(default_structure):
    default_structure.add('one')
    default_structure.add('two')
    default_structure.add('three')
    default_structure.delete(1)
    assert default_structure.length == 2
    assert default_structure.get(1) == 'two'
    assert default_structure.get(2) == 'three'
    assert default_structure._current_item.value == 'three'
    assert default_structure._current_item.prev_item.value == 'two'
    assert default_structure._current_item.prev_item.prev_item == None
    assert default_structure._current_item.next_item == None
@pytest.mark.parametrize('index',[0, 1, 2])
def test_delete_item_with_index_out_of_range_causes_exception(index, default_structure):
    with pytest.raises(IndexError) as ind:
        default_structure.delete(index)
    assert ind.typename == 'IndexError'




