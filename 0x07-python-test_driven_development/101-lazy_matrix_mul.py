#!/usr/bin/python3
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    return (np.matmul(m_a, m_b))
print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
