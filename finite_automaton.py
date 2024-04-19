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
        FiniteAutomaton: Object representing the read automaton.
    """
    num_states = int(input("Number of states (1 <= n <= 10): "))
    if num_states < 1 or num_states > 10:
        print("Number of states must be between 1 and 10.")
        return 1
    else:
        states = [chr(ord('0') + i) for i in range(num_states)]

    alphabet = input("Enter the terminal symbols, separated by space (example: 2 a b): ").split()[1:11]
    
    acceptance_states = [x for x in input("Enter the acceptance states (0 to 9) separated by space: ").split()[1:11]]
    
    num_transitions = int(input("Number of transitions (maximum 50): "))
    transitions = {}

    for _ in range(num_transitions):
        transition = input("Enter the transition in the format q x q', where q, q' ∈ Q, x ∈ Σ ∪ {-}: ").split()
        current_state, symbol, next_state = transition
        if current_state not in transitions:
            transitions[current_state] = {}
        transitions[current_state][symbol] = next_state

    return FiniteAutomaton(states, alphabet, transitions, '0', acceptance_states)

if __name__ == "__main__":
    automaton = read_automaton()

    num_strings = int(input("Number of input strings (maximum 10): "))
    strings = [input(f"Enter string {i+1}: ")[:20] for i in range(num_strings)]

    for string in strings:
        if automaton.accepts(string):
            print("aceita")
        else:
            print("rejeita")
