class TestFiniteAutomaton(unittest.TestCase):
    def test_automaton(self):
        states = ['0', '1', '2']
        alphabet = ['a', 'b']
        transitions = { 
            '0': {'a': '1', 'b': '1'}, 
            '1': {'a': '1', 'b': '2'}, 
            '2': {'a': '0', 'b': '2'}
        }
        initial_state = '0'
        final_states = ['2']

        automaton = FiniteAutomaton(states, alphabet, transitions, initial_state, final_states)

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

    def test_empty_string(self):
        # Test if the automaton accepts an empty string when the initial state is also a final state
        states = ['0']
        alphabet = ['a', 'b']
        transitions = {'0': {'a': '0', 'b': '0'}}
        initial_state = '0'
        final_states = ['0']

        automaton = FiniteAutomaton(states, alphabet, transitions, initial_state, final_states)

        self.assertTrue(automaton.accepts("")) 

    def test_single_state_non_final(self):
        # Test if the automaton rejects a non-empty string when there's only one state and it's not a final state
        states = ['0']
        alphabet = ['a', 'b']
        transitions = {'0': {'a': '0', 'b': '0'}}
        initial_state = '0'
        final_states = []

        automaton = FiniteAutomaton(states, alphabet, transitions, initial_state, final_states)

        self.assertFalse(automaton.accepts("a")) 

    def test_single_state_final(self):
        # Test if the automaton accepts a non-empty string when there's only one state and it's a final state
        states = ['0']
        alphabet = ['a', 'b']
        transitions = {'0': {'a': '0', 'b': '0'}}
        initial_state = '0'
        final_states = ['0']

        automaton = FiniteAutomaton(states, alphabet, transitions, initial_state, final_states)

        self.assertTrue(automaton.accepts("a")) 

    def test_invalid_symbol(self):
        # Test if the automaton rejects a string containing symbols not in the alphabet
        states = ['0', '1']
        alphabet = ['a', 'b']
        transitions = {'0': {'a': '0', 'b': '1'}, '1': {'a': '1', 'b': '1'}}
        initial_state = '0'
        final_states = ['1']

        automaton = FiniteAutomaton(states, alphabet, transitions, initial_state, final_states)

        self.assertFalse(automaton.accepts("abbc")) 
