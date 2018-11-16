"""Case-study #1 Our`s first code
Developers:
Stanislav Bykov, Balabanov Mikhail, Denis Borodkin


"""
import ru_local

print('{}'.format(ru_local.TAXO), end='')
Tax0 = float(input())  # Advance payment for the IV quarter of the previous year
print('{}'.format(ru_local.WPROFITI), end='')
Profit1 = float(input())  # Profit for the I quarter
print('{}'.format(ru_local.WDEDUDCTIONI), end='')
Deduction1 = float(input())  # Deductions for the I quarter
print('{}'.format(ru_local.WPROFITII), end='')
Profit2 = float(input())  # Profit for the II quarter
print('{}'.format(ru_local.WDEDUDCTIONII), end='')
Deduction2 = float(input())  # Deductions for the II quarter
print('{}'.format(ru_local.WPROFITIII), end='')
Profit3 = float(input())  # Profit for the III quarter
print('{}'.format(ru_local.WDEDUDCTIONIII), end='')
Deduction3 = float(input())  # Deductions for the III quarter
print('{}'.format(ru_local.WPROFITIV), end='')
Profit4 = float(input())  # Profit for the IV quarter
print('{}'.format(ru_local.WDEDUDCTIONIV), end='')
Deduction4 = float(input())  # Deductions for the IV quarter

Tax1 = (Profit1 - Deduction1)*0.2  # Tax for the I quarter

print('{}'.format(ru_local.TAXV), Tax0, sep=' ')
print('{}'.format(ru_local.AMOUNTIIIII), round(Tax0/3, 2), ru_local.RIM)
print('{}'.format(ru_local.PROFITI), round(Profit1, 2), sep=' ')
print('{}'.format(ru_local.DEDUCTIONI), round(Deduction1, 2), sep=' ')
print('{}'.format(ru_local.TAXI), round(Tax1, 2), ru_local.RUB)
if Tax1 > Tax0:
    print('{}'.format(ru_local.NEEDPAYI), round(Tax1 - Tax0, 2), ru_local.RUB)
elif Tax0 > Tax1:
    print('{}'.format(ru_local.EXTRAPAYI), round(Tax0 - Tax1, 2), ru_local.RUB)
else:
    print('{}'.format(ru_local.DEBTI))

Tax2 = (Profit2 - Deduction2)*0.2  # Tax for the II quarter

print('{}'.format(ru_local.AMOUNTIVVVI), round(Tax1/3, 2), ru_local.RIM)
print('{}'.format(ru_local.PROFITII), round(Profit2, 2), sep=' ')
print('{}'.format(ru_local.DEDUCTIONII), round(Deduction2, 2), sep=' ')
print('{}'.format(ru_local.TAXII), round(Tax2, 2), ru_local.RUB)
if Tax2 > Tax1:
    print('{}'.format(ru_local.NEEDPAYII), round(Tax2-Tax1, 2), ru_local.RUB)
elif Tax1 > Tax2:
    print('{}'.format(ru_local.EXTRAPAYII), round(Tax1-Tax2, 2), ru_local.RUB)
else:
    print('{}'.format(ru_local.DEBTII))

Tax3 = (Profit3 - Deduction3)*0.2  # Tax for the III quarter

print('{}'.format(ru_local.AMOUNTVIIVIIIIX), round(Tax2/3, 2), ru_local.RIM)
print('{}'.format(ru_local.PROFITIII), round(Profit3, 2), sep=' ')
print('{}'.format(ru_local.DEDUCTIONIII), round(Deduction3, 2), sep=' ')
print('{}'.format(ru_local.TAXIII), round(Tax3, 2), ru_local.RUB)
if Tax3 > Tax2:
    print('{}'.format(ru_local.NEEDPAYIII), round(Tax3-Tax2, 2), ru_local.RUB)
elif Tax2 > Tax3:
    print('{}'.format(ru_local.EXTRAPAYIII), round(Tax2-Tax3, 2), ru_local.RUB)
else:
    print('{}'.format(ru_local.DEBTIII))

Tax4 = (Profit3 - Deduction3)*0.2  # Tax for the IV quarter

print('{}'.format(ru_local.AMOUNTXXIXII), round(Tax3/3, 2), ru_local.RIM)
print('{}'.format(ru_local.PROFITIV), round(Profit4, 2), sep=' ')
print('{}'.format(ru_local.DEDUCTIONIV), round(Deduction4, 2), sep=' ')
print('{}'.format(ru_local.TAXIV), round(Tax4, 2), ru_local.RUB)
if Tax4 > Tax3:
    print('{}'.format(ru_local.NEEDPAYIV), round(Tax4 - Tax3, 2), ru_local.RUB)
elif Tax3 > Tax4:
    print('{}'.format(ru_local.EXTRAPAYIV), round(Tax3-Tax4, 2), ru_local.RUB)
else:
    print('{}'.format(ru_local.DEBTIV))
