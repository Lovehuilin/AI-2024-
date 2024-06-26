import copy
from ChessBoard import *


class Evaluate(object):
    # 棋子棋力得分
    single_chess_point = {
        'c': 989,  # 车
        'm': 439,  # 马
        'p': 442,  # 炮
        's': 226,  # 士
        'x': 210,  # 象
        'z': 55,  # 卒
        'j': 65536  # 将
    }
    # 红兵（卒）位置得分
    red_bin_pos_point = [
        [1, 3, 9, 10, 12, 10, 9, 3, 1],
        [18, 36, 56, 95, 118, 95, 56, 36, 18],
        [15, 28, 42, 73, 80, 73, 42, 28, 15],
        [13, 22, 30, 42, 52, 42, 30, 22, 13],
        [8, 17, 18, 21, 26, 21, 18, 17, 8],
        [3, 0, 7, 0, 8, 0, 7, 0, 3],
        [-1, 0, -3, 0, 3, 0, -3, 0, -1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    # 红车位置得分
    red_che_pos_point = [
        [185, 195, 190, 210, 220, 210, 190, 195, 185],
        [185, 203, 198, 230, 245, 230, 198, 203, 185],
        [180, 198, 190, 215, 225, 215, 190, 198, 180],
        [180, 200, 195, 220, 230, 220, 195, 200, 180],
        [180, 190, 180, 205, 225, 205, 180, 190, 180],
        [155, 185, 172, 215, 215, 215, 172, 185, 155],
        [110, 148, 135, 185, 190, 185, 135, 148, 110],
        [100, 115, 105, 140, 135, 140, 105, 115, 110],
        [115, 95, 100, 155, 115, 155, 100, 95, 115],
        [20, 120, 105, 140, 115, 150, 105, 120, 20]
    ]
    # 红马位置得分
    red_ma_pos_point = [
        [80, 105, 135, 120, 80, 120, 135, 105, 80],
        [80, 115, 200, 135, 105, 135, 200, 115, 80],
        [120, 125, 135, 150, 145, 150, 135, 125, 120],
        [105, 175, 145, 175, 150, 175, 145, 175, 105],
        [90, 135, 125, 145, 135, 145, 125, 135, 90],
        [80, 120, 135, 125, 120, 125, 135, 120, 80],
        [45, 90, 105, 190, 110, 90, 105, 90, 45],
        [80, 45, 105, 105, 80, 105, 105, 45, 80],
        [20, 45, 80, 80, -10, 80, 80, 45, 20],
        [20, -20, 20, 20, 20, 20, 20, -20, 20]
    ]
    # 红炮位置得分
    red_pao_pos_point = [
        [190, 180, 190, 70, 10, 70, 190, 180, 190],
        [70, 120, 100, 90, 150, 90, 100, 120, 70],
        [70, 90, 80, 90, 200, 90, 80, 90, 70],
        [60, 80, 60, 50, 210, 50, 60, 80, 60],
        [90, 50, 90, 70, 220, 70, 90, 50, 90],
        [120, 70, 100, 60, 230, 60, 100, 70, 120],
        [10, 30, 10, 30, 120, 30, 10, 30, 10],
        [30, -20, 30, 20, 200, 20, 30, -20, 30],
        [30, 10, 30, 30, -10, 30, 30, 10, 30],
        [20, 20, 20, 20, -10, 20, 20, 20, 20]
    ]
    # 红将位置得分
    red_jiang_pos_point = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9750, 9800, 9750, 0, 0, 0],
        [0, 0, 0, 9900, 9900, 9900, 0, 0, 0],
        [0, 0, 0, 10000, 10000, 10000, 0, 0, 0],
    ]
    # 红相或士位置得分
    red_xiang_shi_pos_point = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 60, 0, 0, 0, 60, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [80, 0, 0, 80, 90, 80, 0, 0, 80],
        [0, 0, 0, 0, 0, 120, 0, 0, 0],
        [0, 0, 70, 100, 0, 100, 70, 0, 0],
    ]

    red_pos_point = {
        'z': red_bin_pos_point,
        'm': red_ma_pos_point,
        'c': red_che_pos_point,
        'j': red_jiang_pos_point,
        'p': red_pao_pos_point,
        'x': red_xiang_shi_pos_point,
        's': red_xiang_shi_pos_point
    }

    def __init__(self, team):
        self.team = team

    def get_single_chess_point(self, chess: Chess):
        if chess.team == self.team:
            return self.single_chess_point[chess.name]
        else:
            return -1 * self.single_chess_point[chess.name]

    def get_chess_pos_point(self, chess: Chess):
        red_pos_point_table = self.red_pos_point[chess.name]
        if chess.team == 'r':
            pos_point = red_pos_point_table[chess.row][chess.col]
        else:
            pos_point = red_pos_point_table[9 - chess.row][chess.col]
        if chess.team != self.team:
            pos_point *= -1
        return pos_point

    def evaluate(self, chessboard: ChessBoard):
        point = 0
        for chess in chessboard.get_chess():
            point += self.get_single_chess_point(chess)
            point += self.get_chess_pos_point(chess)
        return point


