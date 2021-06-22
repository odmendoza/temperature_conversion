import pytest

from temperature_conversion import __version__
from temperature_conversion.convert import f_to_k, c_to_r, c_to_f 


def test_version():
    assert __version__ == '1.0.0'


@pytest.mark.parametrize(
    "tf, tk_esperado", 
    [
        (32, 273.15),
        (0, 255.372),
        (8, 259.817), 
        (None, None)
    ]
)
def test_f_to_k(tf, tk_esperado):
    tf = f_to_k(tf)
    assert pytest.approx(tf, 0.2) == tk_esperado
    

@pytest.mark.parametrize(
    "tc, tr_esperado", 
    [
        (32, 549.27),
        (0, 491.67),
        (8, 506.07), 
        (None, None)
    ]
)
def test_c_to_r(tc, tr_esperado):
    tc = c_to_r(tc)
    assert pytest.approx(tc, 0.2) == tr_esperado


@pytest.mark.parametrize(
    "tc, tf_esperado", 
    [
        (32, 89.6),
        (0, 32),
        (8, 46.4),
        (None, None)
    ]
)
def test_c_to_f(tc, tf_esperado):
    tc = c_to_f(tc)
    assert pytest.approx(tc, 0.2) == tf_esperado
