from __future__ import division, print_function, absolute_import

import numpy as np
from numpy.testing import assert_array_almost_equal, assert_, assert_raises
from scipy.sparse import csr_matrix


def _check_round_csr_matrix():
    a = csr_matrix((3, 4))
    assert_raises(AssertionError, assert_raises, TypeError, round(a))
    assert_(assert_raises(TypeError, round(a))  is None)

