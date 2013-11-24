py-daterangestr
===============

Create meaningful date/time ranges using strings like e.g. "201301" or "201301-201302".

## Install

    pip install daterangestr

## Quickstart

The `daterangestr` has exactly one function, `to_dates`, which converts a date string
of a certain, simple format to a datetime tuple.

### Example:

```python
>>> from daterangestr import to_dates
>>> (start, end) = to_dates("20131014-20131018")
>>> print start, end
2013-10-14 00:00:00 2013-10-18 23:59:59
```

## Supported string formats

### Rules

1. Dates can be given in format `YYYY`, `YYYYMM` or `YYYYMMDD`.
2. The date string can contain either only one date or two dates, seperated by a dash.
3. If the dash seperator is present and only one date is given, the other date is assumed to be the minimum possible or the maximum possible date.

### Examples

#### 2012

Jan 1 2012 - Dec 31 2012 (whole year)

#### 201201

Jan 1 2012  - Jan 31 2012 (whole month)

#### 2012101

Jan 1 2012 - Jan 1 2012   (whole day)

#### 2011-2011

same as "2011", which means whole year 2012

#### 2011-2012

Jan 1 2011 - Dec 31 2012  (two years)

#### 201104-2012

Apr 1 2011 - Dec 31 2012

#### 201104-201203

Apr 1 2011 - March 31 2012

#### 20110408-2011

Apr 8 2011 - Dec 31 2011

#### 20110408-201105

Apr 8 2011 - May 31 2011

#### 20110408-20110507

Apr 8 2011 - May 07 2011

#### 2011-

Jan 1 2012 - Dec 31 9999 (unlimited)

#### 201104-

Apr 1 2011 - Dec 31 9999 (unlimited)

#### 20110408-

Apr 8 2011 - Dec 31 9999 (unlimited)

#### -2011

Jan 1 0000 - Dez 31 2011

#### -201104

Jan 1 0000 - Apr 30, 2011

#### -20110408

Jan 1 0000 - Apr 8, 2011
