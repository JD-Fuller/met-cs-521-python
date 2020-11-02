"""
Marc Lowenthal
Class: CS 521
Date:
Class Object Example Mug.py
"""

import datetime
import sys

class Mug():
    '''This class constructs the Mug Object and its contents'''
    def __init__(self, color, material='ceramic', contents='water'):
        self.__units = 'F'
        self.__tempf = None
        assert isinstance(material, str), 'material not string!'

        self.color = color
        self.material = material
        self.contents = contents
        # Keep track of the created timestamp as a private attribute
        self.__created_ts = datetime.datetime.now()

    def __repr__(self):
        return ("Marc's {color} {mat} mug contains {cont} at {temp:,.1f}"
                " degrees {units} as of {ts}.".format(
                    color=self.color,
                    mat=self.material,
                    cont=self.contents,
                    temp=self.get_temp(),
                    units='Fahrenheit' if self.__units == 'F' else 'Celsius',
                    ts=self.__created_ts.strftime('%Y-%m-%d %H:%M:%S')))

    def set_as_fahrenheit(self):
        '''set temperature units to Fahrenheit'''
        self.__units = 'F'
        return self

    def set_as_celsius(self):
        '''set temperature units to Celsius'''
        self.__units = 'C'
        #return self

    def set_temp(self, temp):
        ''' set the temp of the mug contents'''
        if self.__units == 'F':
            self.__tempf = temp
        elif self.__units == 'C':
            self.__tempf = temp * 9/5 + 32
        else:
            assert False, 'Temperature Units Not Set'
        return self

    def __get_tempf(self):
        '''return the temperature'''
        if self.__tempf is None:
            assert False, 'Temperature Not Set'
        return self.__tempf

    def __get_tempc(self):
        '''return the temperature'''
        return (self.__tempf - 32) * 5/9

    def get_temp(self):
        '''return the temperature'''
        if self.__units == 'F':
            return self.__get_tempf()
        elif self.__units == 'C':
            return self.__get_tempc()
        else:
            assert False, 'Temperature Units Not Set'

    def __len__(self):
        return len(self.color)


    def __add__(self, other):
        """
        This Creates a new mug from two other mugs
        It uses the first mug's color, the second mug's material,
        blends the contents and chooses the average temperature.
        """
        c = Mug(self.color, material=other.material,
                contents="{}+{}".format(self.contents, other.contents))
        c.set_temp((self.get_temp() + other.get_temp())/2)
        return c


# Unit Tests
if __name__ == '__main__':

    tempf = 212
    tempc = 100
    karen_temp = 58

    # instantiate mug object
    marc_mug = Mug('blue', contents='tea')
    karen_mug = Mug('clear', contents='wine', material='glass')

    # set temperature
    marc_mug.set_temp(tempf)

    # Assert Tests
    assert marc_mug.get_temp() == tempf, (
        'Error matching temperatures {} != {}'.format(marc_mug.get_temp(), tempf))

    # Switch Temp to celsius and check temperature conversion
    marc_mug.set_as_celsius()
    assert marc_mug.get_temp() == tempc, (
        'Error matching temperatures {} != {}'.format(marc_mug.get_temp(), tempf))

    marc_mug.set_as_fahrenheit()

    # Testing the magic add method
    karen_mug.set_temp(karen_temp)
    new_mug = marc_mug + karen_mug
    assert new_mug.color == marc_mug.color, 'Add created incorrect color'
    assert new_mug.material == karen_mug.material, 'Add created incorrect material'
    assert new_mug.contents == 'tea+wine', 'Add created incorrect contents'
    assert new_mug.get_temp() == (marc_mug.get_temp()+karen_mug.get_temp())/2, (
        'Add created incorrect temperature')

    print('Mug Class Tests All Passed!')

    # #####################################################
    # Not part of a unit test, just here for illustration!

    # This will use __str__()
    print(marc_mug)

    marc_mug.contents = 'hot chocolate'
    marc_mug.set_as_celsius()

    print(marc_mug)