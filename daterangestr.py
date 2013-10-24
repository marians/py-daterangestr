#!/usr/bin/python
# encoding: utf-8

"""
Utility to convert strings to start and end datetime tuples

The MIT License (MIT)

Copyright (c) 2013 Marian Steinbach

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import datetime
from calendar import monthrange


def to_dates(param):
    """
    This function takes a date string in various formats
    and converts it to a normalized and validated date range. A list
    with two elements is returned, lower and upper date boundary.

    Valid inputs are, for example:
    2012              => Jan 1 20012 - Dec 31 2012 (whole year)
    201201            => Jan 1 2012  - Jan 31 2012 (whole month)
    2012101           => Jan 1 2012 - Jan 1 2012   (whole day)
    2011-2011         => same as "2011", which means whole year 2012
    2011-2012         => Jan 1 2011 - Dec 31 2012  (two years)
    201104-2012       => Apr 1 2011 - Dec 31 2012
    201104-201203     => Apr 1 2011 - March 31 2012
    20110408-2011     => Apr 8 2011 - Dec 31 2011
    20110408-201105   => Apr 8 2011 - May 31 2011
    20110408-20110507 => Apr 8 2011 - May 07 2011
    2011-             => Jan 1 2012 - Dec 31 9999 (unlimited)
    201104-           => Apr 1 2011 - Dec 31 9999 (unlimited)
    20110408-         => Apr 8 2011 - Dec 31 9999 (unlimited)
    -2011             Jan 1 0000 - Dez 31 2011
    -201104           Jan 1 0000 - Apr 30, 2011
    -20110408         Jan 1 0000 - Apr 8, 2011
    """
    pos = param.find('-')
    lower, upper = (None, None)
    if pos == -1:
        # no seperator given
        lower, upper = (param, param)
    else:
        lower, upper = param.split('-')
    ret = (expand_date_param(lower, 'lower'), expand_date_param(upper, 'upper'))
    return ret


def expand_date_param(param, lower_upper):
    """
    Expands a (possibly) incomplete date string to either the lowest
    or highest possible contained date and returns
    datetime.date for that string.

    0753 (lowest) => 0753-01-01
    2012 (highest) => 2012-12-31
    2012 (lowest) => 2012-01-01
    201208 (highest) => 2012-08-31
    etc.
    """
    year = 0
    month = 0
    day = 0
    if len(param) == 0:
        if lower_upper == 'lower':
            year = datetime.MINYEAR
            month = 1
            day = 1
        else:
            year = datetime.MAXYEAR
            month = 12
            day = 31
    elif len(param) == 4:
        year = int(param)
        if lower_upper == 'lower':
            month = 1
            day = 1
        else:
            month = 12
            day = 31
    elif len(param) == 6:
        year = int(param[0:4])
        month = int(param[4:6])
        if lower_upper == 'lower':
            day = 1
        else:
            (firstday, dayspermonth) = monthrange(year, month)
            day = dayspermonth
    elif len(param) == 8:
        year = int(param[0:4])
        month = int(param[4:6])
        day = int(param[6:8])
    else:
        # wrong input length
        return None
    # force numbers into valid ranges
    year = min(datetime.MAXYEAR, max(datetime.MINYEAR, year))
    month = min(12, max(1, month))
    (firstday, dayspermonth) = monthrange(year, month)
    day = min(dayspermonth, max(1, day))
    return datetime.date(year=year, month=month, day=day)


def test():
    print "Running tests:"
    print to_dates('2012')
    print to_dates('201201')
    print to_dates('20121001')
    print to_dates('2011-2011')
    print to_dates('2011-2012')
    print to_dates('201104-2012')
    print to_dates('201104-201203')
    print to_dates('20110408-2011')
    print to_dates('2011-')
    print to_dates('201104-')
    print to_dates('20110408-')
    print to_dates('-2011')
    print to_dates('-201104')
    print to_dates('-20110408')
    print to_dates('200902')
    print to_dates('201002')
    print to_dates('201102')
    print to_dates('201202')
    print to_dates('201302')

if __name__ == '__main__':
    test()
