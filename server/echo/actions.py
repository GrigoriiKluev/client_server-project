from .controllers import (
    echo_controller,get_messages_controller,update_message_controller, delete_message_controller)







actionnames = [
{'action': 'echo', 'controller': echo_controller},
{'action': 'allmessages', 'controller': get_messages_controller},
{'action': ' update', 'controller': update_message_controller},
{'action': ' delete', 'controller': delete_message_controller}
]
