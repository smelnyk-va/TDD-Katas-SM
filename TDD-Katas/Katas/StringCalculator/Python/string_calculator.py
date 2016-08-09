__author__ = 'smelnyk'


class StringCalculator(object):

    @staticmethod
    def string_add(str_numbers):
        sum = 0

        if str_numbers == '' or str_numbers == "":
            return 0
        else:
            if ',' in str_numbers:
                for number in str_numbers.split(','):
                    sum += int(number)
            else:
                for number in str_numbers.split('\n'):
                    sum += int(number)
            return sum
