import pygame
import random
import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ==========================
# 初期化
# ==========================
pygame.init()

# ==========================
# 画面設定
# ==========================
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("4択クイズ")

# ==========================
# 日本語フォント
# quiz.pyの場所を基準にフォントを読み込む
# ==========================
BASE_DIR = os.path.dirname(__file__)
FONT_PATH = os.path.join(BASE_DIR, "fonts", "NotoSansJP-Bold.ttf")

font_question = pygame.font.Font(FONT_PATH, 40)
font_choice = pygame.font.Font(FONT_PATH, 30)
font_result = pygame.font.Font(FONT_PATH, 36)

# ==========================
# 色
# ==========================
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (210, 210, 210)
GREEN = (120, 230, 120)
RED = (255, 120, 120)

# ==========================
# 問題データ
# ==========================
quiz_data = [
    {
        "question": "日本の首都は？",
        "choices": ["大阪", "東京", "名古屋", "福岡"],
        "answer": 1
    },
    {
        "question": "Pythonを開発した人物は？",
        "choices": [
            "Guido van Rossum",
            "Linus Torvalds",
            "Bill Gates",
            "Steve Jobs"
        ],
        "answer": 0
    },
    {
        "question": "1 + 1 = ?",
        "choices": ["1", "2", "3", "4"],
        "answer": 1
    }
]

# ==========================
# 問題選択
# ==========================
current_quiz = None
answered = False
message = ""

def next_question():
    global current_quiz, answered, message

    current_quiz = random.choice(quiz_data)
    answered = False
    message = ""

next_question()

# ==========================
# ボタン作成
# ==========================
buttons = []

for i in range(4):
    buttons.append(
        pygame.Rect(120, 200 + i * 80, 560, 60)
    )

# ==========================
# メインループ
# ==========================
running = True

while running:

    screen.fill(WHITE)

    # ----------------------
    # 問題表示
    # ----------------------
    question = font_question.render(current_quiz["question"], True, BLACK)
    screen.blit(question, (40, 50))

    # ----------------------
    # 選択肢表示
    # ----------------------
    for i, rect in enumerate(buttons):

        color = GRAY

        if answered and i == current_quiz["answer"]:
            color = GREEN

        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)

        text = font_choice.render(current_quiz["choices"][i], True, BLACK)
        screen.blit(text, (rect.x + 20, rect.y + 15))

    # ----------------------
    # 判定表示
    # ----------------------
    result = font_result.render(message, True, RED)
    screen.blit(result, (40, 550))

    pygame.display.flip()

    # ======================
    # イベント処理
    # ======================
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if not answered:

                mouse_pos = pygame.mouse.get_pos()

                for i, rect in enumerate(buttons):

                    if rect.collidepoint(mouse_pos):

                        answered = True

                        if i == current_quiz["answer"]:
                            message = "正解！"
                        else:
                            correct = current_quiz["choices"][current_quiz["answer"]]
                            message = f"不正解！ 正解は『{correct}』です。"

        elif event.type == pygame.KEYDOWN:

            if answered and event.key == pygame.K_SPACE:
                next_question()

pygame.quit()
sys.exit()