class ChessMap(object):
    def __init__(self, chessboard: ChessBoard):
        self.chess_map = copy.deepcopy(chessboard.chessboard_map)


class ChessAI_MY(object):
    def __init__(self, computer_team):
        '''
        args:
            team: str, 颜色，'r' 或 'b'
            max_depth: int, 最大搜索深度
            old_pos: list, 要操作棋子的横纵坐标
            new_pos: list, 落子的横纵坐标
            evaluate_class: Evaluate, 评估函数
            node_num: int, 拓展结点数
        '''
        self.team = computer_team # 电脑方
        self.max_depth = 3 # 最大搜索深度
        self.old_pos = [0, 0] # 要操作棋子的横纵坐标
        self.new_pos = [0, 0] # 落子的横纵坐标
        self.evaluate_class = Evaluate(self.team) # 评估函数
        self.node_num = 0 # 拓展结点数

    def get_next_step(self, chessboard):
        '''
        该函数应当返回四个值:
            1 要操作棋子的横坐标
            2 要操作棋子的纵坐标
            3 落子的横坐标
            4 落子的纵坐标
        '''
        self.alpha_beta(0, -float('inf'), float('inf'), chessboard, self.team)
        # -----输出拓展结点数
        print('node number %d' % self.node_num)
        self.node_num = 0  # 清零
        # ----------------
        return self.old_pos + self.new_pos # 返回落子的横纵坐标

    @staticmethod
    def get_nxt_player(player):
        # 返回下一个玩家，即对方
        if player == 'r':
            return 'b'
        else:
            return 'r'

    @staticmethod
    def get_tmp_chessboard(chessboard, player_chess, new_row, new_col) -> ChessBoard:
        # 返回一个新的棋盘，用于模拟走棋
        tmp_chessboard = copy.deepcopy(chessboard) # 深拷贝
        tmp_chess = tmp_chessboard.chessboard_map[player_chess.row][player_chess.col]
        tmp_chess.row, tmp_chess.col = new_row, new_col # 更新棋子位置
        tmp_chessboard.chessboard_map[new_row][new_col] = tmp_chess # 更新棋盘
        tmp_chessboard.chessboard_map[player_chess.row][player_chess.col] = None
        return tmp_chessboard # 返回新的棋盘

    def alpha_beta(self, depth, alpha, beta, chessboard, team):
        # 递归搜索, alpha-beta 剪枝
        self.node_num += 1 # 拓展结点数加一
        # 如果已经达到预设的最大搜索深度，则返回当前状态的估值
        if depth >= self.max_depth or chessboard.get_general_position(
                self.get_nxt_player(team)) is None or chessboard.judge_win(self.get_nxt_player(team)):
            return self.evaluate_class.evaluate(chessboard) # 返回当前状态的估值

        # 获得所有棋子，对每个棋子能走的每个位置进行价值评估，通过剪枝选择价值最高的走法
        # 注意：这里只考虑在当前队伍下能走的棋子，以及当前队伍的颜色
        chesses = chessboard.get_chess()  # 获得当前棋盘所有的棋子
        for chess in chesses:  # 遍历所有棋子
            if team == self.team and chess.team == self.team:  # 只考虑当前队伍下的棋子
                all_position = chessboard.get_put_down_position(chess)  # 获得当前棋子可以走的所有位置
                for new_row, new_col in all_position:
                    cur_row, cur_col = chess.row, chess.col  # 存储当前棋子的位置
                    new_chess = chessboard.chessboard_map[new_row][new_col]  # 存储当期棋子的状态

                    
                    # if new_chess is None:
                    #     continue
                    # 将棋子移动到新位置，并递归计算估值
                    # 注意：这里用 DFS 的方式实现搜索，所以在递归完成后需要恢复棋盘状态
                    chessboard.chessboard_map[new_row][new_col] = chessboard.chessboard_map[cur_row][cur_col] # 更新棋盘
                    chessboard.chessboard_map[new_row][new_col].update_position(new_row, new_col) # 更新棋子位置
                    chessboard.chessboard_map[cur_row][cur_col] = None # 更新当前位置为空
                    value = self.alpha_beta(depth + 1, alpha, beta, chessboard, self.get_nxt_player(team)) # 递归计算估值
                    chessboard.chessboard_map[cur_row][cur_col] = chessboard.chessboard_map[new_row][new_col] #     恢复棋盘状态
                    chessboard.chessboard_map[cur_row][cur_col].update_position(cur_row, cur_col)
                    chessboard.chessboard_map[new_row][new_col] = new_chess # 恢复当前位置的状态
                    # 更新 alpha 值，并记录最优走法
                    if depth == 0 and value > alpha or not self.old_pos:  # 第一层,进行决策,选尽可能大的alpha
                        self.old_pos = [cur_row, cur_col]
                        self.new_pos = [new_row, new_col]
                    alpha = max(alpha, value)  # 取最大的值作为alpha

                    # 根据当前 alpha 和 beta 的值进行剪枝
                    if alpha >= beta:
                        return alpha # 剪枝

            else:  # 如果不是当前队伍下的棋子，则继续搜索
                all_position = chessboard.get_put_down_position(chess)  # 获得当前棋子可以走的所有位置
                for new_row, new_col in all_position:
                    cur_row, cur_col = chess.row, chess.col  # 存储当前棋子的位置
                    new_chess = chessboard.chessboard_map[new_row][new_col]

                    # 将棋子移动到新位置，并递归计算估值
                    # 注意：这里用 DFS 的方式实现搜索，所以在递归完成后需要恢复棋盘状态
                    chessboard.chessboard_map[new_row][new_col] = chessboard.chessboard_map[cur_row][cur_col] # 更新棋盘
                    chessboard.chessboard_map[new_row][new_col].update_position(new_row, new_col) # 更新棋子位置
                    chessboard.chessboard_map[cur_row][cur_col] = None # 更新当前位置为空
                    value = self.alpha_beta(depth + 1, alpha, beta, chessboard, self.get_nxt_player(team)) # 递归计算估值
                    chessboard.chessboard_map[cur_row][cur_col] = chessboard.chessboard_map[new_row][new_col] #    恢复棋盘状态
                    chessboard.chessboard_map[cur_row][cur_col].update_position(cur_row, cur_col)
                    chessboard.chessboard_map[new_row][new_col] = new_chess # 恢复当前位置的状态
                    # 更新 beta 值，并进行剪枝
                    beta = min(beta, value)  # 取最小的值作为beta
                    if beta <= alpha:
                        return beta # 剪枝

        # 返回最终的估值
        if team == self.team:
            return alpha
        else:
            return beta # 返回最小值
