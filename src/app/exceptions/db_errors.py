class NotFoundException(Exception):
    def __init__(self, message):
        self.message = message


class DuplicationException(Exception):
    def __init__(self, message):
        self.message = message
