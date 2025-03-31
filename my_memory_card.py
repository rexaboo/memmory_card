#создай приложение для запоминания информации
from random import shuffle
from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox, QRadioButton, QHBoxLayout, QGroupBox, QButtonGroup

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list = []
question_list.append(Question('Небо - ?', 'синее', 'хз не смотрел', 'перламутровое', 'я хз лол'))
question_list.append(Question('Какого океана не бывает?', 'Кабардино - Балканского', 'Тихого', 'Индийского', 'Северно - Ледовитого'))
question_list.append(Question('2 + 2 = ?', '4', '3', '22', '5'))
#question_list.append(Question('Предпочитаешь кофе или чай?', 'кофе', 'чай', 'и то и другое', 'не пью ни то ни другое'))
#question_list.append(Question('Какая твоя любимая пора года?', 'лето', 'зима', 'весна', 'осень'))
def show_result():
    RadioGroupBox.hide()
    PanelGroupBox.show()
    bigbutton.setText('Следующий вопрос')
def show_question():
    RadioGroupBox.show()
    PanelGroupBox.hide()
    bigbutton.setText('Ответить')
    RadioGroup.setExclusive(False) 
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)
'''def start_test():
    if bigbutton.text() == 'Ответить':
        show_result()
    else:
        show_question()'''

app = QApplication([])

vopros = QLabel('Какой национальности не существует?')
bigbutton = QPushButton('Ответить')
RadioGroupBox = QGroupBox('Варианты ответов')

rbtn1 = QRadioButton('Энцы')
rbtn2 = QRadioButton('Чулымцы')
rbtn3 = QRadioButton('Смурфы')
rbtn4 = QRadioButton('Алеуты')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)
answers = [rbtn1, rbtn2, rbtn3, rbtn4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    vopros.setText(q.question)
    correct.setText(q.right_answer)
    show_question()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        window.score += 1
        patrick_chet = (window.score/window.total)*100
        print('Статистика\n-Всего вопросов:', window.total, '\nПравильных ответов:', window.score)
        print('Рейтинг:', patrick_chet, '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!') 
            print('Рейтинг:', (window.score/window.total*100), '%')
def next_question():
    #window.cur_question = window.cur_question + 1
    window.total +=1
    print('Статистика\n-Всего вопросов:', window.total, '\nПравильных ответов:', window.score)
    cur_question = randint(0, len(question_list) -1)
    q = question_list[cur_question]
    ask(q)
def click_ok():
    if bigbutton.text() == 'Ответить':
        check_answer()
    else:
        next_question()
def show_correct(res):
    result.setText(res)
    show_result()


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

PanelGroupBox = QGroupBox('Результат теста')
result = QLabel('Правильно/Неправильно')
correct = QLabel('Правильный ответ')

layout_result = QVBoxLayout()
layout_result.addWidget(result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_result.addWidget(correct, alignment = Qt.AlignHCenter, stretch = 2)
PanelGroupBox.setLayout(layout_result)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(vopros, alignment = (Qt.AlignHCenter|Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(PanelGroupBox)
PanelGroupBox.hide()
'''RadioGroupBox.hide()'''

layout_line3.addStretch(1)
layout_line3.addWidget(bigbutton, stretch = 2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.cur_question = -1
#q = Question('Выбери перевод слова переменная', 'variable', 'мячик', 'вода', 'камень')
window.resize(300, 200)

#ask(q)
bigbutton.clicked.connect(click_ok) 

window.total = 0
window.score = 0

next_question()

window.show()
app.exec()