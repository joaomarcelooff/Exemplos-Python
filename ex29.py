from colorama import Fore, Style  # Biblioteca de cores nos textos

km = int(input('Qual a velocidade do seu carro? '))

if km > 80:
    multa = (km - 80) * 7
    print(Fore.RED + f'MULTADO! Você excedeu o limite permitido que é de 80 km/h.\nVocê deve pagar uma multa de R${multa:.2f}' + Style.RESET_ALL)
    print(Fore.MAGENTA + 'Tenha um bom dia, dirija com segurança!'+ Style.RESET_ALL)
else:
    print(Fore.GREEN + 'Excelente! Tenha um bom dia, dirija com segurança!' + Style.RESET_ALL)