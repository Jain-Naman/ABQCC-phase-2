from westpy.qdet import QDETResult

effective_hamiltonian = QDETResult(filename='west.wfreq.save/wfreq.json')

print(effective_hamiltonian)

fermionic_operator = effective_hamiltonian.make_fermionic_operator()

print(fermionic_operator)
