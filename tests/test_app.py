from app.app import dedupe_header, add_numbers

def test_unique_columns():
    """测试没有重复列名的情况"""
    assert dedupe_header(["id", "name", "age"]) == ["id", "name", "age"]

def test_duplicate_columns():
    """测试所有列名都相同的情况"""
    assert dedupe_header(["id", "id", "id"]) == ["id", "id.1", "id.2"]

def test_mixed_columns():
    """测试混合列名的情况"""
    cols = ["id", "name", "id", "name", "name"]
    expected = ["id", "name", "id.1", "name.1", "name.2"]
    assert dedupe_header(cols) == expected

def test_empty_list():
    """测试空列表的情况"""
    assert dedupe_header([]) == []

def test_single_column():
    """测试只有一个列名的情况"""
    assert dedupe_header(["column"]) == ["column"]

def test_complex_pattern():
    """测试更复杂的重复模式"""
    cols = ["a", "b", "a", "c", "b", "a", "b", "c", "c"]
    expected = ["a", "b", "a.1", "c", "b.1", "a.2", "b.2", "c.1", "c.2"]
    assert dedupe_header(cols) == expected

def test_add_positive_numbers():
    """测试正数相加"""
    assert add_numbers(5.0, 3.0) == 8.0

def test_add_negative_numbers():
    """测试负数相加"""
    assert add_numbers(-2.0, -3.0) == -5.0

def test_add_mixed_numbers():
    """测试正负数相加"""
    assert add_numbers(10.0, -5.0) == 5.0

def test_add_zero():
    """测试与零相加"""
    assert add_numbers(7.0, 0.0) == 7.0
    assert add_numbers(0.0, 7.0) == 7.0

def test_add_decimal_numbers():
    """测试小数相加"""
    assert add_numbers(1.5, 2.7) == 4.2