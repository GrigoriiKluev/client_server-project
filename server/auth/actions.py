from .controllers import login_controller, registration_controller, logout_controller


actionnames = [
    {'action':'login', 'controller':login_controller},
    {'action':'registrate', 'controller':registration_controller},
    {'action':'logout', 'controller':logout_controller},
]
