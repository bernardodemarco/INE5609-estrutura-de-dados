class Screen:
    def __validate_option(self, max_value: int) -> int:
        while True:
            answer = int(self.read_answer())
            if 0 <= answer <= max_value:
                return answer
            print(
                f'Resposta inválida! Por favor, digite um número entre 0 e {max_value}.')

    def show_options(self) -> int:
        print('AKINATOR - TIMES DE FUTEBOL')
        print('O que você gostaria de fazer?')
        print('0 - Encerrar')
        print('1 - Jogar')
        return self.__validate_option(1)

    def read_answer(self, message='') -> str:
        return input(message).lower().strip()

    def yes_or_no_question(self, question: str) -> str:
        while True:
            answer = self.read_answer(question)
            if answer == 's' or answer == 'n':
                return answer
            print('Resposta inválida! Por favor, digite "s" para sim e "n" para não.')

    def guess_answer(self, team_name: str) -> str:
        guess = f'Você pensou no (a) {team_name}? (s/n)\n'
        return self.yes_or_no_question(guess)

    def ask_question(self, question: str) -> str:
        message = f'O time que você pensou {question} (s/n)?\n'
        return self.yes_or_no_question(message)

    def ask_difference(self, team_name: str) -> tuple:
        team_question = f'Em qual time você pensou? \n'
        new_team = self.read_answer(team_question).capitalize()

        difference_question = f'O que diferencia o (a) {team_name} do (da) {new_team}?\n'
        difference = self.read_answer(difference_question)

        return (new_team, difference)

    def show_message(self, message: str) -> None:
        print(message)
