def read_file():
    try:
        filename=input('ievadiet faila nosaukumu:')
        with open(filename, 'r') as file:
            content=file.read()
            print('faila saturs:')
            print(content)
    except FileNotFoundError:
        print(f'Kluda: Fails "{filename}" netika atrasts.')
            
    except PermissionError:
        print(f'Kluda: nav piekluves tiesibu failam "{filename}".')

    except Exception as e:
        print(f'Radas kluda:{e}')

    finally:
        print('Faila apstrade pabeigta.')

read_file()