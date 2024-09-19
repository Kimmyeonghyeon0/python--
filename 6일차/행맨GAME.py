# 기본 라이브러리라 파이썬 설치시 자동으로 설치됩니다!
# random 모듈은 랜덤한 숫자를 생성할 때 사용합니다.
import random

# 게임에 사용될 단어 목록
words = ["apple", "banana", "orange", "grape", "lemon"]

# 행맨 그림
hangman_pics = [
    """
     ------
     |    |
     |
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    ---""",
]

def ascii_welcome():
            print("""
  _    _      _                            _        
 | |  | |    | |                          | |       
 | |  | | ___| | ___ ___  _ __ ___   ___   | |_ ___  
 | |  | |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \  | __/ _ \ 
 | |__| |  __/ | (_| (_) | | | | | |  __/  | || (_) |
  \____/ \___|_|\___\___/|_| |_| |_|\___|   \__\___/ 
                                                    
                                                    
            """)

def game_over_ascii():
    print("""
  ██████  ▄▄▄       ███▄    █ ▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
▒██    ▒ ▒████▄     ██ ▀█   █ ▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒██  ▀█▄  ▓██  ▀█ ██▒▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
  ▒   ██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒ ▓█   ▓██▒▒██░   ▓██░░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░  ░  ░    ░   ▒      ░   ░ ░    ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░        ░  ░         ░    ░  ░       ░ ░        ░    
        """)
    
    
class HangmanGame:
    def __init__(self):
        self.word = random.choice(words)  # 랜덤으로 단어 선택
        self.letters = ""  # 사용자가 입력한 모든 알파벳을 저장
        self.life = 6  # 목숨 & 시도 횟수 (행맨 그림 단계 수에 맞춰 6으로 설정)

    def display(self):
        succeed = True
        print()
        for h in self.word:  # 단어를 가져옴
            if h in self.letters:  # 사용자가 입력한 알파벳에 대해 답인지 아닌지에 대한 출력
                print(h, end="")  # 정답이면 알파벳 표시
            else:
                print("_", end=" ")  # 오답이면 "_" 표시
                succeed = False
        print()
        return succeed

    def play(self):
        ascii_welcome()
        while self.life > 0:
            # 현재 상태 출력
            print(hangman_pics[6 - self.life])  # 남은 목숨에 따라 행맨 그림 출력
            if self.display():  # 단어가 완성되었는지 확인
                print("럭키비키한 두뇌로 단어를 완성 하셨습니다!!")
                break

            # 사용자 입력
            letter = input("알파벳을 입력해주세요(소문자로): ").lower()

            if len(letter) != 1:  # 한 글자만 입력하도록 제한
                print("한 글자만 입력해주세요.")
                continue

            if letter in self.letters:  # 이미 입력한 글자인지 확인
                print("이미 입력한 알파벳입니다.")
                continue

            # 입력한 알파벳 저장
            self.letters += letter

            # 알파벳이 단어에 있는지 확인
            if letter in self.word:
                print("단어를 맞추셨군요? 조금만 더 힘내봐요!")
            else:
                self.life -= 1  # 틀리면 목숨 감소
                print(f"틀렸습니다... 남은 횟수는 {self.life}회입니다.")

        if self.life == 0:
            game_over_ascii()
            print(f"아쉽게도 실패하셨습니다. 정답은 '{self.word}'였습니다.")

if __name__ == "__main__":
    game = HangmanGame()
    game.play()
