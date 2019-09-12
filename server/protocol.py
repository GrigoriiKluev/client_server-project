"""
Protocol API Documentation
"""

def validate_request(raw):
    """

    :param raw: raw client request
    :return: Bool value - validation solution


    - Example ::

        {'action': 'echo', 'time': ''}
    """
    if 'action' in raw and 'time' in raw:
        return True
    return False


def make_response(request, code, data=None):
    """

    :param request:
    :param code:
    :param data:
    :return: Dictionary of params

    - Example ::
        {'action': request.get('action'),'time': request.get('time'),'data': data,'code': code}
    """
    return {
        'action': request.get('action'),
        'time': request.get('time'),
        'data': data,
        'code': code
    }
