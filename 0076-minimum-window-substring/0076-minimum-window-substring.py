class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = Counter(t)
        # create a counter for keeping track of chars in w
        w = Counter()
        # keep track of shortest answer found so far
        r = ''
        # keep track of which characters we have in the current window
        window = deque()
        for ch in s:
            # add current character to window
            window.append(ch)
            # increment count in window
            w[ch] += 1
            # check if predicate is satisifed (window contains all chars in t)
            if all(w[c] >= t_counts[c] for c in t_counts.keys()):
                # remove unnecessary (superfluous) chars
                while window and w[window[0]] > t_counts[window[0]]:
                    w[window.popleft()] -= 1
                # record this new answer only if it is shorter than a previous answer
                # (or if no previous answer exists)
                if r == '' or len(window) < len(r):
                    r = ''.join(window)
                # remove the last added char so we can keep looking for more substrings
                if window:
                    w[window.popleft()] -= 1
           
        return r