# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].


def merge(self, intervals):
        intervals = sorted(intervals, key=lambda i: i.start)

        mergedIntervals = []  # Result list.
        for cur in intervals:
            if len(mergedIntervals) == 0:
                mergedIntervals.append(cur)
            else:
                prev = mergedIntervals[-1]
                if prev.end >= cur.start:  # Overlapped intervals.
                    prev.end = max(prev.end, cur.end)
                else:
                    mergedIntervals.append(cur)

        return mergedIntervals
