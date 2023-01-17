import sys

import pytest

sys.path.append('/home/helga/Hillel_QA/')

from HW23.structure_without_list import StructureWithoutList, Item
@pytest.fixture()
def default_structure():
    structure = StructureWithoutList()
    return structure

@pytest.fixture()
def structure_with_three_items(default_structure):
    default_structure.add('one')
    default_structure.add('two')
    default_structure.add('three')
    return default_structure
