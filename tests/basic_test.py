"""
Test case example.
"""


class TestBoolean:
    """Example test case"""

    @staticmethod
    def test_if_true_is_true():
        """Tests if True is really True"""

        # Given
        expected = True

        # When
        result = True  # True should be replaced by a function call

        # Then
        assert result == expected  # add assertion here

    @staticmethod
    def test_if_false_is_false():
        """Tests if False is really False"""

        # Given
        expected = False

        # When
        result = False  # True should be replaced by a function call

        # Then
        assert result == expected  # add assertion here
