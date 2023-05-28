import time


class Screen:
    def validate_option(self, max_value: int):
        while True:
            try:
                print('')
                option = int(input())
                if 0 <= option <= max_value:
                    return option
                else:
                    raise ValueError
            except ValueError:
                print('ERRO!: Opção inválida, por favor, tente novamente!')

    def show_options(self):
        print("AKINATOR - TIMES DE FUTEBOL")
        print("O que você gostaria de fazer?")
        print("        0 - Encerrar jogo")
        print("        1 - Iniciar jogo novo")
        print("        2 - Continuar jogando")
        return self.validate_option(2)

    def ask_difference(self, team_name):
        user_team = input(
            f'Em qual time você pensou? \n').lower().strip().capitalize()
        difference_between_teams = input(
            f'O que diferencia o (a) {team_name} do (da) {user_team}?\n').lower().strip().capitalize() + '?'
        return (user_team, difference_between_teams)

    def guess_answer(self, team_name):
        return input(f'Você pensou no (a) {team_name}? (s/n)\n').lower().strip()

    def show_message(self, message: str) -> None:
        print(message)

    def read_answer(self):
        return input().lower().strip()
