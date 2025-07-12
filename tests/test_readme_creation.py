import pytest
from unittest.mock import patch
from codemate.core import create_readme

"""
@patch("codemate.core.open")
def test_readme_creation(mock_obj):
    mock_obj.return_value = "README.md"
    
"""


def test_file_creation(tmp_path):
    file = create_readme(tmp_path)
    assert file.exists()







