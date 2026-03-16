"""
arr
[
    0: [[snap_id, latest_val_in_snap_id]]
    1: []
    2: []
]
"""

class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[[0, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        if (not self.arr[index]) or (self.arr[index][-1][0] != self.snap_id):
            self.arr[index].append([self.snap_id, val])
        else:
            self.arr[index][-1][1] = val

    def snap(self) -> int:
        to_ret = self.snap_id
        self.snap_id += 1
        return to_ret

    def get(self, index: int, snap_id: int) -> int:
        temp = self.arr[index]

        l, r = 0, len(temp)-1
        res = None
        while l <= r:
            mid = (l + r) // 2
            if temp[mid][0] <= snap_id:
                res = mid
                l = mid + 1
            else:
                r = mid - 1

        return temp[res][1]