__author__ = 'abhishekanurag'

'''
Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.

--------------------
Two ways to do this:
- Form a graph of the whole dictionary such that every vertex is a word and there are edges between words that can
  be transformed into each other in 1 step.
  Run Dijkstra from start word to end word and that's the answer.
  Useful if this has to be done many times for different words but belonging to the same dictionary.
  Runtime: O(V^2) for making the graph. O((V+E)logV) for Dijkstra.

'''
