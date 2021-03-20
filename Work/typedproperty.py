#!/usr/bin/env python
# typedproperty.py

def typedproperty(name, expected_type):
    private_name = '_' + name

    @property
    def prop(self):
        print(f'get{private_name}')
        return getattr(self, private_name)

    @prop.setter
    def prop(self, value):
        print(f'set{private_name}')
        if not isinstance(value, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, value)

    return prop

String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)
