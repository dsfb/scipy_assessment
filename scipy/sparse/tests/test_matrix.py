from __future__ import division, print_function, absolute_import

import numpy as np
from numpy.testing import assert_array_almost_equal, assert_, assert_raises
from scipy.sparse import csr_matrix


def test_check_round_csr_matrix():
    a = csr_matrix((3, 4))
    assert_("__round__" in dir(a))


def test_check_round_csr_matrix2():
     A = csr_matrix([[-1, 0, 17],[0, -5, 0],[1, -4, 0],[0,0,0]],'d')
     assert_equal(round(A), round(self.spmatrix(A)).todense())
