def income_tax_calculation():
    value_min = 2112.00
    value_seven_percent = 2826.65
    value_fifteen_percent = 3751.05
    value_twenty_two_percent = 4664.68
    first_aliquot = 0.075
    second_aliquot = 0.15
    third_aliquot = 0.225
    fourth_aliquot = 0.275
    value_max_first_aliquot = 53.6
    value_max_second_aliquot = 192.26
    value_max_third_aliquot = 397.83
    remuneration = input('Digite a remuneração do colaborador: ')
    remuneration = float(remuneration)
    if remuneration <= value_min:
        return 'Esse colaborador está isento de IR.'
    if remuneration <= value_seven_percent:
        total_discount = (remuneration - value_min) * first_aliquot
        total_value = remuneration - total_discount
        return f'O colaborador receberá um salário líquido de R${total_value:.2f} \n e o desconto do IR será no valor de R${total_discount:.2f}'
    if remuneration <= value_fifteen_percent:
        total_discount = ((remuneration - value_seven_percent) * second_aliquot) + value_max_first_aliquot
        total_value = remuneration - total_discount
        return f'O colaborador receberá um salário líquido de R${total_value:.2f} \n e o desconto do IR será no valor de R${total_discount:.2f}'
    if remuneration <= value_twenty_two_percent:
        total_discount = ((remuneration - value_fifteen_percent) * third_aliquot) + value_max_second_aliquot
        total_value = remuneration - total_discount
        return f'O colaborador receberá um salário líquido de R${total_value:.2f} \n e o desconto do IR será no valor de R${total_discount:.2f}'
    else:
        total_discount = ((remuneration - value_twenty_two_percent) * fourth_aliquot) + value_max_third_aliquot
        total_value = remuneration - total_discount
        return f'O colaborador receberá um salário líquido de R${total_value:.2f} \n e o desconto do IR será no valor de R${total_discount:.2f}'


print(income_tax_calculation())

