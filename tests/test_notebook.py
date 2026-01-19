from testbook import testbook

@testbook('/Users/ldegroot/exrepo/exrepo/test_notebook.ipynb', execute=True)
def test_foo(tb):
    foo = tb.ref("foo")

    assert foo(2) == 3

