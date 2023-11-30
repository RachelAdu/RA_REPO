import pytest

# check if error occurs if string is given
def addition(a,b):
    return a + b
def test_both_are_numbers():
    assert addition(5.0,6.0) == 11
def test_number_and_string():
    with pytest.raises(TypeError):
        addition('c', 15)

# check if function only accepts a number in range
def mock_customer_input():
    return 15
def selection_from_list(input):
    test_list = ["orange", "lemon", "strawberry", "kiwi"]
    assert input in ((range(len((test_list)))))
    return input + 1
def test_selection_error():
    with pytest.raises(Exception):
        selection_from_list(mock_customer_input)
def test_positive_selection():
    assert selection_from_list(3) == 4
    
# check if eror occurs if phone number does't have 11 digits
   

