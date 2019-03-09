'''
pyscience - python science programming
Copyright (c) 2019 Manuel Alcaraz Zambrano

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from pyscience.units.unitparser import UnitParser

UNITS = UnitParser()
UNITS = UNITS.parse()

def convert(value):
    result = ''
    
    for x in list(value):
        if x == '*':
            result += '/'
        elif x == '/':
            result += '*'
        elif x == '+':
            result += '-'
        elif x == '-':
            result += '+'
        else:
            result += x
    
    return result

class Unit:
    '''TODO: Units is very unstable and may change its API in next releases
    TODO: This module is experimental and may not work well.
    '''
    def __init__(self, type_='', name=None, value=1, prefix=None, unit=None, offset=0, factor=1):
        self.type_ = type_
        self.name = name
        self.value = value
        self.prefix = prefix
        self.unit = unit
        self.offset = offset
        self.factor = factor
    
    def to(self, unit):
        if not isinstance(unit, Unit):
            raise TypeError('unit must be a Unit class')
        
        if not unit.type_ == self.type_: # TODO
            raise TypeError('Cannot convert unit to ' + unit.type_)
        
        if self.name == unit.name:
            return self
        
        if self.prefix and unit.prefix:
            a, b = 1, 1
            for x in UNITS['prefix']:
                if x['symbol'] == self.prefix:
                    a = float(x['value'])
                    break
            for x in UNITS['prefix']:
                if x['symbol'] == unit.prefix:
                    b = float(x['value'])
                    break
            new_value = self.value * a / b
            return Unit(name=unit.name, value=new_value, prefix=unit.prefix)
        else:
            for mag in UNITS['magnitude']:
                if self.name in mag['units'] or self.name == mag['unit']:
                    
                    target_unit = {'factor': unit.factor, 'offset': unit.offset}
                    
                    if self.name in mag['units']:
                        source_unit = mag['units'][self.name]
                    else:
                        source_unit = mag['unit']
                    #
                    result = self.value
                    
                    if source_unit['offset']:
                        result += source_unit['offset']
                    
                    result *= source_unit['factor']
                    #
                    result /= target_unit['factor']
                    
                    if target_unit['offset']:
                        result -= target_unit['offset']
                    
                    result = round(result, 3)
                    return Unit(name=unit.name, value=result)
                
            raise BaseException
    
    def __rmul__(self, value):
        return Unit(name=self.name, value=value, prefix=self.prefix, offset=self.offset)
    
    def __str__(self):
        return f'{self.value} {self.name}'
    
    def __repr__(self):
        return f'<Unit {self.value} {self.unit} offset {self.offset} factor {self.factor}>'

class Units:
    
    def __init__(self):
        pass
    
    def __getattr__(self, name):
        #if name in tuple([x['unit'] for x in UNITS['magnitude']]):
        #    return Unit(name=name, prefix=None, unit=name)
        
        if name.startswith(tuple([x['symbol'] for x in UNITS['prefix']])):
            for mag in UNITS['magnitude']:
                if mag['use_prefixes'] and name[1:] == mag['unit']:
                    print('adios')
                    return Unit(name=name, prefix=name[0], unit=name[1:])
                #elif name in mag['units']:
                #    print('hola')
                #    return Unit(name=name, unit=name)
        
        for mag in UNITS['magnitude']:
            if name in mag['units']:
                #print(mag)
                return Unit(name=name, unit=name, offset=mag['units'][name]['offset'], factor=mag['units'][name]['factor'])
        
        raise ValueError(f'Unit "{name}" does not exit') # Or it is not implemented yet

