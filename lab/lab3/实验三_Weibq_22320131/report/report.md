<font size = 4> <center>中山大学计算机学院 </font>
<font size = 4> 人工智能
本科生实验报告 </font>

<font size = 4> 课程名称：Artificial Intelligence </font>


</center>


<font size = 3><center>学号：22320131
姓名：韦百强 </center> </font>


# 一、 实验题目
**使用α-β剪枝算法实现自己的象棋AI**
# 二、 实验内容
## 1. 实验原理
`AI`的实现算法为α-β剪枝算法（无启发），算法的基本原理（伪代码）如下：
```python
int AlphaBeta(int Alpha , int Beta , int turn)
{
    if(turn==0)
        return Eveluation;
    if(Is Min Node){
        for(each possible move m){
            make move m;
            score=AlphaBeta(Alpha,Beta,turn-1);
            unmake move m;
            if(score < Beta){
                Beta=score;
                if(Alpha>=Beta)
                    return Alpha;
            }
        }
        return Beta;
    }
    else{
        for(each possible move m){
            make move m;
            score=AlphaBeta(Alpha,Beta,turn-1);
            unmake move m;
            if(score>Alpha){
                Alpha=score;
                if(Alpha>=Beta)
                    return Beta;
            }
        }
        return Alpha;
    }
}
```

## 2. 实现过程
>1. 分析给定的各个类及其成员的目的，明确要修改的部分是MyAI的ChessAI类；由于与ChessAI的类名冲突，我将其改名为ChessAI_MY
```python
class ChessAI_MY(object):
    # ......
```
>2. 用alpha_beta剪枝算法实现ai
```python
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

                    
                    if new_chess is None:
                        continue
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

```

>3. 修改主函数，使得ai对弈两场，并统计积分
round_1
```python
def round_1(SCORE):
    SCORE = 0
    # 初始化pygame
    pygame.init()
    # 创建用来显示画面的对象（理解为相框）
    screen = pygame.display.set_mode((750, 667))
    # 游戏背景图片
    background_img = pygame.image.load("./images/bg.jpg")
    # 游戏棋盘
    # chessboard_img = pygame.image.load("images/bg.png")
    # 创建棋盘对象
    chessboard = ChessBoard(screen)
    # 创建计时器
    clock = pygame.time.Clock()
    # 创建游戏对象（像当前走棋方、游戏是否结束等都封装到这个对象中）
    game = Game(screen, chessboard)
    game.back_button.add_history(chessboard.get_chessboard_str_map())
    # 创建AI对象
    # # 第一局我的AI先手，为红方
    ai_r = ChessAI_MY(game.user_team)
    ai_b = ChessAI(game.computer_team)
    # 主循环
    while True:
        # AI行动
        if not game.show_win and not game.show_draw and game.AI_mode and game.get_player() == ai_b.team:
            if game.back_button.is_repeated():
                print("获胜...")
                return SCORE
                game.set_win(game.get_player())
            else:
                # AI预测下一步
                cur_row, cur_col, nxt_row, nxt_col = ai_b.get_next_step(chessboard)
                # 选择棋子
                ClickBox(screen, cur_row, cur_col)
                # 下棋子
                chessboard.move_chess(nxt_row, nxt_col)
                # 清理「点击对象」
                ClickBox.clean()
                # 检测落子后，是否产生了"将军"功能
                if chessboard.judge_attack_general(game.get_player()):
                    print("将军....")
                    # 检测对方是否可以挽救棋局，如果能挽救，就显示"将军"，否则显示"胜利"
                    if chessboard.judge_win(game.get_player()):
                        print("获胜...")
                        return SCORE
                        game.set_win(game.get_player())
                    else:
                        # 如果攻击到对方，则标记显示"将军"效果
                        game.set_attack(True)
                else:
                    if chessboard.judge_win(game.get_player()):
                        print("获胜...")
                        return SCORE
                        game.set_win(game.get_player())
                    game.set_attack(False)    
                
                if chessboard.judge_draw():
                    print("和棋...")
                    SCORE += 1
                    return SCORE
                    game.set_draw()

                # 落子之后，交换走棋方
                game.back_button.add_history(chessboard.get_chessboard_str_map())
                game.exchange()
        else:
            if game.back_button.is_repeated():
                print("获胜...")
                SCORE += 3
                return SCORE
                game.set_win(game.get_player())
            else:
                # AI预测下一步
                cur_row, cur_col, nxt_row, nxt_col = ai_r.get_next_step(chessboard)
                # 选择棋子
                ClickBox(screen, cur_row, cur_col)
                # 下棋子
                chessboard.move_chess(nxt_row, nxt_col)
                # 清理「点击对象」
                ClickBox.clean()
                # 检测落子后，是否产生了"将军"功能
                if chessboard.judge_attack_general(game.get_player()):
                    print("将军....")
                    # 检测对方是否可以挽救棋局，如果能挽救，就显示"将军"，否则显示"胜利"
                    if chessboard.judge_win(game.get_player()):   
                        print("获胜...")
                        SCORE += 3
                        return SCORE
                        game.set_win(game.get_player())
                    else:
                        # 如果攻击到对方，则标记显示"将军"效果
                        game.set_attack(True)
                else:
                    if chessboard.judge_win(game.get_player()):
                        print("获胜...")
                        SCORE += 3
                        return
                        game.set_win(game.get_player())
                    game.set_attack(False)    
                
                if chessboard.judge_draw():
                    print("和棋...")
                    SCORE += 1
                    return SCORE
                    game.set_draw()

                # 落子之后，交换走棋方
                game.back_button.add_history(chessboard.get_chessboard_str_map())
                game.exchange()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # 显示游戏背景
        screen.blit(background_img, (0, 0))
        screen.blit(background_img, (0, 270))
        screen.blit(background_img, (0, 540))

        # # 显示棋盘
        # # screen.blit(chessboard_img, (50, 50))
        # chessboard.show()
        #
        # # 显示棋盘上的所有棋子
        # # for line_chess in chessboard_map:
        # for line_chess in chessboard.chessboard_map:
        #     for chess in line_chess:
        #         if chess:
        #             # screen.blit(chess[0], chess[1])
        #             chess.show()

        # 显示棋盘以及棋子
        chessboard.show_chessboard_and_chess()

        # 标记点击的棋子
        ClickBox.show()

        # 显示可以落子的位置图片
        Dot.show_all()

        # 显示游戏相关信息
        game.show()

        # 显示screen这个相框的内容（此时在这个相框中的内容像照片、文字等会显示出来）
        pygame.display.update()

        # FPS（每秒钟显示画面的次数）
        clock.tick(60)  # 通过一定的延时，实现1秒钟能够循环60次
```
round_2
```python
def round_2():
    # ......
```
>4. 统计结果，分数

