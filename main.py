from tkinter import *
import requests
import validacoes

def buscar_CEP():
    
    CEP = CEP_entrada.get()

    avaliacao = validacoes.validar_CEP(CEP)
    
    if avaliacao != True:
        texto_resposta["text"] = avaliacao

    else:
        url = f"https://brasilapi.com.br/api/cep/v1/{CEP}"
        requisicao = requests.get(url)

        if requisicao.status_code == 200:
            requisicao_dic = requisicao.json()

            texto_resposta["text"]= f"""
            {requisicao_dic["street"]},  {requisicao_dic["neighborhood"]}
            {requisicao_dic["cep"]}, {requisicao_dic["city"]} - {requisicao_dic["state"]}
            """
        
        else:
            texto_resposta["text"]="Não foi possível localizar o CEP desejado"

texto_resposta = {
    "text": ""
}

janela = Tk()
janela.title("Buscador de CEP")
janela.geometry("500x150")

texto = Label(janela, text="Digite um CEP (somente números):" , font="arial 9 bold")
texto.pack(pady = 10)

CEP_entrada = Entry(janela, justify = "center")
CEP_entrada["width"] = 10
CEP_entrada.pack()

botao = Button(janela, text = "Buscar endereço", command = buscar_CEP)
botao.pack(pady = 10)

texto_resposta = Label(janela, text="", justify = "center")
texto_resposta.pack(pady = 10)


janela.mainloop()