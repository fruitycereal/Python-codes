class InterviewConfig:
    """Configuration settings for the interview process"""

    def __init__(self):
        self.max_questions = 5  # Maximum number of questions in the interview
        self.min_questions = 3  # Minimum number of questions before allowing conclusion
        self.question_count = 0  # Current question count
        self.is_completed = False  # Interview completion status

    def increment_question(self):
        self.question_count += 1
        return self.question_count

    def can_conclude(self):
        return self.question_count >= self.min_questions

    def should_conclude(self):
        return self.question_count >= self.max_questions

    def get_remaining_questions(self):
        return self.max_questions - self.question_count

    def reset(self):
        self.question_count = 0
        self.is_completed = False
