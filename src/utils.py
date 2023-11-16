import argparse

class CustomAction(argparse.Action):
    """
    Custom action to store arguments in the order they are passed in. 
    Taken from https://stackoverflow.com/questions/9027028/argparse-argument-order. 
    """
    def __call__(self, parser, namespace, values, option_string=None):
        if not 'ordered_args' in namespace:
            setattr(namespace, 'ordered_args', [])
        previous = namespace.ordered_args
        previous.append((self.dest, values))
        setattr(namespace, 'ordered_args', previous)
