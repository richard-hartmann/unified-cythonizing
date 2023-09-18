class Fooby:
    def __init__(self):
        self.str = "a Fooby class"

    def __call__(self, *args, **kwargs):
        return self.str
