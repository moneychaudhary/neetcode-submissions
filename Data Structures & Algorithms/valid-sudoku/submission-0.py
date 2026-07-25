class Solution:

    def isDuplicate(self, values: List[str]):
        seen = set()
        print(values)
        for num in values:
            if num != "." and num in seen:
                print("True")
                return True
            seen.add(num)
        print("False")
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = defaultdict(list)
        boxes = defaultdict(list)

        for i, row in enumerate(board):
            if self.isDuplicate(row):
                return False

            for j in range(9):
                columns[j].append(row[j])

            b = (i // 3) * 3
            boxes[b].extend(row[0:3])
            boxes[b + 1].extend(row[3:6])
            boxes[b + 2].extend(row[6:9])

        print("Col")
        for col in columns.values(): 
            if self.isDuplicate(col):
                return False

        print("Box")
        for box in boxes.values():
            if self.isDuplicate(box):
                return False
        return True
        



        