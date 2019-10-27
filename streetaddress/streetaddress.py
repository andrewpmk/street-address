#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    streetaddress.streetaddress
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2012 by PN.
    :license: MIT, see LICENSE for more details.
"""

import re

import Levenshtein
from streetaddress import abbrevs
#from streetaddress import abbrevs

# import six


########################################################################
# StreetAddressParser
########################################################################


# class StreetAddressParser():
#     def __init__(self):
#         abbrev_suffix_map = get_abbrev_suffix_dict()
#         self.street_type_set = set(abbrev_suffix_map.keys()) | set(abbrev_suffix_map.values())
#
#         self.text2num_dict = get_text2num_dict()
#         self.suite_type_set = set([
#             'suite', 'ste',
#             'apt', 'apartment', 'apartme', 'apartemen', 'apartado', 'apartament',
#             'room', 'rm', '#',
#             'unit', 'un', 'unt'
#         ])
#         self.rec_st_nd_rd_th = re.compile(r'^\d+(st|nd|rd|th)$', flags=re.I | re.U)
#         self.rec_house_number = re.compile(r'^\d\S*$', flags=re.I | re.U)
#
#     def parse(self, addr_str, skip_house=False):
#         addr_str = addr_str.strip()
#         res = {
#             'house': None,
#             'street_name': None,
#             'street_type': None,
#             'street_full': None,
#             'suite_num': None,
#             'suite_type': None,
#             'other': None,
#         }
#
#         tokens = addr_str.split()
#         start_idx = 0
#
#         if len(tokens) == 0:
#             return res
#
#         if skip_house:
#             start_idx = 0
#         else:
#             if tokens[0].lower() in self.text2num_dict:
#                 res['house'] = six.text_type(self.text2num_dict[tokens[0].lower()])
#                 start_idx = 1
#             elif self.rec_st_nd_rd_th.search(tokens[0]):
#                 # first token is actually a street number (not house)
#                 start_idx = 0
#             elif self.rec_house_number.search(tokens[0]):
#                 res['house'] = tokens[0]
#                 start_idx = 1
#             else:
#                 # no house number
#                 start_idx = 0
#
#             if res['house'] and len(tokens) >= 2 and tokens[1] == '1/2':
#                 res['house'] += ' ' + tokens[1]
#                 start_idx = 2
#
#         street_accum = []
#         other_accum = []
#         is_in_state = 'street'  # can be 'street', 'suite', 'other'
#
#         for i in range(start_idx, len(tokens)):
#             word = tokens[i]
#             # word = re.sub(r'[\.\,]+$', '', word, flags=re.I|re.U)
#             while len(word) > 0 and (word[-1] == '.' or word[-1] == ','):
#                 # truncate the trailing dot (for abbrev)
#                 word = word[:-1]
#             word_lw = word.lower()
#
#             if word_lw in self.street_type_set and len(street_accum) > 0:
#                 res['street_type'] = word
#                 is_in_state = 'other'
#             elif word_lw in self.suite_type_set:
#                 res['suite_type'] = word
#                 is_in_state = 'suite'
#             elif len(word_lw) > 0 and word_lw[0] == '#' and res['suite_num'] is not None:
#                 res['suite_type'] = '#'
#                 res['suite_num'] = word[1:]
#                 is_in_state = 'other'
#             elif is_in_state == 'street':
#                 street_accum.append(word)
#             elif is_in_state == 'suite':
#                 res['suite_num'] = word
#                 is_in_state = 'other'
#             elif is_in_state == 'other':
#                 other_accum.append(word)
#             else:
#                 raise Exception('this state should never be reached')
#
#         # TODO PO Box handling
#         # acronym = lambda s : Regex(r"\.?\s*".join(s)+r"\.?")
#         # poBoxRef = ((acronym("po") | acronym("apo") | acronym("afp")) +
#         #            Optional(CaselessLiteral("BOX"))) + Word(alphanums)("boxnumber")
#
#         if street_accum:
#             res['street_name'] = ' '.join(street_accum)
#         if other_accum:
#             res['other'] = ' '.join(other_accum)
#
#         if res['street_name'] and res['street_type']:
#             res['street_full'] = res['street_name'] + ' ' + res['street_type']
#         elif res['street_name']:
#             res['street_full'] = res['street_name']
#         elif res['street_type']:
#             res['street_full'] = res['street_type']
#
#         return res
#
#
# def get_abbrev_suffix_dict():
#     return abbrevs.USA_ABBREVS
#
#
# def get_text2num_dict():
#     return {
#         'zero': 0,
#         'one': 1,
#         'two': 2,
#         'three': 3,
#         'four': 4,
#         'five': 5,
#         'six': 6,
#         'seven': 7,
#         'eight': 8,
#         'nine': 9,
#         'ten': 10,
#         'eleven': 11,
#         'twelve': 12,
#         'thirteen': 13,
#         'fourteen': 14,
#         'fifteen': 15,
#         'sixteen': 16,
#         'seventeen': 17,
#         'eighteen': 18,
#         'nineteen': 19,
#         'twenty': 20,
#         'thirty': 30,
#         'forty': 40,
#         'fifty': 50,
#         'sixty': 60,
#         'seventy': 70,
#         'eighty': 80,
#         'ninety': 90,
#     }
#
#
# ########################################################################
# # StreetAddressFormatter
# ########################################################################
# class StreetAddressFormatter():
#     def __init__(self):
#         # abbreviate west, east, north, south?
#         self.abbrev_suffix_map = get_abbrev_suffix_dict()
#         self.street_type_set = set(self.abbrev_suffix_map.keys()) | set(
#             self.abbrev_suffix_map.values())
#         # TODO: Should be replaced with data from abbrevs.py
#         self.abbrev_direction_map = {
#             'east': 'E',
#             'west': 'W',
#             'north': 'N',
#             'south': 'S',
#         }
#
#         for k, v in self.abbrev_suffix_map.items():
#             self.abbrev_suffix_map[k] = v.title()
#
#         TH_or_str = '|'.join(self.street_type_set)
#         self.re_TH = re.compile(r'\b(\d+)\s+(%s)\.?$' % TH_or_str, flags=re.I | re.U)
#
#     def st_nd_th_convert(self, num_str):
#         if len(num_str) >= 2 and (num_str[-2:] == '11' or num_str[-2:] == '12'):
#             return num_str + 'th'
#         elif num_str[-1] == '1':
#             return num_str + 'st'
#         elif num_str[-1] == '2':
#             return num_str + 'nd'
#         elif num_str[-1] == '3':
#             return num_str + 'rd'
#         else:
#             return num_str + 'th'
#
#     def append_TH_to_street(self, addr):
#         # street,avenue needs to be the last word
#         addr = addr.strip()
#         match = self.re_TH.search(addr)
#         if match:
#             repl = '%s %s' % (self.st_nd_th_convert(match.group(1)), match.group(2))
#             addr = addr.replace(match.group(0), repl)
#         return addr
#
#     def abbrev_direction(self, addr):
#         word_lst = addr.split()
#         if len(word_lst) == 0:
#             return addr
#
#         for i in range(len(word_lst) - 1):
#             word = word_lst[i].lower()
#             # should have a digit after direction, e.g. "West 23rd"
#             if word in self.abbrev_direction_map and word_lst[i + 1][0].isdigit():
#                 word_lst[i] = self.abbrev_direction_map[word]
#         addr = ' '.join(word_lst)
#         return addr
#
#     def abbrev_street_avenue_etc(self, addr, abbrev_only_last_token=True):
#         word_lst = addr.split()
#         if len(word_lst) == 0:
#             return addr
#
#         if abbrev_only_last_token:
#             pos_lst = [-1]
#         else:
#             pos_lst = range(len(word_lst))
#
#         for p in pos_lst:
#             word = re.sub(r'\.$', '', word_lst[p]).lower()  # get rid of trailing period
#             if word in self.abbrev_suffix_map:
#                 word_lst[p] = self.abbrev_suffix_map[word]
#         addr = ' '.join(word_lst)
#         return addr


# Street address class by Andrew MacKinnon
class StreetAddress():
    def __init__(self):
        self.country_names = set(abbrevs.COUNTRIES.keys()) | set(abbrevs.COUNTRIES_ALTERNATE.keys())
        self.country_codes = set(abbrevs.COUNTRIES.values())
        self.state_names_en = set(abbrevs.US_STATES_EN.keys())
        self.state_names_fr = set(abbrevs.US_STATES_FR.keys())
        self.state_codes = set(abbrevs.US_STATES_EN.values())
        self.province_names_en = set(abbrevs.CAN_PROVINCES_TERRITORIES_EN.keys())
        self.province_names_fr = set(abbrevs.CAN_PROVINCES_TERRITORIES_FR.keys())
        self.province_codes = set(abbrevs.CAN_PROVINCES_TERRITORIES_EN.values())
        self.state_province_names = self.state_names_en | self.state_names_fr | self.province_names_en | self.province_names_fr
        self.state_province_codes = self.state_codes | self.province_codes

        self.suite_type_set = {'suite', 'ste', 'apt', 'apartment', 'apartme', 'apartemen', 'apartado', 'apartament',
                               'app', 'room', 'rm', '#', 'unit', 'un', 'unt'}

        self.street_types_us = set(abbrevs.USA_ABBREVS.keys())
        self.street_abbrevs_us = set(abbrevs.USA_ABBREVS.values())
        self.street_types_can_en = set(abbrevs.CAN_ABBREVS_EN.keys())
        self.street_abbrevs_can_en = set(abbrevs.CAN_ABBREVS_EN.values())
        self.street_types_can_fr = set(abbrevs.CAN_ABBREVS_FR.keys())
        self.street_abbrevs_can_fr = set(abbrevs.CAN_ABBREVS_FR.values())

        self.street_abbrevs_extra = set(abbrevs.EXTRA_STREET_ABBREVS.keys())  # Stuff like Cr and Ln which is unofficial

        self.street_type_suffix = self.street_types_us | self.street_types_can_en
        self.street_abbrev_suffix = self.street_abbrevs_us | self.street_abbrevs_can_en | self.street_abbrevs_extra
        self.street_type_abbrev_suffix = self.street_type_suffix | self.street_abbrev_suffix
        self.street_type_abbrev_prefix = self.street_types_can_fr | self.street_abbrevs_can_fr

        self.street_directions_en = set(abbrevs.DIRECTION_ABBREV_EN.keys())
        self.street_direction_abbrevs_en = set(abbrevs.DIRECTION_ABBREV_EN.values())
        self.street_directions_fr = set(abbrevs.DIRECTION_ABBREV_FR.keys())
        self.street_direction_abbrevs_fr = set(abbrevs.DIRECTION_ABBREV_FR.values())
        self.street_directions_en = self.street_directions_en | self.street_direction_abbrevs_en
        self.street_directions_fr = self.street_directions_fr | self.street_direction_abbrevs_fr
        self.street_directions = self.street_directions_en | self.street_directions_fr

        self.cities = set(abbrevs.CITIES_CAN.keys()) | set(abbrevs.CITIES_US.keys())

    # # Full address
    #
    # @property
    # def full_address(self):
    #     return self._full_address
    #
    # @full_address.setter
    # def full_address(self, value):
    #     self._full_address = value
    #
    # @full_address.deleter
    # def full_address(self):
    #     del self._full_address
    #
    # # Unit number
    #
    # @property
    # def unitnumber(self):
    #     return self._unitnumber
    #
    # @unitnumber.setter
    # def unitnumber(self, value):
    #     self._unitnumber = value
    #
    # @unitnumber.deleter
    # def unitnumber(self):
    #     del self._unitnumber
    #
    # # Unit type
    #
    # @property
    # def unittype(self):
    #     return self._unittype
    #
    # @unittype.setter
    # def unittype(self, value):
    #     self._unittype = value
    #
    # @unittype.deleter
    # def unittype(self):
    #     del self._unittype
    #
    # # Housenumber
    #
    # @property
    # def housenumber(self):
    #     return self._housenumber
    #
    # @housenumber.setter
    # def housenumber(self, value):
    #     self._housenumber = value
    #
    # @housenumber.deleter
    # def housenumber(self):
    #     del self._housenumber
    #
    # # Street prefix
    #
    # @property
    # def streetprefix(self):
    #     return self._streetprefix
    #
    # @streetprefix.setter
    # def streetprefix(self, value):
    #     self._streetprefix = value
    #
    # @streetprefix.deleter
    # def streetprefix(self):
    #     del self._streetprefix
    #
    # # Street type (French)
    #
    # @property
    # def streettype_fr(self):
    #     return self._streettype_fr
    #
    # @streettype_fr.setter
    # def streettype_fr(self, value):
    #     self._streettype_fr = value
    #
    # @streettype_fr.deleter
    # def streettype_fr(self):
    #     del self._streettype_fr
    #
    # # Street name
    #
    # @property
    # def streetname(self):
    #     return self._streetname
    #
    # @streetname.setter
    # def streetname(self, value):
    #     self._streetname = value
    #
    # @streetname.deleter
    # def streetname(self):
    #     del self._streetname
    #
    # # Street type (English)
    #
    # @property
    # def streettype_en(self):
    #     return self._streettype_en
    #
    # @streettype_en.setter
    # def streettype_en(self, value):
    #     self._streettype_en = value
    #
    # @streettype_en.deleter
    # def streettype_en(self):
    #     del self._streettype_en
    #
    # # Street suffix
    #
    # @property
    # def streetsuffix(self):
    #     return self._streetsuffix
    #
    # @streetsuffix.setter
    # def streetsuffix(self, value):
    #     self._streetsuffix = value
    #
    # @streetsuffix.deleter
    # def streetsuffix(self):
    #     del self._streetsuffix
    #
    # # City
    #
    # @property
    # def city(self):
    #     return self._city
    #
    # @city.setter
    # def city(self, value):
    #     self._city = value
    #
    # @city.deleter
    # def city(self):
    #     del self._city
    #
    # # State/province
    #
    # @property
    # def state(self):
    #     return self._state
    #
    # @state.setter
    # def state(self, value):
    #     self._state = value
    #
    # @state.deleter
    # def state(self):
    #     del self._state
    #
    # # Country
    #
    # @property
    # def country(self):
    #     return self._country
    #
    # @country.setter
    # def country(self, value):
    #     self._country = value
    #
    # @country.deleter
    # def country(self):
    #     del self._country

    # Is this an ASCII character in range A-Z?

    def is_alphabetic(self, x):
        # Must be a string with length 1
        if type(x) != str:
            return False
        if len(x) != 1:
            return False
        x = x.upper()  # Convert to uppercase
        if ord(x) >= 65 and ord(x) <= 90:  # ASCII values for A and Z
            return True
        else:
            return False

    # Is this an ASCII character in range 0-9

    def is_ascii_digit(self, x):
        # Must be a string with length 1
        if type(x) != str:
            return False
        if len(x) != 1:
            return False
        if ord(x) >= 48 and ord(x) <= 57:  # ASCII values for 0 and 9
            return True
        else:
            return False

    # Is this the first character of a Canadian postal code?

    def is_first_character_of_postal_code(self, x):
        if not self.is_alphabetic(x):
            return False
        x = x.upper()
        if x in abbrevs.CAN_POSTAL_CODE_FIRST_LETTER.keys():
            return True
        else:
            return False

    # Is this the second character of a Canadian postal code?

    def is_second_character_of_postal_code(self, x):
        if not self.is_alphabetic(x):
            return False
        x = x.upper()
        if x in abbrevs.CAN_POSTAL_CODE_SECOND_LETTER:
            return True
        else:
            return False

    # Is this the third character of a Canadian postal code?

    def is_third_character_of_postal_code(self, x):
        if not self.is_alphabetic(x):
            return False
        x = x.upper()
        if x in abbrevs.CAN_POSTAL_CODE_THIRD_LETTER:
            return True
        else:
            return False

    # Is the string the first part of a Canadian postal code (e.g. H0H)?
    # Regex adapted from https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s15.html

    def is_first_part_can_postal_code(self, x):

        # Input must be string
        if type(x) != str:
            return False
        x = x.strip()  # Remove excess whitespace
        x = x.upper()  # Make uppercase
        if re.match('^(?!.*[DFIOQU])[A-VXY][0-9][A-Z]$', x): # 2019-10-27 - added $ at end so it won't match full postal code
            return True
        else:
            return False

    # Is the string the second part of a Canadian postal code (e.g. 0H0)?
    # Regex adapted from https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s15.html

    def is_second_part_can_postal_code(self, x):

        # Input must be string
        if type(x) != str:
            return False
        x = x.strip()  # Remove excess whitespace
        x = x.upper()  # make uppercase
        if re.match('^(?!.*[DFIOQU])[0-9][A-Z][0-9]$', x): # 2019-10-27 - added $ at end so it won't match full postal code
            return True
        else:
            return False

    # Is this a combined postal code with no space (e.g. H0H0H0)?
    # TODO: Should this accept junk like H0H-0H0?

    def is_combined_postal_code(self, x):
        if type(x) != str:
            return False
        x = x.strip()  # Remove excess whitespace
        if len(x) != 6:  # Must have six characters
            return False
        postal_code_first_part = x[0:3]
        postal_code_second_part = x[3:6]
        if not self.is_first_part_can_postal_code(postal_code_first_part):
            return False
        if not self.is_second_part_can_postal_code(postal_code_second_part):
            return False
        return True

    # Is this a five-digit ZIP code?

    def is_zip5(self, x):
        # If this is a string
        if type(x) == str:
            x = x.strip()
            if len(x) != 5:
                return False
            try:
                x = int(x)  # Convert to integer, note that converting integers like 00001 works
            except ValueError:  # Not an integer
                return False
        # Otherwise must be integer or floating point that is represented as integer
        if type(x) != int:
            if not (type(x) == float and x.is_integer()):
                return False
        # Lowest ZIP Code is 00501 and highest is 99950
        # from https://www.quora.com/What-is-the-lowest-Zip-Code-and-what-is-the-highest-Zip-Code-in-America
        if x < 501 or x > 99950:
            return False
        else:
            return True

    # Is this a Unicode hyphen character?

    def is_unicode_hyphen(self, x):
        if type(x) != str or len(x) != 1:
            return False
        if x in abbrevs.UNICODE_HYPHENS:
            return True
        else:
            return False

    # Is this a nine-digit ZIP+5 code?
    # Only ZIP codes like 00000-0000 accepted
    # Regex adapted from https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s14.html

    def is_zip9(self, x):
        if type(x) != str:
            return False
        x = x.strip()
        if not self.is_zip5(x[0:5]):  # Check if first part is valid ZIP 5 code
            return False
        x = re.sub(abbrevs.UNICODE_HYPHENS_RE, '-', x)  # Replace unicode dashes with -
        if re.match('^[0-9]{5}-[0-9]{4}$', x):
            return True
        else:
            return False

    def find_country_location(self, address):
        matches = []  # List of locations matched
        if type(address) != str:
            raise ValueError
        upper_address = address.upper()
        for i in [x.upper() for x in self.country_codes | self.country_names]:
            match = upper_address.find(i)
            if match != -1:
                matches.append(match)
        return matches

    def find_can_postal_code_location(self, address):
        match = None
        if type(address) != str:
            raise ValueError
        upper_address = address.upper()
        re_match = re.match('(?!.*[DFIOQU])[A-VXY][0-9][A-Z]\s[0-9][A-Z][0-9]', upper_address)
        if re_match:
            return re_match.start()

    # Fix broken Canadian postal codes
    # Returns the fixed postal code if it is fixable, returns False otherwise
    def fix_can_postal_code(self, postal_code, max_steps=4):
        if type(postal_code) != str:
            raise ValueError
        # Max steps must be between 0 and 4
        if max_steps < 0 or max_steps > 4 or type(max_steps) != int:
            raise ValueError
        postal_code = re.sub(r"\s", "", postal_code)  # Remove spaces, tabs, newlines, etc.
        postal_code = re.sub(abbrevs.UNICODE_HYPHENS_RE, "", postal_code) # Remove hyphens and Unicode hyphens
        step = 0  # Which step of postal code modification process are we on?
        while step <= max_steps:
            if step == 1:
                # Replace O and Q with 0 and I with 1
                # These characters are never in a Canadian postal code
                postal_code = re.sub("O", "0", postal_code)
                postal_code = re.sub("Q", "0", postal_code)
                postal_code = re.sub("I", "1", postal_code)
                postal_code = re.sub("o", "0", postal_code)
                postal_code = re.sub("q", "0", postal_code)
                postal_code = re.sub("i", "1", postal_code)
            elif step == 2:
                # Remove all punctuation
                postal_code = re.sub('[.,?!@#$%^&*()\[\]{}|\\\":;/<>+=_]+', '', postal_code)
            elif step == 3:
                # Replace lowercase Ls in area where number should be with 1s
                postal_code_list = list(postal_code)
                postal_code_list[1] = re.sub("l", "1", postal_code)
                postal_code_list[3] = re.sub("l", "1", postal_code)
                postal_code_list[5] = re.sub("l", "1", postal_code)
                postal_code = "".join(postal_code_list)
            elif step == 4:
                postal_code = postal_code[:6]  # Remove all characters after 6th character
            # See if we have found a valid postal code
            if re.match('(?!.*[DFIOQU])[A-VXY][0-9][A-Z][0-9][A-Z][0-9]', postal_code.upper()):
                # Put the middle space in the postal code (was removed earlier if present)
                postal_code = postal_code[0:3] + " " + postal_code[4:6]
                postal_code = postal_code.upper() # Make postal code uppercase
                return postal_code
            step = step + 1
        return False

    # Find locations of commas, semicolons and colons
    def find_commas(self, address):
        matches = []  # List of locations
        for i in re.finditer('[,:;]', address):
            matches.append(i.start())
        return matches

    # Removes commas
    def remove_commas(self, x: str) -> str:
        return x.replace(",","")

    def remove_last_comma(self, x: str) -> str:
        return re.sub(",$","",x)

    def remove_last_period(self, x: str) -> str:
        return re.sub("\.$","",x)

    def exact_or_approximate_match(self, a: str, b: str, levenshtein):
        if type(a) != str or type(b) != str:
            raise ValueError
        if levenshtein is not None and type(levenshtein) != float and type(levenshtein) != int:
            raise ValueError
        if levenshtein is None:
            levenshtein = 1.0
        if type(levenshtein) == int:
            levenshtein = float(levenshtein)
        if levenshtein > 1.0 or levenshtein < 0.0:
            raise ValueError
        if levenshtein == 1.0: # Exact match
            return a == b
        else:
            ratio = Levenshtein.ratio(a, b)
            return ratio >= levenshtein

    # Find word pattern in string
    # Returns tuple (start_index, end_index)
    # Where start_index is index of first word matched
    # End_index is index of last word matched
    # Levenshtein = if not None use approximate string matching
    def find_word(self, pattern: str, string: str, levenshtein = None):
        pattern_words = pattern.split(" ")  # Split pattern into words
        string_words = string.split(" ")  # Split string into words
        start_index = None
        end_index = None
        for i in range(len(string_words)):
            # Look for first word in pattern
            if self.exact_or_approximate_match(pattern_words[0],string_words[i],levenshtein):
                # If not enough words left in the string to possibly find the pattern
                if len(string_words) < i + len(pattern_words):
                    break
                start_index = i
                end_index = i
                match = True
                j = i + 1
                # Look to see if remaining words in pattern are in string
                while match and j - i < len(pattern_words):
                    if not self.exact_or_approximate_match(pattern_words[j - i],string_words[j],levenshtein):
                        match = False
                    if match:
                        end_index = j
                    j = j + 1
                if match == False:
                    return (None, None)
        return (start_index, end_index)

    def find_word_nocase(self, pattern: str, string: str, levenshtein = None):
        return self.find_word(pattern.upper(), string.upper(), levenshtein)

    # Find first and last word index corresponding to first and last character index of a match
    # Used for regular expression matching
    def identify_word_location(self, string: str, start_char, end_char):
        if start_char >= len(string) - 1 or end_char >= len(string) - 1:  # Character indexes must be in range
            raise ValueError
        string_before = string[0:start_char + 1]  # Portion of string before start_char
        string_match = string[start_char:end_char + 1]  # Portion of string between start_char and end_char
        start_index = string_before.count[" "]
        end_index = start_index + string_match.count[" "]
        return (start_index, end_index)

    def tag_if_found(self, pattern: str, string: str, tag: str, address_tags: list, levenshtein = None) -> list:
        x = self.find_word_nocase(pattern, string, levenshtein)
        if x != (None, None):
            for j in range(x[0], x[1] + 1):
                address_tags = self.add_tag(address_tags, tag, j)
        return address_tags

    # Add tag tag to tags at position int
    def add_tag(self, tags: list, tag: str, index: int) -> str:
        if index > len(tags) - 1:  # Index out of range
            raise ValueError
        # Do not add TEXT OR NUMBER to the tags
        # Exception: NUMBER overrides TEXT
        if tag == "TEXT" and tags[index] is not None:
            return tags
        if tag == "NUMBER" and tags[index] is not None and tags[index] != "TEXT":
            return tags
        # Do not add the same tag twice
        if tags[index] is not None and tag in tags[index].split(" "):
            return tags
        # TEXT and NUMBER tags are overridden by anything else
        if tags[index] is None or tags[index] == "TEXT" or tags[index] == "NUMBER":
            tags[index] = tag
        else:
            tags[index] = tags[index] + " " + tag
        return tags

    # Replace all occurrences of the pattern list in the search list with the replace list
    def substitute_list(self, pattern: list, replace: list, search: list):
        if len(pattern) != len(replace):
            raise ValueError  # Replacement list must be same as pattern list
        if len(pattern) == 0: # Cannot use an empty list as a pattern
            raise ValueError
        if len(pattern) > len(search):
            return search  # Nothing to replace since pattern/replace list is longer than list to search
        search_index = 0 # The location in pattern that we are currently looking at
        for i in range(len(search)):
            # Match found
            if search[i] == pattern[search_index]:
                if search_index == len(pattern) - 1: # We have found the entire length of the pattern
                    # Replace the occurence of pattern with replace
                    search = search[:i-search_index] + replace + search[i+1:]
                    search_index = 0
                else:
                    search_index = search_index + 1
            else:
                # No match, reset search index and searching flag
                search_index = 0
        return search

    # Merge two dictionaries, overwriting dict1 with dict2 tags except when dict2 has None for a tag
    def merge_dictionaries(self, dict1, dict2):
        if type(dict1) != dict or type(dict2) != dict:
            raise ValueError
        key_list = list(dict2.keys())
        for i in key_list:
            if dict2[i] is None and i in dict1.keys():
                del dict2[i]  # Remove None entries if they exist in dict1
        dict1.update(dict2)
        return dict1

    # Tag addresses and determine which portion of the address is which
    # Example format: Canada Post, 2701 Riverside Dr, Ottawa, ON, K1A 0B1, Canada
    # Canada Post, 2701 Ch. Riverside, Ottawa, ON, K1A 0B1, Canada
    # How this works: Scan for different parts of the address
    # Finds the following:
    # ZIPCODE - any 5 digit number between 00501 and 99950. Can also be a 5 digit housenumber
    # ZIPCODE4 - any ZIP+4 like 00000-0000. Could potentially also be unit number then 5 digit housenumber
    # NUMBER - any integer other than a ZIPCODE
    # NUMBEREXTENDED - either number with letter at end (2701B) or number with fraction at end (2701-1/2)
    # FRACTION - a fractional number like 1/2
    # UNITHOUSENUMBER - a unit number followed by a housenumber
    # POUNDNUMBER - a number preceded by #
    # SUITE - anything like "Apartment", "Unit", "Suite", etc.
    # ST - Can be either Saint or Street depending on position in string
    # STREET_ABBREV_SUFFIX - Abbreviated street suffix (except St)
    # STREET_ABBREV_PREFIX - Abbreviated street prefix (French)
    # STREET - Likely street name
    # STREET_DIRECTION - North, south, east, west, etc.
    # STATE - State name or abbreviation
    # PROVINCE - State name or abbreviation
    # POSTAL_CODE - 6 digit Canadian postal code (either K1A 0B1 or K1A0B1)
    # POSTAL_CODE_FIRST - First half of Canadian postal code
    # POSTAL_CODE_SECOND - Second half of Canadian postal code
    # COUNTRY - Country name or code
    # TEXT - Anything that is a word that is unrecognized
    # AND - "AND" or "&"
    def tag_address(self, address: str) -> list:
        address = address.strip()
        # Split by space
        address_split = address.split(" ")
        address_tags = [None for i in range(len(address_split))]  # Initialize None array
        address_no_commas = self.remove_commas(address)
        for i in self.country_names:
            address_tags = self.tag_if_found(i, address_no_commas, "COUNTRY", address_tags, 0.8)
        for i in self.state_names_en | self.state_names_fr:
            address_tags = self.tag_if_found(i, address_no_commas, "STATE", address_tags, 0.8)
        for i in self.province_names_en | self.province_names_fr:
            address_tags = self.tag_if_found(i, address_no_commas, "PROVINCE", address_tags, 0.8)
        for i in self.cities:
            address_tags = self.tag_if_found(i, address_no_commas, "CITY", address_tags, 0.8)
        for i in range(len(address_split)):
            address_split_stripped = self.remove_last_comma(address_split[i])
            # Tag anything that contains alphabetic characters that is unrecognized as text
            if re.search('[a-zA-Z]', address_split_stripped):
                address_tags = self.add_tag(address_tags, "TEXT", i)
#            if address_split_stripped.isalpha():
#                address_tags = self.add_tag(address_tags,"TEXT",i)  # Tag anything alphabetic that is unrecognized as text
            # Is this 1st, 2nd, 3rd, etc.
#            if re.match('(\\d+)(st|nd|rd|th)',address_split_stripped):
#                address_tags = self.add_tag(address_tags,"TEXT",i)
            if address_split_stripped.lower() in ("and", "et", "&"):
                address_tags = self.add_tag(address_tags, "AND", i)
            if address_split_stripped in self.country_codes:
                address_tags = self.add_tag(address_tags, "COUNTRY", i)
            if address_split_stripped in self.state_codes:
                address_tags = self.add_tag(address_tags, "STATE", i)
            if address_split_stripped in self.province_codes:
                address_tags = self.add_tag(address_tags, "PROVINCE", i)
            # Look for numbers
            if address_split_stripped.isdigit():
                address_tags = self.add_tag(address_tags, "NUMBER", i)
            if self.is_zip9(address_split_stripped):
                address_tags = self.add_tag(address_tags, "ZIPCODE4", i)
            if self.is_zip5(address_split_stripped):
                address_tags = self.add_tag(address_tags, "ZIPCODE", i)
            if self.is_first_part_can_postal_code(address_split_stripped):
                address_tags = self.add_tag(address_tags, "POSTAL_CODE_FIRST", i)
            if self.is_second_part_can_postal_code(address_split_stripped):
                address_tags = self.add_tag(address_tags, "POSTAL_CODE_SECOND", i)
            if self.is_combined_postal_code(address_split_stripped):
                address_tags = self.add_tag(address_tags, "POSTAL_CODE", i)
            if self.remove_last_period(address_split_stripped.lower()) in self.street_type_abbrev_suffix:
                address_tags = self.add_tag(address_tags, "STREET_ABBREV_SUFFIX", i)
            if self.remove_last_period(address_split_stripped.lower()) in self.street_type_abbrev_prefix:
                address_tags = self.add_tag(address_tags, "STREET_ABBREV_PREFIX", i)
            if address_split_stripped.lower() in [x.lower() for x in self.street_directions]:
                address_tags = self.add_tag(address_tags, "STREET_DIRECTION", i)
            # Use approximate string matching for city
            for j in [x.lower() for x in self.cities]:
                if Levenshtein.ratio(address_split_stripped.lower(), j) >= 0.8:
                    address_tags = self.add_tag(address_tags, "CITY", i)
            #if address_split_stripped.lower() in [x.lower() for x in self.cities]:
            #    address_tags = self.add_tag(address_tags, "CITY", i)
            if address_split_stripped.lower() in self.suite_type_set:
                address_tags = self.add_tag(address_tags, "SUITE", i)
            if self.remove_last_period(address_split_stripped.lower()) == ("st" or "saint"):
                address_tags = self.add_tag(address_tags,"SAINT",i)
            # Tag any weird characters that aren't recognized as TEXT
            for j in range(len(address_tags)):
                if address_tags[j] is None:
                    address_tags[j] = "TEXT"
        # Substitute implausible combinations
        address_tags = self.substitute_list(["ZIPCODE","TEXT","STREET_ABBREV_SUFFIX"],["NUMBER","TEXT","STREET_ABBREV_SUFFIX"],address_tags)
        address_tags = self.substitute_list(["ZIPCODE","TEXT","STREET_ABBREV_SUFFIX SAINT"],["NUMBER","TEXT","STREET_ABBREV_SUFFIX"],address_tags)
        address_tags = self.substitute_list(["NUMBER","TEXT","STREET_ABBREV_SUFFIX SAINT"],["NUMBER","TEXT","STREET_ABBREV_SUFFIX"],address_tags)
        address_tags = self.substitute_list(["NUMBER", "TEXT", "TEXT", "STREET_ABBREV_SUFFIX SAINT"], ["NUMBER", "TEXT", "TEXT", "STREET_ABBREV_SUFFIX"], address_tags)
        address_tags = self.substitute_list(["NUMBER", "TEXT", "TEXT", "TEXT", "STREET_ABBREV_SUFFIX SAINT"],
                                            ["NUMBER", "TEXT", "TEXT", "TEXT", "STREET_ABBREV_SUFFIX"], address_tags)
        address_tags = self.substitute_list(["NUMBER", "TEXT", "TEXT", "TEXT", "TEXT", "STREET_ABBREV_SUFFIX SAINT"],
                                            ["NUMBER", "TEXT", "TEXT", "TEXT", "TEXT", "STREET_ABBREV_SUFFIX"], address_tags)
        address_tags = self.substitute_list(["NUMBER", "TEXT", "TEXT", "TEXT", "TEXT", "TEXT", "STREET_ABBREV_SUFFIX SAINT"],
                                            ["NUMBER", "TEXT", "TEXT", "TEXT", "TEXT", "TEXT", "STREET_ABBREV_SUFFIX"], address_tags)
        address_tags = self.substitute_list(["ZIPCODE","CITY","STREET_ABBREV_SUFFIX"],["NUMBER","TEXT","STREET_ABBREV_SUFFIX"],address_tags)
        address_tags = self.substitute_list(["COUNTRY STATE","ZIPCODE"],["STATE","ZIPCODE"],address_tags)
        address_tags = self.substitute_list(["COUNTRY STATE", "ZIPCODE4"], ["STATE", "ZIPCODE4"], address_tags)
        # Ontario, California
        address_tags = self.substitute_list(["PROVINCE CITY","COUNTRY STATE","ZIPCODE"],["CITY","STATE","ZIPCODE"],address_tags)
        address_tags = self.substitute_list(["PROVINCE CITY","COUNTRY STATE","ZIPCODE4"],["CITY","STATE","ZIPCODE4"],address_tags)
        # Ontario, Canada
        address_tags = self.substitute_list(["PROVINCE CITY","COUNTRY STATE","POSTAL_CODE_FIRST"],["CITY","STATE","POSTAL_CODE_FIRST"],address_tags)
        address_tags = self.substitute_list(["PROVINCE CITY","COUNTRY STATE","POSTAL_CODE_FIRST"],["CITY","STATE","POSTAL_CODE_FIRST"],address_tags)
        address_tags = self.substitute_list(["PROVINCE CITY","POSTAL_CODE_FIRST"],["PROVINCE","POSTAL_CODE_FIRST"],address_tags)
        address_tags = self.substitute_list(["PROVINCE CITY","POSTAL_CODE_FIRST"],["PROVINCE","POSTAL_CODE_FIRST"],address_tags)
        # New York NY
        address_tags = self.substitute_list(["STATE CITY","STATE CITY","STATE"],["CITY","CITY","STATE"],address_tags)
        # Washington DC
        address_tags = self.substitute_list(["STATE CITY","STATE"],["CITY","STATE"],address_tags)
        # Suite followed by 5-digit number that looks like a zip code
        address_tags = self.substitute_list(["SUITE","ZIPCODE"],["SUITE","NUMBER"],address_tags)
        # Weird street names like E St
        address_tags = self.substitute_list(["NUMBER","STREET_DIRECTION","STREET_ABBREV_SUFFIX SAINT"],["NUMBER","TEXT","STREET_ABBREV_SUFFIX"],address_tags)
        # Weird street names like Avenue Rd
        address_tags = self.substitute_list(["NUMBER","STREET_ABBREV_SUFFIX","STREET_ABBREV_SUFFIX"],["NUMBER","TEXT","STREET_ABBREV_SUFFIX"],address_tags)
        address_tags = self.substitute_list(["NUMBER","STREET_ABBREV_SUFFIX","STREET_ABBREV_SUFFIX SAINT"],["NUMBER","TEXT","STREET_ABBREV_SUFFIX"],address_tags)
        address_tags = self.substitute_list(["NUMBER","STREET_ABBREV_SUFFIX STREET_ABBREV_PREFIX","STREET_ABBREV_SUFFIX"],["NUMBER","TEXT","STREET_ABBREV_SUFFIX"],address_tags)
        address_tags = self.substitute_list(["NUMBER","STREET_ABBREV_SUFFIX STREET_ABBREV_PREFIX","STREET_ABBREV_SUFFIX SAINT"],["NUMBER","TEXT","STREET_ABBREV_SUFFIX"],address_tags)
        # Street address suffix that could also be a prefix
        address_tags = self.substitute_list(["NUMBER","TEXT","STREET_ABBREV_SUFFIX STREET_ABBREV_PREFIX"],["NUMBER","TEXT","STREET_ABBREV_SUFFIX"],address_tags)
        return address_tags

    # Match a single tag fuzzily if fuzzy = True
    # Match exactly if fuzzy = False
    # Returns True or False to determine whether there was a match
    def fuzzy_tag_match(self, tag, tag_pattern, fuzzy=True):
        if type(tag) != str or type(tag_pattern) != str:
            raise ValueError
        if type(fuzzy) != bool:
            raise ValueError
        if fuzzy:
            tag_list = tag.split(" ")
            tag_pattern_list = tag_pattern.split(" ")
            for i in tag_pattern_list:
                for j in tag_list:
                    if i == j:
                        return True
            return False
        else:  # Fuzzy is false, do an exact match
            return tag == tag_pattern

    # Identify a pattern of tags in a list of tags
    # Duplicates are permitted - so e.g. if the city is New York, then you get CITY CITY
    # If fuzzy = True, then it will match if any tag in the list is there
    # and it will match if more than one tag was found for a particular word
    # Returns a tuple with start and end index in tags_pattern
    def identify_tags(self, tags, tags_pattern, fuzzy=True):
        # Validate tags and tags_pattern
        if type(tags) != list and type(tags) != tuple:
            raise ValueError
        if type(fuzzy) != bool:
            raise ValueError
        for i in tags:
            if type(i) != str:
                raise ValueError
        if type(tags_pattern) == str:
            tags_pattern = list(tags_pattern) # Convert to list
        for i in tags_pattern:
            if type(i) != str:
                raise ValueError
        start_index = None  # Start of tags_pattern in tags
        end_index = None  # End of tags_pattern in tags
        pattern_index = 0  # At what point are we looking in the pattern?
        pattern_index_matched = None # What point in the pattern have we actually matched so far
        for i in range(len(tags)):
            # If the tag is found at the current pattern index
            if self.fuzzy_tag_match(tags[i],tags_pattern[pattern_index],fuzzy):
                # Found a match
                # If we are not currently searching, then start searching
                if start_index is None:
                    start_index = i
                pattern_index_matched = pattern_index
            else:
                # We are currently searching
                if start_index is not None:
                    pattern_index = pattern_index + 1
                    # We have found all the tags in the pattern
                    if pattern_index > len(tags_pattern) - 1:
                        end_index = i - 1
                        # Stop searching
                        break
                    # Check for the next entry in the pattern
                    if self.fuzzy_tag_match(tags[i],tags_pattern[pattern_index],fuzzy):
                        pattern_index_matched = pattern_index
                    else:
                        # Did not find all of the pattern
                        start_index = None
                        pattern_index = 0
                        pattern_index_matched = None
        # Did we find the entire pattern but run into the end of the tags string?
        if start_index is not None and end_index is None and pattern_index_matched == len(tags_pattern) - 1:
            end_index = len(tags) - 1
        if start_index is not None and end_index is None:
            return (None, None)  # Should not return a start index but no end index
        return (start_index, end_index)

    # Find the first location in tags where the tag tag appears in the list of tags tag
    # where it is found in the order specified by tags_pattern
    def identify_tag_location(self, tags, tags_pattern, tag, fuzzy=True):
        # Find the location of tags_pattern in tags
        identified_tags = self.identify_tags(tags, tags_pattern, fuzzy)
        # If we did not find the sequence of tags
        if identified_tags == (None, None):
            return (None, None)
        start_index = None
        end_index = None
        # Look through the range found in identify_tags
        for i in range(identified_tags[0],identified_tags[1]+1):
            # We found the tag
            if self.fuzzy_tag_match(tags[i],tag,fuzzy):
                start_index = i
            else:
                # We found a different tag
                if start_index is not None:
                    end_index = i - 1
                    return (start_index, end_index)
        # We found a match but got to the end of the range found in identify_tags
        if start_index is not None:
            return (start_index, identified_tags[1])
        # We did not find a match
        return (None, None)

    def parse_address_first_part(self, address_split, tagged_address, pattern_used, direction_prefix = None):
        address_parts = {
            'housename': None,
            'housenumber': None,
            'street_direction_prefix': None,
            'street_type_fr': None,
            'street_name': None,
            'street_type': None,
            'street_direction_suffix': None
        }
        #housename_location = self.identify_tag_location(tagged_address, pattern_used, 'TEXT')
        #if housename_location != (None, None):
        #    address_parts['housename'] = ' '.join(address_split[housename_location[0]:housename_location[1]+1])
        housenumber_location = self.identify_tag_location(tagged_address, pattern_used, 'NUMBER')
        if housenumber_location != (None, None):
            address_parts['housenumber'] = ' '.join(address_split[housenumber_location[0]:housenumber_location[1]+1])
        # TODO: Can't tell difference between street direction prefix and suffix
        street_direction_location = self.identify_tag_location(tagged_address, pattern_used, 'STREET_DIRECTION')
        if street_direction_location != (None, None):
            street_direction = ' '.join(address_split[street_direction_location[0]:street_direction_location[1]+1])
            # Direction is used as prefix
            if direction_prefix == True:
                address_parts['street_direction_prefix'] = street_direction
            else:
                address_parts['street_direction_suffix'] = street_direction
        street_type_fr_location = self.identify_tag_location(tagged_address, pattern_used, 'STREET_ABBREV_PREFIX')
        if street_type_fr_location != (None, None):
            address_parts['street_type_fr'] = ' '.join(address_split[street_type_fr_location[0]:street_type_fr_location[1]+1])
        street_name_location = self.identify_tag_location(tagged_address, pattern_used, 'TEXT')
        if street_name_location != (None, None):
            address_parts['street_name'] = ' '.join(address_split[street_name_location[0]:street_name_location[1]+1])
        street_type_en_location = self.identify_tag_location(tagged_address, pattern_used, 'STREET_ABBREV_SUFFIX')
        if street_type_en_location != (None, None):
            address_parts['street_type'] = ' '.join(address_split[street_type_en_location[0]:street_type_en_location[1]+1])
        return address_parts

    def parse_address_unit_part(self, address_split, tagged_address, pattern_used):
        address_parts = {
            'suite_num': None,
            'suite_type': None
        }
        suite_num_location = self.identify_tag_location(tagged_address, pattern_used, 'TEXT')
        if suite_num_location != (None, None):
            address_parts['suite_num'] = address_split[suite_num_location[0]]
        suite_type_location = self.identify_tag_location(tagged_address, pattern_used, 'SUITE')
        if suite_type_location != (None, None):
            address_parts['suite_type'] = address_split[suite_type_location[0]]
        return address_parts

    def parse_address_second_part(self, address_split, tagged_address, pattern_used):
        address_parts = {
            'city': None,
            'state': None,
            'province': None,
            'postal_code': None,
            'zip_code': None,
            'country': None
        }
        city_location = self.identify_tag_location(tagged_address, pattern_used, 'CITY')
        if city_location != (None, None):
            address_parts['city'] = ' '.join(address_split[city_location[0]:city_location[1] + 1])
        # If we didn't find a city tagged CITY, use TEXT field
        if not address_parts['city']:
            city_location = self.identify_tag_location(tagged_address, pattern_used, 'TEXT')
            if city_location != (None, None):
                address_parts['city'] = ' '.join(address_split[city_location[0]:city_location[1] + 1])
        state_location = self.identify_tag_location(tagged_address, pattern_used, 'STATE')
        if state_location != (None, None):
            address_parts['state'] = ' '.join(address_split[state_location[0]:state_location[1] + 1])
        province_location = self.identify_tag_location(tagged_address, pattern_used, 'PROVINCE')
        if province_location != (None, None):
            address_parts['province'] = ' '.join(address_split[province_location[0]:province_location[1] + 1])
        # Look for ZIP+4 first, then ZIP
        zip_location = self.identify_tag_location(tagged_address, pattern_used, 'ZIPCODE4')
        if zip_location == (None, None):
            zip_location = self.identify_tag_location(tagged_address, pattern_used, 'ZIPCODE')
        if zip_location != (None, None):
            address_parts['zip_code'] = ' '.join(address_split[zip_location[0]:zip_location[1] + 1])
        # Look for postal code location
        postalcode1_location = self.identify_tag_location(tagged_address, pattern_used, 'POSTAL_CODE_FIRST')
        postalcode2_location = self.identify_tag_location(tagged_address, pattern_used, 'POSTAL_CODE_SECOND')
        postalcode_combo_location = self.identify_tag_location(tagged_address, pattern_used, 'POSTAL_CODE')
        if postalcode_combo_location != (None, None):
            postalcode_combo = address_split[postalcode_combo_location[0]]
            postalcode = postalcode_combo[0:2] + " " + postalcode_combo[3:5]
            address_parts['postal_code'] = postalcode
        elif postalcode1_location != (None, None) and postalcode2_location != (None, None):
            postalcode_first = address_split[postalcode1_location[0]]
            postalcode_second = address_split[postalcode2_location[0]]
            address_parts['postal_code'] = postalcode_first + " " + postalcode_second  # Combine postal code
        country_location = self.identify_tag_location(tagged_address, pattern_used, 'COUNTRY')
        if country_location != (None, None):
            address_parts['country'] = ' '.join(address_split[country_location[0]:country_location[1] + 1])
        return address_parts

    def parse_address_unit_part(self, address_split, tagged_address, pattern_used):
        address_parts = {
            'suite_num': None,
            'suite_type': None
        }
        suite_num_location = self.identify_tag_location(tagged_address, pattern_used, 'NUMBER')
        if suite_num_location == (None, None):
            suite_num_location = self.identify_tag_location(tagged_address, pattern_used, 'TEXT')
        if suite_num_location != (None, None):
            address_parts['suite_num'] = address_split[suite_num_location[0]]
        suite_type_location = self.identify_tag_location(tagged_address, pattern_used, 'SUITE')
        if suite_type_location != (None, None):
            address_parts['suite_type'] = address_split[suite_type_location[0]]
        return address_parts

    def parse_address(self, address: str):
        address_parts_blank = {
            'housename': None,
            'housenumber': None,
            'street_direction_prefix': None,
            'street_type_fr': None,
            'street_name': None,
            'street_type': None,
            'street_direction_suffix': None,
            'suite_num': None,
            'suite_type': None,
            'city': None,
            'state': None,
            'province': None,
            'postal_code': None,
            'zip_code': None,
            'country': None
        }
        address_parts = {}
        # Split by space
        address_no_commas = self.remove_commas(address)
        address_split = address_no_commas.split(" ")
        # Tag the address
        tagged_address = self.tag_address(address)
        # Get first part of address (everything up to street type and street direction suffix if applicable)
        direction_prefix, pattern_used_first_part = self.identify_first_part_tags(tagged_address)
        pattern_used_unit_part = self.identify_unit_part_tags(address_split, tagged_address)
        # Get second part of address (city and everything after it)
        pattern_used_second_part = self.identify_second_part_tags(tagged_address)
        # Parse first part of address
        if pattern_used_first_part is not None:
            parsed_address_first_part = self.parse_address_first_part(address_split, tagged_address, pattern_used_first_part, direction_prefix)
            #print(parsed_address_first_part)
        # Parse unit part of address
        if pattern_used_unit_part is not None:
            parsed_address_unit_part = self.parse_address_unit_part(address_split, tagged_address, pattern_used_unit_part)
            #print(parsed_address_first_part)
        # Parse second part of address
        if pattern_used_second_part is not None:
            parsed_address_second_part = self.parse_address_second_part(address_split, tagged_address, pattern_used_second_part)
            #print(parsed_address_second_part)
        # Combine 1st part and 2nd part
        if pattern_used_first_part or pattern_used_unit_part or pattern_used_second_part:
            if pattern_used_first_part:
                address_parts = self.merge_dictionaries(address_parts_blank, parsed_address_first_part)
            if pattern_used_unit_part:
                address_parts = self.merge_dictionaries(address_parts, parsed_address_unit_part)
            if pattern_used_second_part:
                address_parts = self.merge_dictionaries(address_parts, parsed_address_second_part)
            return address_parts
        # Look for common patterns - TODO should remove some of this as it is redundant
        if tagged_address == ["ZIPCODE4"] or tagged_address == ["ZIPCODE"]:
            address_parts = {
                'zip_code': address_split[0] + address_split[1]
            }
        if tagged_address == ["POSTAL_CODE_FIRST", "POSTAL_CODE_SECOND"]:
            address_parts = {
                'postal_code': address_split[0] + address_split[1]
            }
        if tagged_address == ["CITY"]:
            address_parts = {
                'city': address_split[0]
            }
        if tagged_address == ["PROVINCE"]:
            address_parts = {
                'province': address_split[0]
            }
        if tagged_address == ["STATE"]:
            address_parts = {
                'state': address_split[0]
            }
        if tagged_address == ["COUNTRY"]:
            address_parts = {
                'country': address_split[0]
            }
        # Add blank fields to address
        address_parts = self.merge_dictionaries(address_parts_blank, address_parts)
        return address_parts

    def identify_unit_part_tags(self, address_split, tagged_address):
        # Find something like "Suite 9"
        # See if there is a unit with word (e.g. Suite A) followed by city
        unit_part_tags = self.identify_tags(tagged_address, ["SUITE", "TEXT", "CITY"])
        if unit_part_tags != (None, None):
            pattern_used_unit_part = ["SUITE", "TEXT"]
            # city_part_tags = self.identify_tags(tagged_address, "CITY")
            # unit_part_tags = (unit_part_tags[0], city_part_tags[0])  # Remove city
            return pattern_used_unit_part
        unit_part_tags = self.identify_tags(tagged_address, ["SUITE", "NUMBER", "CITY"])
        if unit_part_tags != (None, None):
            pattern_used_unit_part = ["SUITE", "NUMBER"]
            # city_part_tags = self.identify_tags(tagged_address, "CITY")
            # unit_part_tags = (unit_part_tags[0], city_part_tags[0])  # Remove city
            return pattern_used_unit_part
        unit_part_tags = self.identify_tags(tagged_address, ["SUITE", "TEXT"])
        if unit_part_tags != (None, None):
            pattern_used_unit_part = ["SUITE", "TEXT"]
            # if unit_part_tags != (None, None):
            #     # Is suite number a letter like A, etc.
            #     if len(address_split[unit_part_tags[1]]) == 1 and address_split[unit_part_tags[1]].isalpha():
            #         unit_part_tags = (unit_part_tags[0], unit_part_tags[0] + 1)
            return pattern_used_unit_part
        unit_part_tags = self.identify_tags(tagged_address, ["SUITE", "NUMBER"])
        if unit_part_tags != (None, None):
            pattern_used_unit_part = ["SUITE", "NUMBER"]
            return pattern_used_unit_part
        return None

    def identify_first_part_tags(self, tagged_address):
        # Try to isolate the first part of the address from the second part
        found_tag = False
        patterns = [
            ["TEXT", "NUMBER", "TEXT", "STREET_ABBREV_SUFFIX", "STREET_DIRECTION"],
            ["TEXT", "NUMBER", "STREET_DIRECTION", "TEXT", "STREET_ABBREV_SUFFIX"],
            ["TEXT", "NUMBER", "TEXT", "STREET_ABBREV_SUFFIX"],
            ["TEXT", "NUMBER", "STREET_ABBREV_PREFIX", "TEXT", "STREET_DIRECTION"],
            ["TEXT", "NUMBER", "STREET_ABBREV_PREFIX", "TEXT"],
            ["NUMBER", "TEXT", "STREET_ABBREV_SUFFIX", "STREET_DIRECTION"],
            ["NUMBER", "STREET_DIRECTION", "TEXT", "STREET_ABBREV_SUFFIX"],
            ["NUMBER", "TEXT", "STREET_ABBREV_SUFFIX"],
            ["NUMBER", "STREET_ABBREV_PREFIX", "TEXT", "STREET_DIRECTION"],
            ["NUMBER", "STREET_ABBREV_PREFIX", "TEXT"]
        ]
        step = 0
        pattern_used_first_part = None
        direction_prefix = None
        while not found_tag and step < len(patterns):
            first_part_tags = self.identify_tags(tagged_address, patterns[step])
            if first_part_tags != (None, None):
                found_tag = True
                pattern_used_first_part = patterns[step]
                if step == 1 or step == 6:  # Street direction is a prefix
                    direction_prefix = True
                else:
                    direction_prefix = False
            step = step + 1
        return direction_prefix, pattern_used_first_part

    def identify_second_part_tags(self, tagged_address):
        # Identify tags for second part (city, province/state, country, zip/postal code)
        found_tag = False
        patterns = [
            ["CITY", "PROVINCE", "POSTAL_CODE_FIRST", "POSTAL_CODE_SECOND", "COUNTRY"],
            ["CITY", "PROVINCE", "POSTAL_CODE_FIRST", "POSTAL_CODE_SECOND"],
            ["CITY", "PROVINCE", "POSTAL_CODE", "COUNTRY"],
            ["CITY", "PROVINCE", "POSTAL_CODE"],
            ["CITY", "PROVINCE", "COUNTRY", "POSTAL_CODE_FIRST", "POSTAL_CODE_SECOND"],
            ["CITY", "PROVINCE", "COUNTRY", "POSTAL_CODE"],
            ["CITY", "POSTAL_CODE_FIRST", "POSTAL_CODE_SECOND", "PROVINCE", "COUNTRY"],
            ["CITY", "POSTAL_CODE_FIRST", "POSTAL_CODE_SECOND", "PROVINCE"],
            ["CITY", "POSTAL_CODE", "PROVINCE", "COUNTRY"],
            ["CITY", "POSTAL_CODE", "PROVINCE"],
            ["CITY", "POSTAL_CODE_FIRST", "POSTAL_CODE_SECOND", "COUNTRY"],
            ["CITY", "POSTAL_CODE", "COUNTRY"],
            ["CITY", "COUNTRY", "POSTAL_CODE_FIRST", "POSTAL_CODE_SECOND"],
            ["CITY", "COUNTRY", "POSTAL_CODE"],
            ["CITY", "STATE", "ZIPCODE4", "COUNTRY"],
            ["CITY", "STATE", "ZIPCODE", "COUNTRY"],
            ["CITY", "STATE", "ZIPCODE4"],
            ["CITY", "STATE", "ZIPCODE"],
            ["CITY", "ZIPCODE4", "STATE", "COUNTRY"],
            ["CITY", "ZIPCODE", "STATE", "COUNTRY"],
            ["CITY", "ZIPCODE4", "STATE"],
            ["CITY", "ZIPCODE", "STATE"],
            ["CITY", "STATE", "COUNTRY"],
            ["CITY", "COUNTRY", "ZIPCODE4"],
            ["CITY", "COUNTRY", "ZIPCODE"],
            ["CITY", "COUNTRY"],
            # TEXT is unknown city
            ["TEXT", "PROVINCE", "POSTAL_CODE_FIRST", "POSTAL_CODE_SECOND", "COUNTRY"],
            ["TEXT", "PROVINCE", "POSTAL_CODE_FIRST", "POSTAL_CODE_SECOND"],
            ["TEXT", "PROVINCE", "POSTAL_CODE", "COUNTRY"],
            ["TEXT", "PROVINCE", "POSTAL_CODE"],
            ["TEXT", "PROVINCE", "COUNTRY", "POSTAL_CODE_FIRST", "POSTAL_CODE_SECOND"],
            ["TEXT", "PROVINCE", "COUNTRY", "POSTAL_CODE"],
            ["TEXT", "POSTAL_CODE_FIRST", "POSTAL_CODE_SECOND", "PROVINCE", "COUNTRY"],
            ["TEXT", "POSTAL_CODE_FIRST", "POSTAL_CODE_SECOND", "PROVINCE"],
            ["TEXT", "POSTAL_CODE", "PROVINCE", "COUNTRY"],
            ["TEXT", "POSTAL_CODE", "PROVINCE"],
            ["TEXT", "POSTAL_CODE_FIRST", "POSTAL_CODE_SECOND", "COUNTRY"],
            ["TEXT", "POSTAL_CODE", "COUNTRY"],
            ["TEXT", "COUNTRY", "POSTAL_CODE_FIRST", "POSTAL_CODE_SECOND"],
            ["TEXT", "COUNTRY", "POSTAL_CODE"],
            ["TEXT", "STATE", "ZIPCODE4", "COUNTRY"],
            ["TEXT", "STATE", "ZIPCODE", "COUNTRY"],
            ["TEXT", "STATE", "ZIPCODE4"],
            ["TEXT", "STATE", "ZIPCODE"],
            ["TEXT", "ZIPCODE4", "STATE", "COUNTRY"],
            ["TEXT", "ZIPCODE", "STATE", "COUNTRY"],
            ["TEXT", "ZIPCODE4", "STATE"],
            ["TEXT", "ZIPCODE", "STATE"],
            ["TEXT", "STATE", "COUNTRY"],
            ["TEXT", "COUNTRY", "ZIPCODE4"],
            ["TEXT", "COUNTRY", "ZIPCODE"],
            ["TEXT", "COUNTRY"]
        ]
        step = 0
        pattern_used_second_part = None
        while not found_tag and step < len(patterns):
            second_part_tags = self.identify_tags(tagged_address, patterns[step])
            if second_part_tags != (None, None):
                found_tag = True
                pattern_used_second_part = patterns[step]
            step = step + 1
        return pattern_used_second_part
