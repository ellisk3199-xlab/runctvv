
# the greeting string
def get_greeting() -> str:
    return "Welcome back Bob!"

# print
def greet():
    print(get_greeting())

# smoke test
def test_greeting_string():
    # Assert against the returned string directly
    assert get_greeting() == "Welcome back Bob!"
