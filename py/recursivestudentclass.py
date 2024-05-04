class Student:

    def __init__(self, name, age, roll, gender = "Male", indent = 0):
        self.name = name
        self.age = age
        self.roll = roll
        self.gender = gender
        self.indent = indent
    
    def print(self) -> str:
        name = self.name
        age = self.age
        roll = self.roll
        sex = self.gender
        info = ('\t'*self.indent) + 'Full Legal Name:\t'
        if isinstance(name, Student):
            name.indent = self.indent + 1
            name = '\n\n' + name.print()
        info += f'{name}\n' + ('\t'*self.indent) + 'Age:\t\t\t'
        if isinstance(age, Student):
            age.indent = self.indent + 1
            age = '\n\n' + age.print()
        info += f'{age}\n' + ('\t'*self.indent) + 'Enrollment number:\t'
        if isinstance(roll, Student):
            roll.indent = self.indent + 1
            roll = '\n\n' + roll.print()
        info += f'{roll}\n' + ('\t'*self.indent) + 'Sex/Gender:\t\t'
        if isinstance(sex, Student):
            sex.indent = self.indent + 1
            sex = '\n\n' + sex.print()
        info += f'{sex}\n'
        return info
