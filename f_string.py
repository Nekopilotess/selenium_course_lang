# catalog_text = self.catalog_link.text # считываем текст и записываем его в переменную
# assert catalog_text == "Каталог", \
# f"Wrong language, got {catalog_text} instead of 'Каталог'"

def test_input_text(expected_result, actual_result):
    assert (expected_result == actual_result), f"expected {expected_result}, got {actual_result}"

s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')

assert "login" in browser.current_url, # сообщение об ошибке

def test_substring(fulltext, some_value):
    assert some_value in full_string, f"expected '{some_value}' to be substring of '{fulltext}'"

