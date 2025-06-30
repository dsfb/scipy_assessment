from __future__ import division, print_function, absolute_import

import numpy as np
from numpy.testing import assert_array_almost_equal, assert_equal, assert_, assert_raises
from scipy.sparse import base, csr_matrix


def test_check_round_csr_matrix():
    a = csr_matrix((3, 4))
    assert_("__round__" in dir(a))


def test_check_round_csr_matrix2():
     A = csr_matrix((5, 7))
     assert_equal(round(A), round(base.spmatrix(A)).todense())
