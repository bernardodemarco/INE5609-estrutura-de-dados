class View:
    def read_answer(self, message: str = '', is_numeric: bool = False) -> str:
        while True:
            answer = input(message).strip()
            is_empty = len(answer) == 0
            if not is_empty and (not is_numeric or answer.isnumeric()):
                return answer
            message = 'Resposta inválida! Por favor, insira ao menos um caractere'
            if is_numeric:
                message += ' numérico'
            message += '.'
            print(message)

    def show_options(self) -> int:
        print('O que você gostaria de fazer?')
        print('0 - Encerrar')
        print('1 - Carregar dados')
        print('2 - Busca simples')
        print('3 - Busca composta')
        print('4 - Incluir elemento')
        print('5 - Remover elemento')
        print('6 - Exibir dados')
        while True:
            answer = int(self.read_answer(is_numeric=True))
            if 0 <= answer <= 6:
                return answer
            print(
                f'Resposta inválida! Por favor, digite um valor entre 0 e 6.')

    def ask_student_data(self) -> dict:
        print('INSIRA AS SEGUINTES INFORMAÇÕES DO ALUNO:')
        name = self.read_answer('NOME:')
        index = self.read_answer('NÚMERO DE MATRÍCULA:')
        course = self.read_answer('CURSO:')
        soccer_team = self.read_answer('TIME DE FUTEBOL PREFERIDO:')
        salary = int(self.read_answer(message='SALÁRIO:', is_numeric=True))
        return {
            'name': name,
            'index': index,
            'course': course,
            'soccer_team': soccer_team,
            'salary': salary,
        }

    def show_message(self, message: str) -> None:
        print(message)
