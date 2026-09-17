ACTIVE = "active"
DORMANT = "dormant"
NEXUS = "nexus"
TERMINATED = "terminated"

current_state = ACTIVE


def set_state(new_state):

    global current_state

    current_state = new_state


def get_state():

    return current_state