import unittest
from finite_automaton import FiniteAutomaton, read_automaton

class TestFiniteAutomaton(unittest.TestCase):
    def test_automaton(self):
        automaton = FiniteAutomaton([0, 1, 2], ['a', 'b'], {0: {'a': 1, 'b': 1}, 1: {'a': 1, 'b': 2}, 2: {'a': 0, 'b': 2}}, 0, [1, 2])

        self.assertFalse(automaton.accepts("abbbba")) # 1
        self.assertTrue(automaton.accepts("aabbbb")) # 2
        self.assertTrue(automaton.accepts("bbabbabbabbb")) # 3
        self.assertTrue(automaton.accepts("bbbbbbbbb")) # 4
        self.assertFalse(automaton.accepts("-")) # 5
        self.assertFalse(automaton.accepts("abababababab")) # 6
        self.assertTrue(automaton.accepts("bbbbaabbbb")) # 7
        self.assertFalse(automaton.accepts("abba")) # 8
        self.assertFalse(automaton.accepts("a")) # 9
        self.assertFalse(automaton.accepts("aaa")) # 10


if __name__ == "__main__":
    unittest.main()
