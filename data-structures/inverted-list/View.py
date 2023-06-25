from constants import SALARY_CATEGORIES

class View:
    def read_answer(self, message: str = '', is_numeric: bool = False) -> str:
        while True:
            answer = input(message + '\n').strip()
            is_empty = len(answer) == 0
            if not is_empty and (not is_numeric or answer.isnumeric()):
                return answer
            error_message = 'Resposta inválida! Por favor, insira ao menos um caractere'
            if is_numeric:
                error_message += ' numérico'
            error_message += '.'
            print(error_message)

    def show_options(self) -> int:
        print('O que você gostaria de fazer?')
        print('0 - Encerrar')
        print('1 - Carregar dados')
        print('2 - Consulta simples')
        print('3 - Consulta composta')
        print('4 - Incluir elemento')
        print('5 - Remover elemento')
        print('6 - Exibir dados')
        print('--------------------------------------')

        while True:
            answer = int(self.read_answer(is_numeric=True))
            if 0 <= answer <= 6:
                return answer
            print(
                f'Resposta inválida! Por favor, digite um valor entre 0 e 6.')
   
    def show_simple_query_options(self) -> int:
        print('1 - Buscar por curso')
        print('2 - Buscar por time de futebol')
        print('3 - Buscar por salário')
        print('--------------------------------------')

        while True:
            answer = int(self.read_answer(is_numeric=True))
            if 1 <= answer <= 3:
                return answer
            print(
                f'Resposta inválida! Por favor, digite um valor entre 1 e 3.')
   
    def show_composite_query_options(self) -> int:
        print('1 - Buscar por curso e time de futebol')
        print('2 - Buscar por curso e salário')
        print('3 - Buscar por time de futebol e salário')
        print('--------------------------------------')

        while True:
            answer = int(self.read_answer(is_numeric=True))
            if 1 <= answer <= 3:
                return answer
            print(
                f'Resposta inválida! Por favor, digite um valor entre 1 e 3.')

    def get_salary_category(self) -> str:
        print('1 - 0 <= SALÁRIO < 5000 (REAIS)')
        print('2 - 5000 <= SALÁRIO < 10000 (REAIS)')
        print('3 - 10000 <= SALÁRIO (REAIS)')
        print('--------------------------------------')

        while True:
            answer = int(self.read_answer(is_numeric=True))
            if 1 <= answer <= 3:
                return list(SALARY_CATEGORIES.keys())[answer - 1]
            print(
                f'Resposta inválida! Por favor, digite um valor entre 1 e 3.')

    def ask_student_data(self) -> dict:
        print('INSIRA AS SEGUINTES INFORMAÇÕES DO ALUNO:')
        name = self.read_answer('NOME:')
        index = self.read_answer('NÚMERO DE MATRÍCULA:')
        course = self.read_answer('CURSO (abreviação -> sin, cco, eca, ...):').lower()
        soccer_team = self.read_answer('TIME DE FUTEBOL PREFERIDO:').lower()
        salary = int(self.read_answer(message='SALÁRIO:', is_numeric=True))
        return {
            'name': name,
            'index': index,
            'course': course,
            'soccer_team': soccer_team,
            'salary': salary,
        }
    
    def show_student_data(self, data: dict) -> None:
        print(f'NÚMERO DE MATRÍCULA: {data["index"]}')
        print(f'NOME: {data["name"]}')
        print(f'CURSO: {data["course"]}')
        print(f'TIME DE FUTEBOL PREFERIDO: {data["soccer_team"]}')
        print(f'SALÁRIO: {data["salary"]}')
        print('--------------------------------------')

    def show_message(self, message: str) -> None:
        print(message)
