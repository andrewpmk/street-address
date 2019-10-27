#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import logging
# import json
# import six
# import unittest
# from optparse import OptionParser
#from streetaddress import StreetAddressFormatter, StreetAddressParser, StreetAddress
from streetaddress import StreetAddress

########################################################################
# Test
########################################################################
if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG,
#                         format='%(asctime)-8s %(levelname)-8s %(message)s',
#                         datefmt='%H:%M:%S'
#                         )
#     usage = """Usage: %prog [options]
#
# Examples:
#     ./%prog --addr="366 West 52nd Street  New York, NY 10019"
#     ./%prog --addr="135-20 40th ROAD, queens, NY 11354"
#     ./%prog --addr="22-15 31st St, 11105"
#
#     """
#     optp = OptionParser(usage=usage)
#
#     optp.add_option('--addr', help='address to parse',
#             action='store', type='string', dest="addr", default=None)
#     opts, args = optp.parse_args()
#
#     #if not opts.addr:
#     #    optp.error('addr must be specified')
#     #orig_addr = opts.addr
#
#     tests = """\
#         3120 De la Cruz Boulevard
#         100 South Street
#         123 Main
#         221B Baker Street
#         10 Downing St
#         1600 Pennsylvania Ave
#         33 1/2 W 42nd St.
#         454 N 38 1/2
#         21A Deer Run Drive
#         256K Memory Lane
#         12-1/2 Lincoln
#         23N W Loop South
#         23 N W Loop South
#         25 Main St
#         2500 14th St
#         12 Bennet Pkwy
#         Pearl St
#         Bennet Rd and Main St
#         19th St
#         1500 Deer Creek Lane
#         2081 N Webb Rd
#         2081 N. Webb Rd
#         1515 West 22nd Street
#         2029 Stierlin Court
#         P.O. Box 33170
#         The Landmark @ One Market, Suite 200
#         One Market, Suite 200
#         One Market
#         One Union Square
#         One Union Square, Apt 22-C
#         186 Avenue A
#         10 Avenue of America
#         25 West St
#         """.split("\n")
#
#     addr_parser = StreetAddressParser()
#     addr_formatter = StreetAddressFormatter()
#
#     if opts.addr:
#         lst = [opts.addr]
#     else:
#         lst = map(str.strip,tests)
#
#     for t in lst:
#         if t:
#             print('"%s"' % t)
#             logging.info('addr_str: ' + six.text_type(t))
#             addr = addr_parser.parse(t)
#
#             if addr['street_full'] is not None:
#                 street = addr_formatter.append_TH_to_street(addr['street_full'])
#                 logging.info('After append_TH_to_street: ' + street)
#
#                 street = addr_formatter.abbrev_direction(street)
#                 logging.info('After abbrev_direction: ' + street)
#
#                 street = addr_formatter.abbrev_street_avenue_etc(street)
#                 logging.info('After abbrev_street_avenue_etc: ' + street)
#
#                 street = addr_formatter.abbrev_street_avenue_etc(street, abbrev_only_last_token=False)
#                 logging.info('After abbrev_street_avenue_etc (aggressive): ' + street)
#
#             print(json.dumps(addr, sort_keys=True))

    # New testing code
    handler = StreetAddress()
    test_cases = [
        "180 Bloor St W Suite 1401, Toronto ON M5S 2V6 Canada",
        "26 Vandalay Cres, Kingston, Ontario, K7L 5T9",
        "26 Vandalay Cr, Kingston, Ontario, K7L 5T9",
        "100 3rd St W, New York NY 10001",
        "800 Main Street East, Ontario CA 93003",
        "800 Main Street East, Ontario CA 93003 United States",
        "100 E St, Washington DC",
        "180 Avenue Rd Toronto ON",
        "180 Avenue Toronto ON",
        "Jane Doe & John Moe, 253 Merton St J200, Toronto, ON, M4S 1C6",
        "The White House, 1600 Pennslyvania Ave NW, Washington, DC 20500, USA",
        "Donald Trump, 688 Kingston ON, Canada",
        "Justin Trudeau, 24 Sussex Dr, Ottawa, ON K1M 1M4",
        "Justin Trudeau, 24 Sussex Dr, Ottawa, ON K1M1M4",
        "77 Main St, Torontoo, Ontario, N2L 2K2", # Misspelled Toronto and mismatched postal code
        "199 Endy St, Missisauga, ON", # Misspelled Mississauga
        "John Tory, 1 Bedford Rd, Toronto ON",
        # From https://www.randomlists.com/random-addresses
        "184 Lees Creek Ave. Bonita Springs, FL 34135",
        "7554 N. Henry Smith St. Lowell, MA 01851",
        "65 Henry Smith St. Ballston Spa, NY 12020",
        "816 Saxton Ave. Fairfield, CT 06824",
        "244 Deerfield Street Lynn, MA 01902",
        "8626 Deerfield Court Kalispell, MT 59901",
        "229 Fairway St. Dawsonville, GA 30534",
        "75 Piper St. Ronkonkoma, NY 11779",
        "69 West Williams Road South Ozone Park, NY 11420",
        "381 Golden Star Road La Vergne, TN 37086",
        "7887 Albany Lane, Ellenwood, GA 30294",
        "9216 Manchester Rd. Passaic, NJ 07055",
        "234 S. Sunnyslope Drive St. Martins, NB E5R 8C8",
        "59 Cardinal Lane Dufferin County, ON L0N 4V7",
        "48 W. Liberty Dr. Kapuskasing, ON P5N 8E1",
        "29 San Carlos St. Orillia, ON L3V 6H9",
        "672 Riverside Dr. Tecumseh, ON N8V 7E1",
        "18 Fremont Ave. Apt 4 Red Bank, NB E9E 2N5",
        "362 San Juan Ave. Woodbridge, VA 22191",
        "64 Madison St. Chillicothe, OH 45601",
        "7176 Elizabeth Street Davenport, IA 52804",
        "440 Virginia Rd. Canyon Country, CA 91387",
        "8474 Rockaway St. San Antonio, TX 78213",
        "29 Silver Spear Lane Sylvania, OH 43560"
        # From https://www.bestrandoms.com/random-address
        "1428 De Courmont Rue Gautier, Mississippi(MS), 39553",
        "1441 Private 1975 Rd Gladewater, Texas(TX), 75647",
        "420 Hillside Ave Waverly, Ohio(OH), 45690",
        "4214 Galiceno Cedar Park, Texas(TX), 78613",
        "220 Scandia Cir Athens, Georgia(GA), 30605",
        "8320 Banet Rd Floyds Knobs, Indiana(IN), 47119",
        "10246 Jamestown Rd Ashland, Virginia(VA), 23005",
        "514 Moriah Noel Dr Resaca, Georgia(GA), 30735",
        "5313 W Thompson St Philadelphia, Pennsylvania(PA), 19131",
    ]
    print("Test: find_word(\"Canada\", \"Toronto Canada\")")
    print(handler.find_word("Canada", "Toronto Canada"))
    print("Test: find_word(\"Montreal\", \"Toronto Montreal Canada\")")
    print(handler.find_word("Montreal", "Toronto Montreal Canada"))
    print("Test: find_word(\"Montreal Canada\", \"Toronto Montreal Canada\")")
    print(handler.find_word("Montreal Canada", "Toronto Montreal Canada"))
    for i in test_cases:
        print("Test: tag_address\(\"" + i + "\")")
        print(handler.tag_address(i))
        print("Test: parse_address\(\"" +i + "\")")
        print(handler.parse_address(i))

    print("Identify pattern test")
    print(handler.identify_tags(["TEST","NUMBER","STREET","STREET_ABBREV_SUFFIX","CITY","PROVINCE"],["NUMBER","STREET","STREET_ABBREV_SUFFIX"]))