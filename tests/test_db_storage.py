# tests/test_models/test_engine/test_db_storage.py
import unittest
from models import storage
from models.state import State

class TestDBStorage(unittest.TestCase):
    """Tests for DBStorage class."""

    def test_get(self):
        """Test the get method."""
        new_state = State(name="California")
        new_state.save()
        state = storage.get(State, new_state.id)
        self.assertIsNotNone(state)
        self.assertEqual(state.id, new_state.id)

    def test_count(self):
        """Test the count method."""
        count_before = storage.count(State)
        new_state = State(name="New York")
        new_state.save()
        count_after = storage.count(State)
        self.assertEqual(count_after, count_before + 1)

if __name__ == "__main__":
    unittest.main()
