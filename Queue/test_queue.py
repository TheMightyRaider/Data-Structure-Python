from arrayqueue import Queue

class TestQueue:
    def test_push(self):
        q=Queue()
        
        assert q.data==[]
        q.enqueue(1)
        assert q.data==[1]
        q.enqueue(2)
        assert q.data==[1,2]

    def test_delete(self):
        q=Queue()
        q.enqueue(1)
        q.enqueue(2)
        assert q.data==[1,2]
        q.dequeue()
        assert q.data==[2]
