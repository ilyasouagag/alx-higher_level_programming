#!/usr/bin/python3
"""a function that multiplicate two matrix and return a new one"""


def matrix_mul(m_a, m_b):
    """function that multiplicate two matrix and return a new one
        matrix a * matrix b = matrix c"""
    m_c = []
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
    if m_a in ([], [[]]):
        raise ValueError("m_a can't be empty")
    if m_b in ([], [[]]):
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    for row in range(len(m_a)):
        a = []
        for col in range(len(m_b[0])):
            a.append(0)
        m_c.append(a)
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for n in range(len(m_a[0])):
                m_c[i][j] += m_a[i][n] * m_b[n][j]
    return m_c
