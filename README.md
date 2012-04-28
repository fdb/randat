Randat generates random data.
=============================

The rationale behind this was to be able to generate real-world data for load testing. Often when faced with this problem I would copy a few lines of real data and store them over and over. This had the side effect that keys were not distributed evenly, resulting in unreliable performance numbers.

The API is simple and consistent:

    >>> import randat

    >>> randat.random_int()
    42 # Because I haven't specified a seed, your output will vary.
    >> randat.random_int(seed=42) # Every random function takes in a seed.
    64
    >>> randat.random_int(min=-100, max=0, seed=42) # Use min/max to specify the range.
    -36

    >>> randat.random_string(seed=42)
    'qahft'
    >>> randat.random_string(length=10, chars='ARGH', seed=42)
    'GARAGGHARA'

    >>> randat.random_timestamp(seed=42)
    1370421666 # 2013-06-05
    >> randat.random_timestamp(min='2012-01-01', max='2012-12-31', seed=42)
    1345537364 # 2012-08-21

    >>> randat.random_ip(seed=42)
    '163.6.70.57'

Randat is free software, licensed under the MIT License. See LICENSE for details.
