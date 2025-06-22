import pytest

from business.helpers import get_value


class TestGetValue:
    """Tests for the get_value function."""

    @pytest.fixture(scope="class")
    def sample_input(self) -> str:
        """Provides a sample input string for the tests."""
        return "World"

    def test_get_value_with_fixture(self, sample_input: str):
        """Tests get_value returns the expected string using a class fixture."""
        expected_output = f"business.helpers from: {sample_input}"
        assert get_value(sample_input) == expected_output
