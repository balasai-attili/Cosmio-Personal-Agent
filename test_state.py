import state

print(state.get_state())

state.set_state(
    state.DORMANT
)

print(state.get_state())