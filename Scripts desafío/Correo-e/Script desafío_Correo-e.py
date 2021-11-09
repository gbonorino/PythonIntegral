# Script Correos electrónicos
# Autor: yo
# Fecha: hoy
# Propósito: Tomar un listado de correos 
#    y segregar usuario y dominio
# Entrada: Una lista con direcciones electrónicas


correos_e = ['novedades@mail.bbva.com.ar','americanairlines@aadvantage.email.aa.com','americanexpress@email.americanexpress.com','eventanilla@afip.gov.ar','no-reply@e.udemymail.com']
def titulo(opcion):
    if opcion == 'usuario':
        print('Los usuarios son:')
    else:
        print('Los dominios son:')

usuario=[]
dominio=[]
for correo in correos_e:
    u = correo[:correo.index('@')]
    d = correo[correo.index('@')+1:]
    usuario.append(u)
    dominio.append(d)
    
titulo('usuario')
for j in usuario:
    print(j)
print()    
titulo('dominio')
for k in dominio:
    print(k)



