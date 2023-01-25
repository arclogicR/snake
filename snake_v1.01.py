import pygame
import time
import random


def screen_init(background_color, snake_color):
    pygame.display.set_caption('Snake')  # 显示窗口标题
    screen.fill(background_color)  # 定义背景色为黑色
    pygame.draw.rect(screen, snake_color, [74, 74, 452, 452], 1)  # 绘制游戏边框，矩形数组使用左上角坐标和长，宽定义
    screen.blit(textImage_score, position_score)  # 定义分数值位置
    screen.blit(textImage_bottom, position_bottom)  # 定义顶标位置
    screen.blit(textImage_top, position_top)  # 定义底标位置


def draw(x, y):  # 根据逻辑坐标画方块
    pygame.draw.rect(screen, color_green,
                     [75 + snake_width * (x - 1), 75 + snake_width * (y - 1), snake_width, snake_width], 0)


def clear(x, y):  # 根据逻辑坐标清除方块
    screen.fill((0, 0, 0), [75 + snake_width * (x - 1), 75 + snake_width * (y - 1), snake_width, snake_width])


def clear_pxl(x, y, width, height):  # 根据像素清除区域
    screen.fill(color_black, [x, y, width, height])


def snake_turn(direction):  # 根据方向转向
    snake[position_snake_head[0]][position_snake_head[1]] = direction  # 将snake矩阵蛇头位置赋值为当前方向
    position_snake_head[0] += vector[direction][0]  # 转向x轴操作
    position_snake_head[1] += vector[direction][1]  # 转向y轴操作
    if snake[position_snake_head[0]][position_snake_head[1]] == 0:  # 不碰到则将转向后的舌头位置赋值为当前方向
        snake[position_snake_head[0]][position_snake_head[1]] = direction
        return 0
    else:
        return 1


def snake_move(direction):  # 直行移动
    position_snake_head[0] += vector[direction][0]  # 直行x轴操作
    position_snake_head[1] += vector[direction][1]  # 直行y轴操作
    if snake[position_snake_head[0]][position_snake_head[1]] == 0:  # 不碰到则将转向后的舌头位置赋值为当前方向
        snake[position_snake_head[0]][position_snake_head[1]] = direction
        return 0
    else:
        return 1


def clear_tail():
    snake_direction_tail = snake[position_snake_tail[0]][position_snake_tail[1]]
    clear(position_snake_tail[0], position_snake_tail[1])
    snake[position_snake_tail[0]][position_snake_tail[1]] = 0
    position_snake_tail[0] += vector[snake_direction_tail][0]
    position_snake_tail[1] += vector[snake_direction_tail][1]


def score_update(scr):  # 更新分数
    textImage_score_value = text_font.render(scr, True, color_green)  # 定义分数值文字
    clear_pxl(650, 100, 100, 35)  # 清空
    screen.blit(textImage_score_value, (650, 100))  # 更新分数


interval = 0.06  # 蛇身移动间隔事件，越小越快
snake_width = 15  # 蛇身像素宽度
color_green = [0, 255, 0]  # 定义颜色列表
color_black = [0, 0, 0]  # 定义颜色列表
screen_width = 800  # 定义屏幕宽
screen_height = 600  # 定义屏幕高
position_score = [625, 70]  # 定义分数显示位置
position_bottom = [170, 540]  # 定义底部显示位置
position_top = [240, 30]  # 定义顶部显示位置
score = 0  # 定义分数值

pygame.init()  # 初始化pygame

screen = pygame.display.set_mode([screen_width, screen_height])  # 定义画板大小
text_font = pygame.font.Font("arial.ttf", 20)  # 定义字体
textImage_bottom = text_font.render("Developed By Arclogic", True, color_green)  # 定义底标文字
textImage_top = text_font.render("PRESS ↑↓←→", True, color_green)  # 定义顶标文字
textImage_score = text_font.render("Score", True, color_green)  # 定义分数文字
textImage_gameover = text_font.render('Game Over', True, color_green)  # 定义游戏结束文字
textImage_finalscore = text_font.render('Your Final Score', True, color_green)  # 定义最终分数文字

screen_init(color_black, color_green)  # 画板初始化

position_food = [16, 4]
position_snake_head_init_x = 16  # 定义蛇头初始x坐标（将452*452像素的方块分为30*30边长为15的小方格逻辑坐标）
position_snake_head_init_y = 11  # 首定义蛇头初始y坐标
position_snake_tail_init_x = 16  # 首定义蛇尾初始x坐标
position_snake_tail_init_y = 19  # 首定义蛇尾初始y坐标
position_snake_head = []  # 定义蛇头坐标列表
position_snake_tail = []  # 定义蛇尾坐标列表
position_snake_head.append(position_snake_head_init_x)  # 蛇头坐标赋值
position_snake_head.append(position_snake_head_init_y)  # 蛇头坐标赋值
position_snake_tail.append(position_snake_tail_init_x)  # 蛇尾坐标赋值
position_snake_tail.append(position_snake_tail_init_y)  # 蛇尾坐标赋值
vector_up = [0, -1]  # 定义方向向量
vector_down = [0, 1]  # 定义方向向量
vector_left = [-1, 0]  # 定义方向向量
vector_right = [1, 0]  # 定义方向向量
vector = [[]]  # 定义二位列表方向向量
vector.append(vector_up)  # 方向向量赋值
vector.append(vector_down)  # 方向向量赋值
vector.append(vector_left)  # 方向向量赋值
vector.append(vector_right)  # 方向向量赋值
snake_length = 9  # 蛇身初始长度
is_clear = 1  # 出否需要删除蛇尾标志位
is_key = 0  # 是否有效按键标志位
death = 0  # 是否死亡标志位

