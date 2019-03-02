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

# TODO: Units is very unstable and may change its API in next releases

LONGITUDE_UNITS = ['km', 'hm', 'dam', 'm', 'dm', 'cm', 'mm']
LONGITUDE = {
    'km': 1000,
    'hm': 100,
    'dam': 10,
    'm': 1,
    'dm': .1,
    'cm': .01,
    'mm': .001
}
TIME_UNITS = ['year', 'month', 'week', 'day', 'hour', 'minute', 'second']
TIME = {
    'year': 6622560000,
    'month': 18144000,
    'week': 604800,
    'day': 86400,
    'hour': 3600,
    'minute': 60,
    'second': 1 
}

UNITS = {
    'longitude': LONGITUDE,
    'time': TIME
    }

class Unit:
    
    def __init__(self, type_, name, value=None):
        self.type_ = type_
        self.name = name
        self.value = value
    
    def to(self, unit):
        if not isinstance(unit, Unit):
            raise TypeError('unit must be a Unit class')
        
        if not unit.type_ == self.type_:
            raise TypeError('Cannot convert unit to ' + unit.type_)
        
        unit_list = UNITS[self.type_]
        
        new_value = self.value * unit_list[self.name] / unit_list[unit.name]
        return Unit(self.type_, unit.name, new_value)
    
    def __rmul__(self, value):
        return Unit(self.type_, self.name, value)
    
    def __str__(self):
        return f'{self.value} {self.name}'
    
    def __repr__(self):
        return '<Unit ' + str(self) + '>'

class Units:
    
    def __init__(self):
        pass
    
    def __getattr__(self, name):
        if name in LONGITUDE_UNITS:
            return Unit('longitude', name)
        elif name in TIME_UNITS:
            return Unit('time', name)

