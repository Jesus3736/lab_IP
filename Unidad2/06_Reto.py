cuenta = float(input("Total de la cuenta: "))
porcentaje = float(input("Porcentaje de propina: "))
personas = int(input("Numero de personas: "))

propina = cuenta * porcentaje / 100
total_con_propina = cuenta + propina
pago_por_persona = total_con_propina / personas

print(f"Total con propina: {total_con_propina:.2f}")
print(f"Cada persona paga: {pago_por_persona:.2f}")
print(f"Propina: {propina:.2f}")


"""
== > Iguales
!= > diferentes
> > Mayor que
< > Menor que
>= > Mayor o igual que
<= > Menor o igual que
"""