#三维数组创立
def Estabilsh_candidates():
    candidates = [[[1 for i in range(9)] for i in range(9)] for i in range(9)]
    return candidates

# 将candidate转化为每个单元格的可能数字列表并返回
def change(candidates):
    result = [[[]for i in range(9)]for i in range(9)]
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if candidates[i][j][k] == 1:
                    result[i][j].append(k + 1)
    return result

#从已有数字出发
def lastRemainingCellInference(board):
    #创建一个三维数组存储每个位置的候选值，初始值全部赋为1-9
    candidates = Estabilsh_candidates()
    #处理已经填入的数字：
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                val = board[i][j] - 1 #将其转为索引
                for k in range(9):
                    candidates[i][j][k] = 1 if k == val else 0
                for p in range(9):
                    #处理同行
                    candidates[i][p][val] = 0 if p != j else candidates[i][p][val]
                    #处理同列
                    candidates[p][j][val] = 0 if p != i else candidates[p][j][val]
                    #处理同宫格
                    box_i , box_j = 3 * (i // 3), 3 * (j // 3)
                    for r in range(box_i , box_i + 3):
                        for c in range(box_j, box_j + 3):
                            if not (r == i and c == j):
                                candidates[r][c][val] = 0
    #将candidate转化为每个单元格的可能数字列表并返回
    result = change(candidates)
    return result

#从空格出发
def possibleNumberInference(board):
    # 创建一个三维数组存储每个位置的候选值，初始值全部赋为1-9
    candidates = Estabilsh_candidates()
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for p in range(9):
                    #处理同行
                    if board[i][p] != 0:
                        candidates[i][j][board[i][p] - 1] = 0
                    #处理同列
                    if board[p][j] != 0:
                        candidates[i][j][board[p][j] - 1] = 0
                #处理同宫格
                box_i , box_j = 3 * (i //3), 3 * (j // 3)
                for r in range(box_i, box_i + 3):
                    for c in range(box_j, box_j + 3):
                        if board[r][c] != 0:
                            candidates[i][j][board[r][c] - 1] = 0
            else:
                #对于已有数字的单元格，只有一个候选值
                val = board[i][j] -1
                for k in range(9):
                    candidates[i][j][k] = 1 if k == val else 0
    # 将candidate转化为每个单元格的可能数字列表并返回
    result = change(candidates)
    return result

def format_sudoku(board):
    """格式化打印数独板"""
    result = ""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            result += "-" * 21 + "\n"
        for j in range(9):
            if j % 3 == 0 and j != 0:
                result += "| "
            value = str(board[i][j]) if board[i][j] != 0 else "."
            result += value + " "
        result += "\n"
    return result

def format_candidates(candidates):
    """格式化打印候选值，使结果更易读"""
    result = ""
    for i in range(9):
        for j in range(9):
            result += f"位置({i},{j}): {candidates[i][j]}\n"
            if j == 8 and i != 8:
                result += "-" * 30 + "\n"
    return result

def verify_inferences(method1, method2):
    """验证两种推理方法的结果是否一致"""
    consistent = True
    differences = []
    
    for i in range(9):
        for j in range(9):
            if sorted(method1[i][j]) != sorted(method2[i][j]):
                consistent = False
                differences.append((i, j, method1[i][j], method2[i][j]))
    
    return consistent, differences

def check_empty_cells(board, candidates):
    """检查是否有无解的单元格"""
    empty_cells = []
    
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0 and not candidates[i][j]:
                empty_cells.append((i, j))
    
    return empty_cells

def test():
    TEST_CASES = {
        "case_1":{
            "board":[
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]
            ]
        },
        "case_2_empty": {
            "board": [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
        },
        "case_3_full": {
            "board": [
                [5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9]
            ]
        },
        "case_4_easy": {
            "board": [
                [3, 0, 6, 5, 0, 8, 4, 0, 0],
                [5, 2, 0, 0, 0, 0, 0, 0, 0],
                [0, 8, 7, 0, 0, 0, 0, 3, 1],
                [0, 0, 3, 0, 1, 0, 0, 8, 0],
                [9, 0, 0, 8, 6, 3, 0, 0, 5],
                [0, 5, 0, 0, 9, 0, 6, 0, 0],
                [1, 3, 0, 0, 0, 0, 2, 5, 0],
                [0, 0, 0, 0, 0, 0, 0, 7, 4],
                [0, 0, 5, 2, 0, 6, 3, 0, 0]
            ]
        },
        "case_5_hard": {
            "board": [
                [0, 0, 0, 6, 0, 0, 4, 0, 0],
                [7, 0, 0, 0, 0, 3, 6, 0, 0],
                [0, 0, 0, 0, 9, 1, 0, 8, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 5, 0, 1, 8, 0, 0, 0, 3],
                [0, 0, 0, 3, 0, 6, 0, 4, 5],
                [0, 4, 0, 2, 0, 0, 0, 6, 0],
                [9, 0, 3, 0, 0, 0, 0, 0, 0],
                [0, 2, 0, 0, 0, 0, 1, 0, 0]
            ]
        }
    }
    
    for case_name, case_data in TEST_CASES.items():
        board = case_data["board"]
        print(f"\n===== 测试 {case_name} =====")
        print("原始数独（棋盘格式）：")
        print(format_sudoku(board))
        
        # 执行两种推理方法
        pn_inference = possibleNumberInference(board)
        lr_inference = lastRemainingCellInference(board)
        
        # 验证两种方法是否一致
        consistent, differences = verify_inferences(pn_inference, lr_inference)
        
        if consistent:
            print("\n✓ 两种推理方法结果一致")
        else:
            print("\n✗ 两种推理方法结果不一致！")
            for i, j, pn, lr in differences:
                print(f"  位置({i},{j}) 不一致:")
                print(f"    从空格推理: {pn}")
                print(f"    从已填数字推理: {lr}")
        
        # 检查无解单元格
        empty_cells = check_empty_cells(board, pn_inference)
        if empty_cells:
            print("\n! 发现无解单元格:")
            for i, j in empty_cells:
                print(f"  位置({i},{j})")
        
        # 保留原始输出格式
        print("\nPossible Number Inference:")
        print(pn_inference)
        print("\nRemaining Cell Inference:")
        print(lr_inference)

if __name__ == "__main__":
    test()
