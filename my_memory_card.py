from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup
import random


class Question():
    def __init__(self, text, cor_ans, ans2, ans3, ans4):
        self.text_question = text
        self.cor_ans = cor_ans
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4

def show_result():
    group_ans.hide()
    group_result.show()
    button.setText('следующий вопрос')

def show_question():
    group_result.hide()
    group_ans.show()
    button.setText('Ответить')
    group_var.setExclusive(False)
    var_ans1.setChecked(False)
    var_ans2.setChecked(False)
    var_ans3.setChecked(False)
    var_ans4.setChecked(False)
    group_var.setExclusive(True)

def ask(q):
    show_question()
    random.shuffle(radio_buttons)
    question.setText(q.text_question)
    cor_label.setText(str(q.cor_ans))
    radio_buttons[0].setText(str(q.cor_ans))
    radio_buttons[1].setText(str(q.ans2))
    radio_buttons[2].setText(str(q.ans3))
    radio_buttons[3].setText(str(q.ans4))

def check_answer():
    main_win.num_questions += 1
    if radio_buttons[0].isChecked():
        show_correct('правильно')
        main_win.num_cor_answers += 1
    elif radio_buttons[1].isChecked() or radio_buttons[2].isChecked() or radio_buttons[3].isChecked():
        show_correct('неправильно')
    print('Статистика')
    print('Всего вопросов:', main_win.num_questions)
    print('Правильных ответов:', main_win.num_cor_answers)
    print('Рейтинг:', str(round(main_win.num_cor_answers/main_win.num_questions * 100, 1)) + '%')

def show_correct(result):
    if result == 'правильно':
        res_label.setText('Правильно!')
    elif result == 'неправильно':
        res_label.setText('Неправильно')
    show_result()

def next_question():
    ask(questions[random.randint(0, len(questions) - 1)])
    
def click_ok():   
    if button.text() == 'Ответить':
        check_answer()
    elif button.text() == 'следующий вопрос':
        next_question()


app = QApplication([])
main_win = QWidget()

main_win.setWindowTitle('Memory card')
main_win.resize(400, 400)
main_win.num_questions = 0
main_win.num_cor_answers = 0

question = QLabel('На какой языке написана программа?')
group_ans = QGroupBox('Варианты ответов')
button = QPushButton('Ответить')

var_ans1 = QRadioButton()
var_ans2 = QRadioButton()
var_ans3 = QRadioButton()
var_ans4 = QRadioButton()
radio_buttons = [var_ans1, var_ans2, var_ans3, var_ans4]
group_var = QButtonGroup()
group_var.addButton(var_ans1)
group_var.addButton(var_ans2)
group_var.addButton(var_ans3)
group_var.addButton(var_ans4)

group_line = QVBoxLayout()
group_ans.setLayout(group_line)
group_line_h1 = QHBoxLayout()
group_line_h2 = QHBoxLayout()
group_line_h1.addWidget(var_ans1)
group_line_h1.addWidget(var_ans3)
group_line_h2.addWidget(var_ans2)
group_line_h2.addWidget(var_ans4)
group_line.addLayout(group_line_h1)
group_line.addLayout(group_line_h2)


group_result = QGroupBox('Результат теста')
res_label = QLabel('Правильно/Неправильно')
cor_label = QLabel('Правильный ответ')
gr_res_line = QVBoxLayout()
group_result.setLayout(gr_res_line)
gr_res_line.addWidget(res_label)
gr_res_line.addWidget(cor_label, alignment=Qt.AlignCenter)
group_result.hide()

main_line = QVBoxLayout()
main_win.setLayout(main_line)
main_line.addWidget(question, alignment=Qt.AlignCenter)
main_line.addWidget(group_ans, alignment=Qt.AlignCenter)
main_line.addWidget(group_result, alignment=Qt.AlignCenter)
main_line.addWidget(button, alignment=Qt.AlignCenter)

question_1 = Question('Сколько цветов в радуге?', 7, 9, 4, 1)
question_2 = Question('Какой цвет получается при смешивании синего и желтого?', 'Зеленый', 'Красный', 'Фиолетовый', 'Оранжевый')
question_3 = Question('Какой из этих континентов самый большой по площади?', 'Азия', 'Африка', 'Европа', 'Северная Америка')
question_4 = Question('Какой элемент обозначается символом "H" в таблице Менделеева?', 'Водород', 'Гелий', 'Азот', 'Кислород')
question_5 = Question('На какой языке написана программа?', 'Python', 'Английский', 'Кумир', 'Русский')
questions = [question_1, question_2, question_3, question_4, question_5] 
ask(question_1)
button.clicked.connect(click_ok)

main_win.show()
app.exec_()



#создай приложение для запоминания информации