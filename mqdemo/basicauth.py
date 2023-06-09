"""An incredibly simple HTTP basic auth implementation."""


from base64 import b64decode, b64encode
from urllib.parse import quote, unquote


class DecodeError(Exception):
    pass


class EncodeError(Exception):
    pass


def encode(username, password):
    """Returns an HTTP basic authentication encrypted string given a valid
    username and password.
    """
    if ':' in username:
        raise EncodeError

    username_password = f'{quote(username)}:{quote(password)}'
    return f'Basic {b64encode(username_password.encode()).decode()}'


def decode(encoded_str):
    """Decode an encrypted HTTP basic authentication string. Returns a tuple of
    the form (username, password), and raises a DecodeError exception if
    nothing could be decoded.
    """
    split = encoded_str.strip().split(' ')

    # If split is only one element, try to decode the username and password
    # directly.
    if len(split) == 1:
        try:
            username, password = b64decode(split[0]).decode().split(':', 1)
        except:
            raise DecodeError

    # If there are only two elements, check the first and ensure it says
    # 'basic' so that we know we're about to decode the right thing. If not,
    # bail out.
    elif len(split) == 2:
        if split[0].strip().lower() == 'basic':
            try:
                username, password = b64decode(split[1]).decode().split(':', 1)
            except:
                raise DecodeError
        else:
            raise DecodeError

    # If there are more than 2 elements, something crazy must be happening.
    # Bail.
    else:
        raise DecodeError

    return unquote(username), unquote(password)
