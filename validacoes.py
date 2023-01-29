def verificar_caracteres(CEP):
    if CEP.isdigit() == False:
        return "O CEP inserido deve conter apenas números"
    else:
        return True

def verificar_CEP_tamanho(CEP):
    if len(CEP) != 8:
        return "O CEP inserido deve conter 8 dígitos numéricos"
    else:
        return True

def verificar_CEP_positivo(CEP):
    if int(CEP) < 0:
        return "O CEP inserido deve ser um número positivo"
    else:
        return True

def validar_CEP(CEP):

    status = verificar_caracteres(CEP)
    if status != True:
        return status

    status = verificar_CEP_tamanho(CEP)
    if status != True:
        return status
        
    status = verificar_CEP_positivo(CEP)
    return status