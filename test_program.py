import sys


def test_python_version():
    """Test that Python version is available."""
    assert sys.version is not None
    assert len(sys.version) > 0
