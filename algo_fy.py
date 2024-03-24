import heapq

'''
 You are working for a promising new music streaming service “Algo-fy”.
 Algo-fy would like to offer a new ranking feature that will track the top k most streamed songs of the day.

 You’ve been tasked with building a class “AlgoFy” that can track the most streamed songs
 and return an accurate list top k list at any point in time.

 Another team has already developed the song streaming feature: iStream and you will need to integrate with it.
 iStream will send AlgoFy play data as it processes customer requests.
 This data will be batched so the AlgoFy class will need to ingest lists of played songs multiple times

 A song is identified with an integer id number.

 The AlgoFy class will need to have the following methods:
 - Constructor(k): the number of songs to track in the topk
 - streamSongs(List of songIds): Receive a batch of streamed songs => updates internal state
 - getTopK(): return the top k most streamed songs in order

 As an example, the AlgoFy class may see the following usage:
 ranker = new AlgoFy(2)
 ranker.streamSongs([1, 1, 2, 2, 3])
 ranker.streamSongs([3, 3, 3, 1, 2, 1, 3])
 ranker.getTopK() => [3, 1]
 ranker.streamSongs([2, 2, 2, 2, 2])
 ranker.getTopK() => [2, 3]

 You must solve this problem by effectively using the properties of a Priority Queue or Heap.

 You must also provide an explanation of the running time of both getTopK and streamSongs

Code Author: <Your Name Here>

Running Time Analysis of get_top_k
--------------------
<Your analysis here>

Running Time Analysis of stream_songs
--------------------
<Your analysis here>
'''


class AlgoFy:
    def __init__(self, k):
        self.k = k

    def stream_songs(self, songIds):
       pass

    def get_top_k(self):
        return []


"""
DO NOT EDIT BELOW THIS
Below is the unit testing suite for this file.
It provides all the tests that your code must pass to get full credit.
"""


class TestAlgoFy:
    def run_unit_tests(self):
        self.test_example()
        self.test_example_2()
        self.test_many_batches()
        self.test_fewer_than_k()
        self.test_empty()

    def print_test_result(self, test_name, result):
        color = "\033[92m" if result else "\033[91m"
        reset = "\033[0m"
        print(f"{color}[{result}] {test_name}{reset}")

    def test_answer(self, test_name, result, expected):
        if result == expected:
            self.print_test_result(test_name, True)
        else:
            self.print_test_result(test_name, False)
            print(f"Expected: {expected} \nGot:      {result}")

    def test_example(self):
        ranker = AlgoFy(2)
        ranker.stream_songs([1, 1, 2, 2, 3])
        ranker.stream_songs([3, 3, 3, 1, 2, 1, 3])
        result = ranker.get_top_k()
        expected_answer = [3, 1]

        self.test_answer("test_example", result, expected_answer)

    def test_example_2(self):
        ranker = AlgoFy(2)
        ranker.stream_songs([1, 1, 2, 2, 3])
        ranker.stream_songs([3, 3, 3, 1, 2, 1, 3])
        ranker.get_top_k()
        ranker.stream_songs([2, 2, 2, 2, 2])

        result = ranker.get_top_k()
        expected_answer = [2, 3]

        self.test_answer("test_example_2", result, expected_answer)

    def test_many_batches(self):
        ranker = AlgoFy(5)

        for i in range(1, 10):
            for j in range(1, 15):
                ranker.stream_songs([i, j])
            ranker.get_top_k()
        ranker.stream_songs([3, 1, 1, 1, 2, 3])
        ranker.stream_songs([5, 4, 4, 3, 2, 2, 2, 1, 1])
        result = ranker.get_top_k()
        expected_answer = [1, 2, 3, 4, 5]

        self.test_answer("test_many_batches", result, expected_answer)

    def test_fewer_than_k(self):
        ranker = AlgoFy(4)

        ranker.stream_songs([1, 2, 3, 1, 2, 3, 1, 2, 1])
        result = ranker.get_top_k()
        expected_answer = [1, 2, 3]

        self.test_answer("test_fewer_than_k", result, expected_answer)

    def test_empty(self):
        ranker = AlgoFy(3)

        result = ranker.get_top_k()
        expected_answer = []

        self.test_answer("test_empty", result, expected_answer)


if __name__ == '__main__':
    test_runner = TestAlgoFy()
    test_runner.run_unit_tests()