## 3. 创新点
>1. 根据MyAI的定义，直接运行会出现`TypeError: judge_j_attack() argument after * must be an iterable, not NoneType`的错误，需要对Chessboard.py的代码进行修改，如下：
```python
def judge_attack_general(self, attack_player):
        """
        判断 attact_player方是否 将对方的军
        """
        # 1. 找到对方"将"的位置
        general_player = "r" if attack_player == "b" else "b"
        general_position = self.get_general_position(general_player)
        
        # 检查 general_position 是否为 None (此处为添加部分)
        if general_position is None:
            return False

        # 2. 遍历我方所有的棋子
```

>2. 同样的None带来的问题还会再move_chess中出现，只需要对Chessboard的move_chess函数修改即可，如下：
```python
  # 移动位置
        self.chessboard_map[new_row][new_col] = self.chessboard_map[old_row][old_col]
        # 修改棋子的属性 (if 语句为新增的)
        if self.chessboard_map[new_row][new_col] is not None:
        # 修改棋子的属性
            self.chessboard_map[new_row][new_col].update_position(new_row, new_col)
        # 清楚之前位置为None
        self.chessboard_map[old_row][old_col] = None

```

>3. 通过助教提供的资料，实现拖动窗口不会导致崩溃：
```python
for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
```


# 三、	实验结果及分析

>1. 程序运行成功，短视频在./img下
<img src = ".\img\image copy.png">

>2. 如果胜场为2，那么分数为6
<img src = ".\img\image copy 2.png">

*ps:应该是存在bug，很多次尝试都是我的劣质ai赢，提前写好的ai在后手很厉害，在先手很菜*
## 创新点
因为None类型的特殊性，我考虑尽量再各个函数中对None进行边界条件限制，于是我尝试在MyAI的ChessAI_MY类的alpha_beta()方法中添加：
```python
if new_chess is None:
    continue
```
以期望当遇到None位置时，继续循环。但是出现bug，如下图所示
<img src = ".\img\image.png">
车不见了，而且我也找不出问题所在；我猜想
>1. 图片资源不显示，但是车还在那，因为程序正常运行；
>2. 少了一个棋子，但是不影响程序运行。

所以这段代码就不加了，最后也没有出现`太多`问题
# 四、 参考资料

1. Python3+pygame中国象棋 代码完整 非常好 有效果演示https://blog.csdn.net/qq_60168783/article/details/121407285
2. python实现中国象棋https://blog.csdn.net/kekechengxiao/article/details/135227827?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-135227827-blog-121407285.235%5Ev43%5Epc_blog_bottom_relevance_base6&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-135227827-blog-121407285.235%5Ev43%5Epc_blog_bottom_relevance_base6&utm_relevant_index=5
3. 黑白棋的α-β剪枝算法https://github.com/dougefla/Reversi_MCTS
4. 黑白棋的极大极小搜索算法https://github.com/monikerzju/zju-ai-reversi
5. 最清晰易懂的MinMax算法和Alpha-Beta剪枝详解https://blog.csdn.net/weixin_42165981/article/details/103263211
6. 案例参考https://github.com/cxw745/AI_SYSU_2023/tree/main/lab4%20AIChess_alphabeta
7. 人工智能实验课III-附录1：关于双AI对弈窗口未响应问题https://mp.weixin.qq.com/s/z8S8WjZa0icizRh3cBFOKg
8. α-β剪枝算法https://github.com/Ivan-Von/AI_2022_SYSU
9. Alpha-Beta 剪枝算法https://blog.csdn.net/mungco/article/details/12317547#:~:text=Alpha-Beta%E5%89%AA%E6%9E%9D%E7%AE%97%E6%B3%95%E7%9A%84%E4%BC%AA%E4%BB%A3%E7%A0%81%E5%A6%82%E4%B8%8B%EF%BC%9A%20int%20AlphaBeta%28int%20Alpha%2C,int%20Beta%2C%20int%20turn%29