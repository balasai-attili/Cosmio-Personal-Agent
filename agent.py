pending_action = None

def set_action(action):
    global pending_action
    pending_action = action

def get_action():
    return pending_action

def clear_action():
    global pending_action
    pending_action = None