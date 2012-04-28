# Randat generates random data.
from random import seed as _seed, randint, choice
import string
from datetime import date
from time import mktime
import re

_DATE_RE = re.compile('([0-9]{4})-([0-9]{2})-([0-9]{2})')

def _set_seed(seed=None):
  if seed is not None:
    _seed(seed)

def random_int(min=0, max=100, seed=None):
  _set_seed(seed)
  return randint(min, max)

def random_string(length=5, chars=string.lowercase, seed=None):
  _set_seed(seed)
  s = ''
  for i in xrange(length):
    s += choice(chars)
  return s

def random_ip(seed=None):
  _set_seed(seed)
  return '%s.%s.%s.%s' % (random_int(max=255), random_int(max=255), random_int(max=255), random_int(max=255))

def _date_to_timestamp(s):
  """Parse a date in yyyy-mm-dd format and return a Unix timestamp. 
  
  The date is assumed to be UTC."""
  m = _DATE_RE.match(s)
  if m is None:
    raise ValueError('Date should be in yyyy-mm-dd format.')
  year, month, day = (int(v) for v in m.groups())
  d = date(year, month, day)
  return mktime(d.timetuple())

def random_timestamp(min=None, max=None, seed=None):
  if min is None:
    min = _date_to_timestamp('2000-01-01')
  else:
    min = _date_to_timestamp(min)
  if max is None:
    max = _date_to_timestamp('2020-12-31')
  else:
    max = _date_to_timestamp(max)
  return random_int(min=min, max=max, seed=seed)

