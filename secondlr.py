DFA_GRAPH = {1: {'dlm': 2, 'ltr': 2, "cfr": 2},
             2: {'dlm': 3, 'ltr': 3, "cfr": 2},
             3: {'dlm': 4, 'ltr': 4, "cfr": 4},
             4: {'dlm': 6, 'ltr': 5, "cfr": 5},
             5: {'dlm': 6, 'ltr': 6, "cfr": 6},
             6: {'dlm': 7, 'ltr': 7, "cfr": 7},
             7: {'dlm': 8, 'ltr': 8, "cfr": 8},
             8: {'dlm': 8, 'ltr': 3, "cfr": 9}}

POSSIBLE_SIGNALS = ['dlm', 'ltr', 'cfr']


def dfa_foo(control_signals, starting_point=1, graph=DFA_GRAPH):
    history, str_to_print, current_state = list(), str(), list(graph.keys())[starting_point - 1]
    history.append(current_state)
    for i in range(len(control_signals)):
        if control_signals[i] in POSSIBLE_SIGNALS:
            current_state = list(graph.values())[history[-1] - 1][control_signals[i]]
        history.append(current_state)
    history = [i+1 for i in history]
    for i in range(len(control_signals)):
        str_to_print += f" {history[i]}({control_signals[i]})---> "
    print(f"\n{str_to_print + str(history[-1])} ")


