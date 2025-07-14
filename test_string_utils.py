from string_utils import StringUtils


utils = StringUtils()


def test_capitalize_positive():
    assert utils.capitalize("skypro") == "Skypro"
    assert utils.capitalize("hello world") == "Hello world"
    assert utils.capitalize("python") == "Python"


def test_capitalize_negative():
    assert utils.capitalize("") == ""
    assert utils.capitalize(" ") == " "
    assert utils.capitalize("123abc") == "123abc"


def test_trim_positive():
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("             hello world") == "hello world"
    assert utils.trim("          python") == "python"


def test_trim_negative():
    assert utils.trim("skypro") == "skypro"
    assert utils.trim("") == ""
    assert utils.trim("12 35") == "12 35"


def test_contains_positive():
    assert utils.contains("SkyPro", "S") is True
    assert utils.contains("Hello world", "w") is True
    assert utils.contains("Python", "o") is True


def test_contains_negative():
    assert utils.contains("SkyPro", "U") is False
    assert utils.contains("Hello world", "1") is False
    assert utils.contains("Python", "  ") is False


def test_delete_symbol_positive():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("Hello world", " world") == "Hello"
    assert utils.delete_symbol("SkyPro", "SkyPro") == ""


def test_delete_symbol_negative():
    assert utils.delete_symbol("SkyPro", "z") == "SkyPro"
    assert utils.delete_symbol("", "k") == ""
    assert utils.delete_symbol("SkyPro", "123") == "SkyPro"
