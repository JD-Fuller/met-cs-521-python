"""
JD Fuller
Class: CS 521 - Fall 1
Date: 14OCT2020
Homework Problem # 2
Description of Problem: Create Organ class and subclasses of heart and brain
"""


class Organ(object):
    '''Class Organ creates an organ object'''

    def __init__(self, name='', weight=0, org_system='', vital=True):
        self.organ_name = name
        self.organ_weight_grams = weight
        assert isinstance(weight, int), 'Weight must be a number'
        self.vital_organ = vital
        self.organ_system = org_system
        assert isinstance(org_system, str), 'Organ system must be string'

    def __repr__(self):
        return repr('Organ Name:' + self.organ_name + '  Organ Weight: ' + str(self.organ_weight_grams) + ' grams '
                    + '  Vital Organ: ' + str(self.vital_organ) + '  Sub-System: ' + self.organ_system)


class Heart(Organ):
    """Heart Organ Subclass"""
    def __init__(self, length=0, weight=0, thickness=0, breadth=0):
        super().__init__(name='', org_system='Muscular', vital=True)
        self.heart_length_cm = length
        assert isinstance(length, int), 'Length must be number'
        self.heart_weight_grams = weight
        assert isinstance(weight, int), 'Length must be a number'
        self.heart_thickness_cm = thickness
        assert isinstance(thickness, float), 'Thickness must be a number'
        self.heart_breadth_cm = breadth
        assert isinstance(breadth, float), 'Breadth must be a number'

    def heart_status(self):
        return 'pumping blood'

    def heart_weight_oz(self):
        return 'Heart Weight in oz: ' + str(self.heart_weight_grams * .035)

    def __repr__(self):
        return repr('Heart: ' + str(self.heart_weight_grams) +
                    '  Vital Organ: ' + str(self.vital_organ) +
                    '  Organ System: ' + self.organ_system +
                    '  Organ Name: ' + self.organ_name +
                    '  Heart Length: ' + str(self.heart_length_cm) +
                    '  Heart Weight: ' + str(self.heart_weight_grams) + ' grams' +
                    '  Heart Breadth: ' + str(self.heart_breadth_cm) +
                    '  Heart Thickness: ' + str(self.heart_thickness_cm))


class Brain(Organ):
    """Brain Organ Subclass"""
    def __init__(self, volume=0, weight=0.0):
        super().__init__(name='', org_system='Nervous', vital=True)
        self.brain_volume = volume
        assert isinstance(volume, int), 'Volume must be a number'
        self.brain_weight_gram = weight
        assert isinstance(weight, float), 'Weight must be a number'

    def brain_status(self):
        return 'thinking...'

    def brain_weight_oz(self):
        return 'Brain Weight: ' + str(self.brain_weight_gram * .035)

    def __repr__(self):
        return repr('Brain: ' + str(self.brain_volume) + '  Vital Requirement: ' + str(self.vital_organ) +
                    '  Organ System: ' + self.organ_system + '  Organ Name: ' + self.organ_name +
                    '  Brain Weight: ' + '{:.2f}'.format(self.brain_weight_gram) + ' grams')


# Unit Tests
if __name__ == "__main__":
    my_organ = Organ('Larynx', 35, 'Respiratory System')
    my_heart = Heart(12, 280, 6.0, 9.0)
    my_brain = Brain(1260, 1370.0)
    assert my_brain.brain_weight_oz() == 'Brain Weight: ' + str(1370.0 * .035), 'Error matching brain weight in oz'
    assert my_brain.brain_volume == 1260, 'Error matching volume'
    assert my_heart.heart_weight_grams == 280, 'Error matching weight of heart'
    assert my_heart.heart_weight_oz() == 'Heart Weight in oz: ' + str(280 * .035), 'Error matching heart weight in oz'

    print(repr(my_organ))

    print(my_heart.heart_status())
    print(my_heart.heart_weight_oz())
    print(my_heart)

    print(my_brain.brain_volume)
    print(my_brain.brain_weight_gram)

    print(my_brain)
    print(my_brain.brain_weight_oz())
    print(my_brain)
    print('All Tests Passed')
