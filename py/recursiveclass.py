class Recursive_Data:

    def __init__(self, arg1, arg2, arg3, indent = 0):

        self.val1 = arg1
        self.val2 = arg2
        self.val3 = arg3
        self.indent = indent

    def __str__(self) -> str:

        val1 = self.val1
        val2 = self.val2
        val3 = self.val3
        info = ('\t'*self.indent) + 'Value 1:\t'

        if isinstance(val1, Recursive_Data):
            val1.indent = self.indent + 1
            val1 = '\n\n' + val1.__str__()
        info += f'{val1}\n' + ('\t'*self.indent) + 'Value 2:\t'

        if isinstance(val2, Recursive_Data):
            val2.indent = self.indent + 1
            val2 = '\n\n' + val2.__str__()
        info += f'{val2}\n' + ('\t'*self.indent) + 'Value 3:\t'

        if isinstance(val3, Recursive_Data):
            val3.indent = self.indent + 1
            val3 = '\n\n' + val3.__str__()
        info += f'{val3}\n'

        return info
