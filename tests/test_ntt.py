"""Tests for ntt.py."""
import os
import unittest
from util.ntt import NTTContext, FFTContext
from util.polynomial import Polynomial
from util.random_sample import sample_uniform
from tests.helper import check_complex_vector_approx_eq

TEST_DIRECTORY = os.path.dirname(__file__)


class TestNTT(unittest.TestCase):
    def setUp(self):
        self.ntt = NTTContext(poly_degree=4, coeff_modulus=73)

    def test_ntt(self):
        fwd = self.ntt.ntt(coeffs=[0, 1, 4, 5], rou=self.ntt.roots_of_unity)
        self.assertEqual(fwd, [10, 34, 71, 31])

    def test_intt(self):
        coeffs = [10, 34, 71, 31]
        coeffs = [(coeffs[i] * -18) % 73 for i in range(4)]
        inv = self.ntt.ntt(coeffs=coeffs, rou=self.ntt.roots_of_unity_inv)
        self.assertEqual(inv, [0, 1, 4, 5])

    def test_fft(self):
        """Checks that fft_fwd and fft_inv are inverses.

        Performs the FFT on the input vector, performs the inverse FFT on the result,
        and checks that they match.

        Raises:
            ValueError: An error if test fails.
        """
        n = 1 << 5
        context = FFTContext(M = 4 * n)
        vec = sample_uniform(0, 7, n)
        fft_vec = context.fft_fwd(vec)
        to_check = context.fft_inv(fft_vec)

        check_complex_vector_approx_eq(vec, to_check, 0.000001, "fft_inv is not the inverse of fft_fwd")

    def test_emb(self):
        """Checks that emb and emb_inv are inverses.

        Performs the EMB on the input vector, performs the inverse EMB on the result,
        and checks that they match.

        Raises:
            ValueError: An error if test fails.
        """
        n = 1 << 5
        context = FFTContext(M = 4 * n)

        vec = sample_uniform(0, 7, n)
        fft_vec = context.emb(vec)
        to_check = context.emb_inv(fft_vec)

        check_complex_vector_approx_eq(vec, to_check, 0.000001, "emb_inv is not the inverse of emb")

if __name__ == '__main__':
    res = unittest.main(verbosity=3, exit=False)
