import os
os.system('clear')
try:
   while True:
        import setup
        opcao = str(input(f'//: '))
        if opcao == '1':
            from modulos.painel import painel
        elif opcao == '2':
            from modulos.scan import scan
        elif opcao == '3':
            from modulos.track import track
        elif opcao == '4':
            from modulos.calculadora import calculadora
        elif opcao == '5':
            from modulos.pacote import pacote
        elif opcao == '6':
            from modulos.pegalammer import pegalammer
        elif opcao == '7':
            print(f'\nSaindo...')
            time.sleep(1)
            os.system('clear')
            break
        else:
            print(f'Comando não reconhecido')
            sleep(1)
except KeyboardInterrupt:
    print(f'\nSaindo...')
    time.sleep(1)
