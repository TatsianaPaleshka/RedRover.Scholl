# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#     - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получения значений этого
#     атрибута нужно использовать методы get и set.

class IsoCurrenciesCodes:
    def __init__(self, alphabetic_code, numeric_code, minor_unit, currency_name, location):
        self.alphabetic_code = alphabetic_code
        self.numeric_code = numeric_code
        self.minor_unit = minor_unit
        self.currency_name = currency_name
        self.location = location

    def get_iso(self):
        return f'Code = {self.alphabetic_code}, Num = {self.numeric_code}, Minor unit = {self.minor_unit}, ' \
               f'Currency = {self.currency_name}, Location = {self.location}'

    def print_iso(self):
        print(f'Code = {self.alphabetic_code}, Num = {self.numeric_code}, '
              f'Minor unit = {self.minor_unit}, Currency = {self.currency_name}, Location = {self.location}')


class HistoricalIso(IsoCurrenciesCodes):
    def __init__(self, alphabetic_code, numeric_code, minor_unit, currency_name, location, from_date, to_date,
                 replaced_by):
        super().__init__(alphabetic_code, numeric_code, minor_unit, currency_name, location)
        self.__from_date = from_date
        self.__to_date = to_date
        self.__replaced_by = replaced_by

    def get_historical_iso(self):
        return f'Historical ISO codes: Code = {self.alphabetic_code}, Num = {self.numeric_code}, ' \
               f'Minor unit = {self.minor_unit}, Currency = {self.currency_name}, Location = {self.location}, ' \
               f'From = {self.__from_date}, Until = {self.__to_date}, Replaced by = {self.__replaced_by}'

    def set_to_date(self, to_date):
        self.__to_date = to_date

    def get_to_date(self):
        return self.__to_date

    def set_from_date(self, from_date):
        self.__from_date = from_date

    def get_from_date(self):
        return self.__from_date

    def set_replaced_by(self, replaced_by):
        self.__replaced_by = replaced_by

    def get_replaced_by(self):
        return self.__replaced_by


class nonIso(IsoCurrenciesCodes):
    def __init__(self, unofficial_code, alphabetic_code, numeric_code, minor_unit, currency_name, location, notes):
        super().__init__(alphabetic_code, numeric_code, minor_unit, currency_name, location)
        self.unofficial_code = unofficial_code
        self.comment = notes

    def get_non_iso(self):
        return f'Non-standard codes: Unofficial code = {self.unofficial_code}, ISO code = {self.alphabetic_code}, ' \
               f'Num = {self.numeric_code}, Minor unit = {self.minor_unit}, Currency = {self.currency_name}, ' \
               f'Location = {self.location}, Notes = {self.comment}'


# Actual ISO currencies codes
iso_BYN = IsoCurrenciesCodes('BYN', 933, 2, 'Belarusian ruble', 'BY')
print(f'Actual ISO currencies codes: {iso_BYN.get_iso()}')
iso_BYN.print_iso()
# print(iso_BYN.location)
iso_RUB = IsoCurrenciesCodes('RUB', 643, 2, 'Russian ruble', 'RU')
iso_RUB.print_iso()
iso_GPB = IsoCurrenciesCodes('GPB', 826, 2, 'Pound sterling', 'UK')
iso_GPB.print_iso()

# Historical ISO codes
iso_RUR = HistoricalIso('RUR', 810, 2, 'Russian ruble', 'RU', '1992', '1997-12-31', 'RUB')
print(iso_RUR.get_historical_iso())
iso_RUR.print_iso()
iso_RUR.set_from_date('1992-01-01')
# print(iso_RUR.get_from_date())
print(iso_RUR.get_historical_iso())

# Non-standard codes
non_STG = nonIso('STG', 'GPB', 826, 2, 'Sterling', 'UK', """STG stands for STerlinG, the official name of the United
Kingdom's currency, of which the pound is the main unit. STG conflicts with ISO 4217, because ST stands for São Tomé 
and Príncipe.""")
# non_STG.get_iso()
print(non_STG.get_non_iso())
