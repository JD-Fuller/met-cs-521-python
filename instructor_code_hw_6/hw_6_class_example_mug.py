import datetime
import sys


class Mug():
    """This class constructs the Mug Object and its contents"""

    def __init__(self, color, material='ceramic', contents='water'):
        self.__units = 'F'
        self.__tempf = None
        assert isinstance(material, str), 'material not string!'

        self.color = color
        self.material = material
        self.contents = contents
        # Keep track of the created timestamp as a private attribute
        self.__created_ts = datetime.datetime.now()

    def __str__(self):
        return ("Marc's {color} {mat} mug containts {cont} at {temp:,.1f}"
                "degrees {units} as of {ts}.".format(
            color=self.color,
            mat=self.material,
            cont=self.contents,
            temp=self.get_temp(),
            units='Fahrenheit' if self.__units == 'F' else 'Celsius',
            ts=self.__created_ts.strftime('%Y-%m-%d %H:%M:%S')))

    def set_as_fahrenheit(self):
        """set temperature units to Fahrenheit"""
        self.__units = 'F'
        return self

    def set_as_celsius(self):
        '''Set temperature units to celsius'''
        self.__units = 'C'
        return self

    def set_temp(self, temp):
        """set the temp of the mug contents"""
        if self.__units == 'F':
            self.__tempf = temp
        elif self.__units == 'C':
            self.__tempf = temp * 9 / 5 + 32
        else:
            assert False, 'Temperature units not set'
        return self

    def get_tempf(self):
        """return the temp"""
        if self.__tempf is None:
            assert False, 'Temperature is not set'
        return self.__tempf

    def __get_tempc(self):
        '''return the temp in celcius'''
        return (self.__tempf - 32)*5/9

    def get_temp(self):
        '''return the temp'''
        if self.__units == 'F':
            return self.__get_tempf()
        elif self.__units == 'C':
            return self.__get_tempc()
        else:
            assert False, 'Temperature Units Not Set'

    def __len__(self):
        return len(self.color)
