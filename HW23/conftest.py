import sys

import pytest

sys.path.append('/home/helga/Hillel_QA/')

from HW23.structure_without_list import StructureWithoutList, Item
@pytest.fixture()
def default_structure():
    structure = StructureWithoutList ()
    return structure