from nearest_neighbors import NearestNeighbors

__author__ = 'abhishekanurag'

from location import Location


class TwoDTree:
    def __init__(self, locations, xy=None, randomize=True):
        self.size = len(locations)
        if xy is not None:
            self.xy = xy
        else:
            self.xy = True
        start = 0
        end = self.size - 1
        if self.size % 2 == 0:
            median = self.size / 2 - 1
        else:
            median = self.size / 2
        if start < end:
            self.loc = Location.partition_around_median(locations, self.xy, randomize)
            if start < median:
                self.left = TwoDTree(locations[:median], not self.xy, randomize)
            else:
                self.left = None
            if median < end:
                self.right = TwoDTree(locations[median + 1:], not self.xy, randomize)
            else:
                self.right = None
        elif start == end:
            self.loc = locations[start]
            self.left = self.right = None
        else:
            self.loc = self.left = self.right = None

    def __str__(self):
        return self._to_string('')

    def _to_string(self, prefix):
        if self.xy:
            axis = 'X'
        else:
            axis = 'Y'
        left_str = right_str = ''
        if self.loc:
            self_str = prefix + '{' + str(self.loc) + '(' + str(self.loc.lid) + ')' + '}' + str(self.size)
        else:
            self_str = '{}0'

        if self.left and self.right:
            left_str = '\n|\n' + self.left._to_string(prefix + '---L ' + axis)
            right_str = '\n|\n' + self.right._to_string(prefix + '---R ' + axis)
        elif self.left:
            left_str = '\n|\n' + self.left._to_string(prefix + '---L ' + axis)
        elif self.right:
            right_str = '\n|\n' + self.right._to_string(prefix + '---R ' + axis)

        return self_str + left_str + right_str


    def k_nearest_neighbors(self, search, k, ignore=None):
        if self.size < k:
            search_size = self.size
        else:
            search_size = k
        if ignore:
            nn = NearestNeighbors(search_size,set(ignore))
        else:
            nn = NearestNeighbors(search_size)
        self._knn(nn, search)
        return nn.get_list()

    def _knn(self, nn, search):
        nn.add(self.loc.get_topic(search))

        left_or_right = False  # False = right
        x_axis_and_less = self.xy and search.x <= self.loc.x
        y_axis_and_less = not self.xy and search.y <= self.loc.y
        if x_axis_and_less or y_axis_and_less:
            left_or_right = True  # True = left

        self._get_k_best_from(left_or_right, search, nn)

        if not nn.is_full():
            self._get_k_best_from(not left_or_right, search, nn)
        else:
            current_worst = nn.peek()
            if current_worst:
                x_diff = y_diff = 0
                if self.xy:
                    x_diff = search.x - self.loc.x
                    x_diff = x_diff * x_diff
                else:
                    y_diff = search.y - self.loc.y
                    y_diff = y_diff * y_diff
                worst_dist = current_worst.distance

                x_axis_and_better_dist = self.xy and x_diff <= worst_dist
                y_axis_and_better_dist = not self.xy and y_diff <= worst_dist

                if x_axis_and_better_dist or y_axis_and_better_dist:
                    self._get_k_best_from(not left_or_right, search, nn)

    def _get_k_best_from(self, left_or_right, search, nn):
        if left_or_right and self.left:
            self.left._knn(nn, search)
        elif not left_or_right and self.right:
            self.right._knn(nn, search)




