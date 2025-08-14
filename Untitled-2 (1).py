
# QLabel: 문제 표시
# QLineEdit: 사용자 입력
# QPushButton + Signal & Slot: 클릭 시 답 체크
# QMessageBox: 정답/오답 알림

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from datetime import datetime

# 문제 리스트
problems = [
    {"question": "세상에서 가장 빠른 닭은?", "answer": "후다닥"},
    {"question": "병아리가 가장 잘 먹는 약은?", "answer": "삐약"},
    {"question": "왕이 넘어지면?", "answer": "킹콩"},
    {"question": "왕이 외출할 때 타는 차?", "answer": "킹카"},
    {"question": "7 * 8 = ?", "answer": "56"} 
]

score = 0
current_index = 0

def check_answer():
    global score, current_index
    user_answer = answer_input.text().strip()
    
    if user_answer == problems[current_index]["answer"]:
        QMessageBox.information(window, "결과", "정답! 🎉")
        score += 1
    else:
        QMessageBox.warning(window, "결과", f"틀렸습니다 😢 정답: {problems[current_index]['answer']}")
    
    current_index += 1
    if current_index < len(problems):
        problem_label.setText(problems[current_index]["question"])
        answer_input.clear()
    else:
        QMessageBox.information(window, "퀴즈 종료", f"퀴즈가 끝났습니다! 점수: {score}/{len(problems)}")
        save_score()  # 점수 파일 저장
        window.close()

def save_score():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 현재 날짜와 시간
    with open("scores.txt", "a") as f:
        f.write(f"[{now}] 점수: {score}/{len(problems)}\n")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("퀴즈 프로그램")
window.setGeometry(300, 300, 400, 200)

problem_label = QLabel(problems[current_index]["question"], window)
problem_label.move(20, 20)

answer_input = QLineEdit(window)
answer_input.move(20, 60)
answer_input.resize(200, 30)

submit_button = QPushButton("제출", window)
submit_button.move(240, 60)
submit_button.clicked.connect(check_answer)

window.show()
sys.exit(app.exec_())


