def divide_numbers():
    try:
        num1=float(input('Ievadiet pirmo skaitli: '))
        num2=float(input('Ievadiet otro skaitli: '))
        result=num1/num2
        print(f'Rezultats: {result}')

    except ZeroDivisionError:
        print('Kluda: Dalisana ar nulli nav atlauta.')

    except ValueError:
        print('Kluda: Ludzu ievadiet derigus skaitlus.')

    except Exception as e:
        print('Radas neparedzeta kluda: {e}.')       

    finally:
        print('Darbiba pabeigta.')

divide_numbers()             