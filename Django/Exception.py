class RecordException(Exception):
    def __init__(self, message = "Unknown Record Error Occured"):
        self.message = message
        super().__init__(message)