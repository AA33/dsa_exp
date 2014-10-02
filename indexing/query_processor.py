__author__ = 'abhishekanurag'

import sys
from indexing.name_trie import NameTrieNode
from multiprocessing import Pool
import itertools
from heapq import heappush, heappushpop, heappop, heapify

'''
Runnable wrapper for managing queries to the trie index.
 - Starts multiple processes to asynchronously search the main trie and all it's _ rooted children
 - Manages them in a process Pool and then merges results that each subprocess got.
'''
class QueryProcessor:
    def __init__(self, name_trie):
        self.name_trie = name_trie

    def process(self, s):
        search_tries = list(self.name_trie.underscore_children)
        search_tries.append(self.name_trie)
        pool = Pool()
        best_heaps = pool.map(get_best_from_trie_parallel, itertools.izip(search_tries, itertools.repeat(s)))
        pool.close()
        pool.join()
        return QueryProcessor._merge(best_heaps, self.name_trie.MAX_RESULT_SIZE)

    @staticmethod
    def _add_to_merged(merged_best, merged_best_set, best, max_size):
        if len(best) > 0:
            score, name = heappop(best)
            score *= -1
            if len(merged_best) < max_size:
                if (score, name) not in merged_best_set:
                    merged_best_set.add((score, name))
                    heappush(merged_best, (score, name))
            else:
                if (score, name) not in merged_best_set:
                    merged_best_set.add((score, name))
                    merged_best_set.remove(heappushpop(merged_best, (score, name)))


    @staticmethod
    def _merge(best_min_heaps, max_size):
        best_max_heaps = []
        for best in best_min_heaps:
            best_max = list()
            for tuple in best:
                max_tuple = (tuple[0] * -1, tuple[1])
                best_max.append(max_tuple)
            heapify(best_max)
            best_max_heaps.append(best_max)
        merged_best = []
        merged_best_set = set()
        # Take top from all and form a min heap of upto max_size
        for best in best_max_heaps:
            QueryProcessor._add_to_merged(merged_best, merged_best_set, best, max_size)

        # keep merging till some heap has a better result than the merged heap
        has_better = True
        while has_better:
            has_better = False
            for best in best_max_heaps:
                if len(best) > 0:
                    max = best[0]
                    if -1 * max[0] > merged_best[0][0] or len(merged_best) < max_size:
                        has_better = True
                        QueryProcessor._add_to_merged(merged_best, merged_best_set, best, max_size)

        return list(reversed(sorted(merged_best)))


def get_best_from_trie_parallel(trie_prefix):
    trie, prefix = trie_prefix
    return trie.get_best_children(prefix)


# Main
def main():
    print 'Hello! Ready for indexing. There are some sample files in this folder if you would like : names.csv and names2.csv'
    input_file = raw_input("Enter the name of the csv file with the <name,score> data:")
    trie = NameTrieNode.construct(input_file)
    qp = QueryProcessor(trie)
    while 1:
        search = raw_input("Enter search term:(Enter to exit)")
        if search=='':
            break
        print qp.process(search)
    print 'Done!'

if __name__ == "__main__":
    sys.exit(main())