class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        todo = Counter(tasks)
        units = 0         
        n += 1 
        while todo:
            # Pick the n items with highest count
            ready = todo.most_common(n)
            n_ready = len(ready)
            units += n_ready
            for k, _ in ready:
                if todo[k] > 1:
                    todo[k] -= 1
                else:
                    del todo[k]     # Would go to 0; delete
            if todo:
                # Fill in with idle time as needed
                units += n - n_ready
        return units