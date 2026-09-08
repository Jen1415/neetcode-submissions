class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        from collections import Counter
        columns = [[] for _ in range(9)]
        sub_boxes = [[] for _ in range(9)]
        box = 0
        row_count = 0
        
        # check rows
        for row in board:
            
            if row_count >= 3 and row_count < 6:
                box = 3
            if row_count >= 6:
                box = 6

            # append columns and sub_boxes
            for i in range(9):
                columns[i].append(row[i])

                if i < 3:
                    # box 0 3 6
                    sub_boxes[box].append(row[i])

                if i >= 3 and i < 6:
                    #  box 1 4 7
                    sub_boxes[box + 1].append(row[i])

                if i >= 6:
                    # box 2 5 8
                    sub_boxes[box + 2].append(row[i])

            if self.isDuplicate(row): return False
            row_count += 1

        # check columns
        for column in columns:
            if self.isDuplicate(column): return False

        # check subboxes
        for sub_box in sub_boxes:
            if self.isDuplicate(sub_box): return False

        return True

    def isDuplicate(self, elements):
        table = dict(Counter(element for element in elements if element != '.'))
        for key, value in table.items():
            if value > 1: return True
