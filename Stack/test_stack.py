from stack import Stack

class TestStack():
    def test_empty(self):
        s = Stack()
        # After creating, stack must be empty
        assert s.isEmpty()

        s.push(1)
        assert not s.isEmpty()

    def test_push(self):
        s = Stack()
        assert s.data == []

        s.push(1)
        assert s.data == [1]

        s.push(2)
        assert s.data == [1, 2]

    def test_pop(self):
        s= Stack()
        s.push(1)
        assert s.data == [1]
        s.pop()
        assert s.data == []
 


