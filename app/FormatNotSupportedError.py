class FormatNotSupportedError(Exception):
    def __init__(self, message,code):
        super().__init__(message)
        self.code    = code
        self.message = message

    def __str__(self):
        return f"{self.message}"