snake = [[0 for i in range(32)] for j in range(32)]  # 定义snake矩阵存储当前蛇身信息，值为0表示不是蛇身；值为1，2，3，4表示蛇身4个方向

for i in range(11, 20, 1):  # 绘制初始蛇形
    snake[16][i] = 1
    draw(16, i)

pygame.display.update()  # 更新图像

while True:
    for event in pygame.event.get():  # 遍历当前事件队列列表
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        else:
            if event.type == pygame.KEYDOWN:  # 若有按键事件
                is_key = 1  # 按键默认有效
                if event.key == pygame.K_RIGHT:  # 若为光标右
                    snake_direction = 4  # 方向赋值
                    if snake[position_snake_head[0]][position_snake_head[1]] == 1 or snake[position_snake_head[0]][
                        position_snake_head[1]] == 2:  # 只有在蛇身方向为上或下时，按下光标右才有效
                        if snake_turn(4):  # 按键有效则进行转向
                            death = 1  # 转向后碰壁或吃自己则死亡
                    else:
                        is_key = 0  # 若蛇身不为上下，则按键无效
                else:  # 其余几个方向同理
                    if event.key == pygame.K_LEFT:
                        snake_direction = 3

                        if snake[position_snake_head[0]][position_snake_head[1]] == 1 or snake[position_snake_head[0]][
                            position_snake_head[1]] == 2:
                            if snake_turn(3):
                                death = 1
                        else:
                            is_key = 0
                    else:
                        if event.key == pygame.K_UP:
                            snake_direction = 1
                            if snake[position_snake_head[0]][position_snake_head[1]] == 3 or \
                                    snake[position_snake_head[0]][
                                        position_snake_head[1]] == 4:
                                if snake_turn(1):
                                    death = 1
                            else:
                                is_key = 0
                        else:
                            if event.key == pygame.K_DOWN:
                                snake_direction = 2
                                if snake[position_snake_head[0]][position_snake_head[1]] == 3 or \
                                        snake[position_snake_head[0]][
                                            position_snake_head[1]] == 4:
                                    if snake_turn(2):
                                        death = 1
                                else:
                                    is_key = 0
                            else:
                                is_key = 0
    if death == 1:
        break  # 死亡即跳出while
    if is_key == 0:  # key无效则蛇头按原方向移动
        if snake_move(snake[position_snake_head[0]][position_snake_head[1]]):  # 蛇头直行
            break  # 直行碰壁或迟到自己则跳出

    if position_snake_head[0] < 1 or position_snake_head[0] > 30:  # 越界跳出
        break
    if position_snake_head[1] < 1 or position_snake_head[1] > 30:  # 越界跳出
        break

    while snake[position_food[0]][position_food[1]]:  # 若食物所在坐标被蛇身占用则重复执行
        position_food[0] = random.randint(1, 30)  # 随机生成food x坐标
        position_food[1] = random.randint(1, 30)  # 随机生成food y坐标
        if is_clear == 1:  # 当蛇尾需要清除时执行
            snake_length += 1  # 蛇身长度+1
            score += 10  # 累加分数
            clear_pxl(645, 100, 100, 35)  # 清除原来的分数文字
        is_clear = 0  # 本轮蛇尾无需清除，即蛇身长度+1

    draw(position_food[0], position_food[1])  # 画foot点，重复则覆盖
    draw(position_snake_head[0], position_snake_head[1])  # 画蛇头
    score_update(str(score))  # 更新分数
    pygame.display.update()  # 更新画板

    if is_clear:  # 如果需要清除
        clear_tail()  # 清除蛇尾像素

    is_clear = 1  # 重置清除位
    is_key = 0  # 重置按键有效位
    pygame.display.update()  # 更新画板
    time.sleep(interval)  # 直执行延迟
screen.blit(textImage_gameover, (600, 200))  # 显示gameover
screen.blit(textImage_finalscore, (570, 225))  # 显示最终分数
textImage_finalscore_value = text_font.render(str(score), True, color_green)  # 定义最终分数值
screen.blit(textImage_finalscore_value, (650, 250))  # 显示最终分数值
pygame.display.update()
time.sleep(5)  # 退出前延迟
