from hello import say_hello, add


def test_say_hello():
    assert (
        say_hello('Aria') == 
        'Hello, Aria, welcome to Data Engineering Systems (IDS 706)!'
    )
    assert (
        say_hello('Jerry') == 
        'Hello, Jerry, welcome to Data Engineering Systems (IDS 706)!'
    )
 

def test_add():
    assert (
        add(0, 1) == 1
    )
    assert (
        add(1, -1) == 0
    )
    assert (
        add(1_000_000, 2_000_000) == 3_000_000
    )
