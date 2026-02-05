import builtins
import pytest

import tsp


# euclid 
# перевірка правильності обчислення евклідової дистанції
def test_dist():
    """TC9: перевірка правильності обчислення евклідової дистанції"""
    assert tsp.euclid((0, 0), (3, 4)) == 5.0


# перевірка нульової дистанції між однаковими містами
def test_dist_zero():
    """TC9: перевірка нульової дистанції між однаковими містами"""
    assert tsp.euclid((1, 1), (1, 1)) == 0.0



# check_tsp_points 

# перевірка коректного набору міст (без помилок)
def test_check_ok():
    """TC10: перевірка коректного набору міст (без помилок)"""
    tsp.check_tsp_points([(0, 0), (1, 1), (2, 2)])


# перевірка обмеження: кількість міст менша за 2
def test_check_less_two():
    """TC2: перевірка обмеження — кількість міст менша за 2"""
    with pytest.raises(tsp.Input):
        tsp.check_tsp_points([(0, 0)])


# перевірка заборони дублікатів координат міст
def test_check_duplicate():
    """TC8: перевірка заборони дублікатів координат міст"""
    with pytest.raises(tsp.Input):
        tsp.check_tsp_points([(1, 2), (1, 2)])



# build_matrix 

# перевірка розміру матриці відстаней
def test_matrix_size():
    """TC10: перевірка розміру матриці відстаней"""
    m = tsp.build_matrix([(0, 0), (1, 0), (0, 1)])
    assert len(m) == 3
    assert all(len(r) == 3 for r in m)


# перевірка нулів на головній діагоналі матриці
def test_matrix_diag():
    """TC12: перевірка нулів на головній діагоналі матриці"""
    m = tsp.build_matrix([(0, 0), (1, 0), (0, 1)])
    assert m[0][0] == 0.0
    assert m[1][1] == 0.0
    assert m[2][2] == 0.0


# перевірка симетричності матриці відстаней
def test_matrix_sym():
    """TC11: перевірка симетричності матриці відстаней"""
    m = tsp.build_matrix([(0, 0), (3, 4)])
    assert m[0][1] == m[1][0]


# перевірка правильного значення дистанції у матриці
def test_matrix_value():
    """TC10/TC11: перевірка правильного значення дистанції у матриці"""
    m = tsp.build_matrix([(0, 0), (3, 4)])
    assert m[0][1] == 5.0


# перевірка помилки при дублікатах точок у матриці
def test_matrix_dup():
    """TC8: перевірка помилки при дублікатах точок у матриці"""
    with pytest.raises(tsp.Input):
        tsp.build_matrix([(0, 0), (0, 0)])


# перевірка виводу матриці у консоль
def test_print_matrix(capsys):
    """TC13: перевірка виводу матриці у консоль (формат з 2 знаками після коми)"""
    m = [[0.0, 1.0], [1.0, 0.0]]
    tsp.print_matrix(m)

    out = capsys.readouterr().out
    assert "0.00 1.00" in out
    assert "1.00 0.00" in out



# read_int 

# перевірка введення числа некоректних значень
def test_read_int(monkeypatch):
    """TC1/TC2/TC3: перевірка введення числа з некоректними значеннями"""
    data = iter(["", "a", "1", "5"])
    monkeypatch.setattr(builtins, "input", lambda _: next(data))

    n = tsp.read_int("n: ")
    assert n == 5



# read_point 

# перевірка введення координат міста з помилками та коректним значенням
def test_point(monkeypatch):
    """TC4/TC5/ТС6: перевірка введення координат міста з помилками та коректним значенням"""
    data = iter(["", "10", "a b"," 5", "1 2"])
    monkeypatch.setattr(builtins, "input", lambda _: next(data))

    x, y = tsp.read_points("c: ")
    assert x == 1.0
    assert y == 2.0


# перевірка допустимих граничних координат
def test_point_limits(monkeypatch):
    """TC7: перевірка допустимих граничних координат"""
    data = iter(["-1000 1000"])
    monkeypatch.setattr(builtins, "input", lambda _: next(data))

    x, y = tsp.read_points("c: ")
    assert x == -1000.0
    assert y == 1000.0
