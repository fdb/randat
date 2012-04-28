import unittest

import randat

class RandatTest(unittest.TestCase):

  def test_random_number(self):
    self.assertEquals(64, randat.random_int(seed=42))

  def test_random_string(self):
    self.assertEquals('qahft', randat.random_string(seed=42))
    self.assertEquals('qahftrxc', randat.random_string(length=8, seed=42))
    self.assertEquals('aaaaa', randat.random_string(chars='a'))

  def test_random_ip(self):
    self.assertEquals('163.6.70.57', randat.random_ip(seed=42))

  def test_random_timestamp(self):
    self.assertEquals(1370421666, randat.random_timestamp(seed=42))
    self.assertEquals(1333663200, randat.random_timestamp(min='2012-04-06', max='2012-04-06', seed=42))

if __name__=='__main__':
  unittest.main()

