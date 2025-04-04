class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q {self.question_number}. {question.text} (True/False)")
        self.check_answer(user_answer, question.answer)
        print(f'Current Score : {self.score}/{self.question_number}')
        print('\n')

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, u_answer, o_answer):
        if u_answer.lower() == o_answer.lower():
            self.score += 1
            print('You got it right')
        else:
            print('You got it wrong')
        print(f'Correct Answer = {o_answer}')
