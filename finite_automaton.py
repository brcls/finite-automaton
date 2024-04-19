class FiniteAutomaton:
    """
    Class representing a deterministic finite automaton (DFA).

    Attributes:
        states (list): List of states of the automaton.
        alphabet (list): List of symbols of the automaton's alphabet.
        transitions (dict): Dictionary representing the transitions of the automaton.
            The keys are the current states, and the values are dictionaries
            whose keys are symbols from the alphabet and values are the
            states reachable after the transition.
        initial_state (str): Initial state of the automaton.
        final_states (list): List of acceptance states of the automaton.
    """

    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        """
        Initializes a finite automaton.

        Args:
            states (list): List of states of the automaton.
            alphabet (list): List of symbols of the automaton's alphabet.
            transitions (dict): Dictionary representing the transitions of the automaton.
                The keys are the current states, and the values are dictionaries
                whose keys are symbols from the alphabet and values are the
                states reachable after the transition.
            initial_state (str): Initial state of the automaton.
            final_states (list): List of acceptance states of the automaton.
        """
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

    def transition(self, state, symbol):
        """
        Performs a transition in the automaton.

        Args:
            state (str): Current state.
            symbol (str): Input symbol.

        Returns:
            str: Next state after the transition, or None if there is no transition
                defined for the current state with the provided symbol.
        """
        if state in self.transitions and symbol in self.transitions[state]:
            return self.transitions[state][symbol]
        else:
            return None

    def accepts(self, string):
        """
        Checks if a string is accepted by the automaton.

        Args:
            string (str): Input string.

        Returns:
            bool: True if the string is accepted, False otherwise.
        """
        current_state = self.initial_state
        for symbol in string:
            current_state = self.transition(current_state, symbol)
            if current_state is None:
                return False
        return current_state in self.final_states


def read_automaton():
    """
    Function to read the information of an automaton from user input.

    Returns:
        FiniteAutomaton or int: Object representing the read automaton if input is valid,
                                otherwise raises a ValueError.
    """
    try:
        # Read the number of states
        num_states = int(input("Number of states (1 <= n <= 10): "))
        if num_states < 1 or num_states > 10:
            raise ValueError("Number of states must be between 1 and 10.")

        states = [chr(ord('0') + i) for i in range(num_states)]  # Naming states as '0', '1', ..., '9'

        # Read the alphabet symbols
        alphabet = input("Enter the number of terminal symbols, and then what they are, separated by space, example: 2 a b (maximum 10): ").split()[1:]
        if len(alphabet) > 10:
            raise ValueError("Number of alphabet symbols must be at most 10.")

        # Read the acceptance states
        acceptance_states = [x for x in input("Enter the acceptance states (0 to 9) separated by space (1 <= n <= number of states): ").split()[1:]]
        acceptance_states_set = set(acceptance_states)
        states_set = set(states)

        if len(acceptance_states) > num_states:
            raise ValueError("The number of acceptance states must be within the limit of the number of states.")
        elif acceptance_states_set - states_set:
            raise ValueError("The acceptance states must be included in the states list.")

        # Read the number of transitions
        num_transitions = int(input("Number of transitions (maximum 50): "))
        if num_transitions > 50:
            raise ValueError("Number of transitions must be at most 50.")

        transitions = {}

        # Read the transitions
        for _ in range(num_transitions):
            transition = input("Enter the transition in the format q x q', where q, q' ∈ Q, x ∈ Σ ∪ {-}: ").split()[:3]
            current_state, symbol, next_state = transition

            if current_state not in transitions:
                transitions[current_state] = {}
            transitions[current_state][symbol] = next_state

        return FiniteAutomaton(states, alphabet, transitions, '0', acceptance_states)

    except ValueError as e:
        print("Error while reading automaton:", e)
        return 1  # Return a dummy value to indicate error


def read_strings():
    """
    Function to read input strings from user input.

    Returns:
        list: List of input strings, each string limited to 20 characters,
              or raises a ValueError if input is invalid.
    """
    try:
        # Read input strings
        num_strings = int(input("Number of input strings (maximum 10): "))
        if num_strings > 10:
            raise ValueError("Number of strings must be at most 10.")

        strings = [input(f"Enter string {i+1}: ")[:20] for i in range(num_strings)]

        return strings

    except ValueError as e:
        print("Error while reading input strings:", e)
        return []


if __name__ == "__main__":
    try:
        automaton = read_automaton()
        if automaton == 1:  # Check if automaton reading failed
            raise ValueError("Automaton reading failed.")
        
        strings = read_strings()

        # Test each input string against the automaton
        for string in strings:
            if automaton.accepts(string):
                print("aceita")  # Accepts the string
            else:
                print("rejeita")  # Rejects the string

    except ValueError as e:
        print("Exception encountered:", e)
