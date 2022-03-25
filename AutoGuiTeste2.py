from tkinter import *
import pyautogui as auto
import pyperclip as pyper
import mysql.connector
from time import sleep
from selenium import webdriver
from random import randint
from datetime import datetime
from datetime import date

sleep(5)
print(auto.position())

con = mysql.connector.connect(host='localhost', database='sefip', user='root', password='')
cursor = con.cursor()
if con.is_connected():
    db_info = con.get_server_info()
    print('Conectado ao servidor MySQL versão ', db_info)

janela1 = Tk()
janela1.geometry('550x300')

def Size(*args):
    razaovalue = razaoValue.get()
    logvalue = logValue.get()
    bairrovalue = bairroValue.get()
    cityvalue = cityValue.get()
    cepvalue = cepValue.get()
    telvalue = telValue.get()
    dddvalue = dddValue.get()
    if len(razaovalue) > 39: razaoValue.set(razaovalue[:39])
    if len(logvalue) > 49: logValue.set(logvalue[:49])
    if len(bairrovalue) > 19: bairroValue.set(bairrovalue[:19])
    if len(cityvalue) > 19: cityValue.set(cityvalue[:19])
    if len(cepvalue) > 8: cepValue.set(cepvalue[:8])
    if len(telvalue) > 8: telValue.set(telvalue[:8])
    if len(dddvalue) > 2: dddValue.set(dddvalue[:2])


razaoValue = StringVar()
razaoValue.trace('w', Size)

logValue = StringVar()
logValue.trace('w', Size)

bairroValue = StringVar()
bairroValue.trace('w', Size)

cityValue = StringVar()
cityValue.trace('w', Size)

cepValue = StringVar()
cepValue.trace('w', Size)
telValue = StringVar()
telValue.trace('w', Size)

dddValue = StringVar()
dddValue.trace('w', Size)


# numero da pasta
npastatxt = Label(janela1, text='Número')
npastatxt.place(x=0, y=0)

npasta = Entry(janela1, width=5)
npasta.place(x=80, y=0)

# nome da pasta
pastatxt = Label(janela1, text='Pasta')
pastatxt.place(x=120, y=0)

pasta = Entry(janela1, width=30)
pasta.place(x=160, y=0)

# CNPJ
cnpjtxt = Label(janela1, text='CNPJ')
cnpjtxt.place(x=0, y=25)

cnpj = Entry(janela1, width=20)
cnpj.place(x=80, y=25)

# Razao Social
razaotxt = Label(janela1, text='Razão Social')
razaotxt.place(x=0, y=50)

razao = Entry(janela1, width=38, textvariable=razaoValue)
razao.place(x=80, y=50)

# Logradouro
logtxt = Label(janela1, text='Logradouro')
logtxt.place(x=0, y=80)

log = Entry(janela1, width=45, textvariable=logValue)
log.place(x=80, y=80)

# Bairro
bairrotxt = Label(janela1, text='Bairro')
bairrotxt.place(x=0, y=105)

bairro = Entry(janela1, width=25, textvariable=bairroValue)
bairro.place(x=80, y=105)

# cep
ceptxt = Label(janela1, text='CEP')
ceptxt.place(x=235, y=105)

cep = Entry(janela1, width=15, textvariable=cepValue)
cep.place(x=260, y=105)

# cidade
cidadetxt = Label(janela1, text='Cidade')
cidadetxt.place(x=0, y=130)

cidade = Entry(janela1, width=25, textvariable=cityValue)
cidade.place(x=80, y=130)

# UF
uftxt = Label(janela1, text='UF')
uftxt.place(x=235, y=130)

uf = Entry(janela1, width=15)
uf.place(x=260, y=130)

# DDD
dddtxt = Label(janela1, text='DDD')
dddtxt.place(x=0, y=155)

ddd = Entry(janela1, width=3, textvariable=dddValue)
ddd.place(x=80, y=155)

# Telefone
teltxt = Label(janela1, text='Telefone')
teltxt.place(x=110, y=155)

tel = Entry(janela1, width=20, textvariable=telValue)
tel.place(x=160, y=155)

# CNAE
cnaetxt = Label(janela1, text='CNAE')
cnaetxt.place(x=0, y=180)

cnae= Entry(janela1, width=7)
cnae.place(x=80, y=180)



# Botão de coleta de dados
def myClick():
    pastanum = npasta.get()
    pastaname = pasta.get()
    cnpjdata = cnpj.get()
    global razaodata
    razaodata = razao.get()
    logdata = log.get()
    bairrodata = bairro.get()
    cepdata = cep.get()
    global cidadedata
    cidadedata = cidade.get()
    ufdata = uf.get()
    ddddata = ddd.get()
    teldata = tel.get()
    cnaedata = cnae.get()

    auto.PAUSE = 3

    pyper.copy(f'{pastanum} - {pastaname}')

    sleep(1)

    auto.click(x=422, y=747)

    #clica na barra de diretorio
    auto.click(x=806, y=163)

    #escreve o diretorio
    auto.write("C:\\Users\\Public\\Documents\\Empresas CM")

    #dá enter
    auto.press('enter')

    #abre nova pasta
    auto.click(x=503, y=79)

    #escreve o nome da pasta
    auto.hotkey('ctrl', 'v')

    auto.press('enter')
    #abrir a barra de pesquisa
    auto.press('win')
    #clica no sefip
    auto.click(x=474, y=290)
    sleep(4)
    #maximiza o sefip
    auto.click(x=973, y=132)
    #clica no lsc
    auto.click(x=110, y=107)
    #clica em nova empresa
    auto.click(x=1213, y=689)
    #celeciona cnpj-1
    auto.press('1')
    #barra do cnpj
    auto.press('tab')
    #escreve o cnpj
    auto.write(cnpjdata)
    #linha da razao social
    auto.press('tab')
    #escreve a razao social
    auto.write(razaodata)
    #linha do logradouro
    auto.press('tab')
    #escreve o logradouro
    auto.write(logdata)
    #linha do bairro
    auto.press('tab')
    #escreve o bairro
    auto.write(bairrodata)
    #vai para a linha do cep
    if len(bairrodata) < 20:
        auto.press('tab')
    #escreve o cep
    auto.write(cepdata)
    #escreve cidade
    auto.write(cidadedata)
    #linha da uf
    auto.press('tab')
    #escreve a uf
    auto.write(ufdata)
    #linha do ddd
    auto.click(x=316, y=284, clicks=3)
    #escreve ddd
    auto.write(ddddata)
    #linha do telefone
    auto.press('tab')
    #telefone
    auto.write(teldata)
    #escreve cnae
    auto.write(cnaedata)
    #clica no cnae
    auto.click(x=316, y=350)
    #linha do cnae preponderante
    auto.press('tab')
    #escreve cnae preponderante
    auto.write(cnaedata)
    #clica no cnae preponderante
    auto.click(x=542, y=349)
    #linha do fpas
    auto.press('tab')
    #escreve fpas
    auto.write('515')
    #clica em salvar
    auto.click(x=1224, y=690, clicks=3)
    #confirma dados
    auto.click(x=641, y=418)

    # atualiza
    auto.press('f5')
    # clica no binoculos
    auto.click(x=198, y=60)
    # escreve a empresa que quer achar
    auto.write(razaodata)
    # clica em localizar
    auto.click(x=946, y=239)
    # clica na empresa que foi incluída
    auto.click(x=534, y=380, clicks=2)
    # clica em fechar
    auto.click(x=957, y=272)
    # clica em novo trabalhador
    auto.click(x=984, y=691)

def myClick4():
    auto.PAUSE = 3
    sleep(1)
    #clica em executar
    auto.click(x=1115, y=688)
    sleep(10)
    #clica em ok
    auto.click(x=676, y=424)
    #clica nos diretórios
    auto.click(x=851, y=257)
    #minimiza a pasta
    auto.click(x=588, y=307)
    #clica em usuarios
    auto.click(x=586, y=448)
    #clica em publico
    auto.click(x=605, y=466)
    #clica em documentos publicos
    auto.click(x=626, y=413)
    #clica em empresas com movimento
    auto.click(x=646, y=375)
    #clica na pasta de destino
    auto.click(x=703, y=321)
    #clica em ok
    auto.click(x=707, y=528)
    #clica em salvar
    auto.click(x=820, y=404)
    #clica em ok
    auto.click(x=692, y=392)
    #novamente
    auto.click(x=684, y=397)
    #e de novo
    auto.click(x=681, y=431)
    #clica em analitico grf
    auto.click(x=406, y=69)
    #clica em gerar pdf
    auto.click(x=871, y=508)
    #clica em documents
    auto.click(x=599, y=348)
    #clica em subir
    auto.click(x=813, y=301)
    #clica em empresas cm
    auto.click(x=633, y=363)
    #clica na pasta de destino
    auto.click(x=623, y=377)
    #clica em ok
    auto.click(x=682, y=512)
    # clica em processo finalizado com sucesso
    auto.click(x=682, y=420)
    #clica em fechar
    auto.click(x=938, y=510)
    #clica em relação de trabalhadores
    auto.click(x=427, y=149)
    #clica em gerar pdf
    auto.click(x=813, y=536)
    #clica em ok
    auto.click(x=688, y=510)
    #clica em processo finalizado com sucesso
    auto.click(x=682, y=420)
    #clica em fechar
    auto.click(x=898, y=537)
    #clica em comprovante de pagamento da previdencia
    auto.click(x=452, y=224)
    #clica em gerar pdf
    auto.click(x=868, y=505)
    #clica em ok
    auto.click(x=683, y=507)
    #clica em processo finalizado com sucesso
    auto.click(x=682, y=420)
    #clica em fechar
    auto.click(x=941, y=508)
    #clica em gps
    auto.click(x=432, y=240)
    #clica em gerar pdf
    auto.click(x=868, y=526)
    #clica em ok
    auto.click(x=683, y=509)
    #clica em processo finalizado com sucesso
    auto.click(x=682, y=420)
    #clica em fechar
    auto.click(x=940, y=524)
    #clica em analatico de gps
    auto.click(x=413, y=296)
    #clica em gerar pdf
    auto.click(x=726, y=417)
    #clica em ok
    auto.click(x=685, y=508)
    #clica em processo finalizado com sucesso
    auto.click(x=680, y=418)

def myClick5():

    if datetime.today().day < 10 and datetime.today().month >=10:
        data_em_texto = (f'0{datetime.today().day}/{datetime.today().month}/{datetime.today().year}')
    elif datetime.today().month < 10 and datetime.today().day >= 10:
        data_em_texto = (f'{datetime.today().day}/0{datetime.today().month}/{datetime.today().year}')
    elif datetime.today().day < 10 and datetime.today().month < 10:
        data_em_texto = (f'0{datetime.today().day}/0{datetime.today().month}/{datetime.today().year}')
    else:
        data_em_texto = (f'{datetime.today().day}/{datetime.today().month}/{datetime.today().year}')
    now = datetime.now()
    minuto = now.minute + 27
    if minuto >= 60 and minuto - 60 < 10 and now.second < 10:
        horario = (f'{now.hour + 1}:0{minuto - 60}:0{now.second}')
    elif minuto >= 60 and now.second < 10:
        horario = (f'{now.hour + 1}:{minuto - 60}:0{now.second}')
    elif minuto <= 60 and now.second < 10:
        horario = (f'{now.hour}:{minuto}:0{now.second}')
    elif minuto >= 60 and minuto - 60 < 10 and now.second >= 10:
        horario = (f'{now.hour + 1}:0{minuto - 60}:{now.second}')
    elif minuto >= 60 and minuto - 60 >= 10 and now.second >= 10:
        horario = (f'{now.hour + 1}:{minuto - 60}:{now.second}')
    elif minuto >= 60 and minuto - 60 >= 10 and now.second < 10:
        horario = (f'{now.hour + 1}:{minuto - 60}:0{now.second}')
    else:
        horario = (f'{now.hour}:{minuto}:{now.second}')
    auto.PAUSE = 3
    sleep(1)
    #clica na pasta
    auto.click(x=420, y=743)

    #clica na barra de diretorios
    auto.click(x=884, y=154)

    #escreve o diretorio
    auto.write('C:\\Users\\user\\Documents\\Desktop\\Trabalho\\Comprovantes')

    #enter
    auto.press('enter')

    #clica comprovante de pagamento
    auto.click(x=229, y=267, clicks=2)
    sleep(10)

    #clica no pdf
    auto.click(x=466, y=744)

    #clica na primeira linha
    auto.click(x=94, y=369)
    auto.click(x=97, y=369, clicks=3)

    #copia a linha
    auto.hotkey('ctrl', 'c')

    #muda de pagina
    auto.hotkey('alt', 'tab')
    #clica na primeira linha do comprovante
    auto.click(x=622, y=302)
    auto.hotkey('ctrl', 'v')
    #volta para a pagina pdf
    auto.hotkey('alt', 'tab')
    #desce a pagina
    auto.click(x=1046, y=717, clicks=2)
    #copia o codigo de barras
    auto.click(x=174, y=700, clicks=3)
    auto.hotkey('ctrl', 'c')
    #volta para o comprovante
    auto.hotkey('alt', 'tab')
    #clica na segunda linha do comprovante
    auto.click(x=608, y=329)
    #cola o codigo
    auto.hotkey('ctrl', 'v')
    #volta para o pdf
    auto.hotkey('alt', 'tab')
    #clica no cnpj
    auto.click(x=499, y=464, clicks=3)
    #copia o cnpj
    auto.hotkey('ctrl', 'c')
    #volta para o comprovante
    auto.hotkey('alt', 'tab')
    #clica na terceira linha do comprovante
    auto.click(x=608, y=354)
    #cola a informação
    auto.hotkey('ctrl', 'v')
    #desce para a linha de competencia
    auto.press('tab')
    #escreve a data de vencimento
    if datetime.today().day < 7 and datetime.today().month < 10:
        auto.write(f'07/0{datetime.today().month}/{datetime.today().year }')
    elif datetime.today().day < 7 and datetime.today().month > 10:
        auto.write(f'07/{datetime.today().month}/{datetime.today().year}')
    elif datetime.today().month < 10:
        auto.write(f'07/0{datetime.today().month + 1}/{datetime.today().year}')
    else:
        auto.write(f'07/{datetime.today().month}/{datetime.today().year}')    #desce para a linha de vencimento
    auto.press('tab')
    #escreve a competencia
    if datetime.today().day < 7 and datetime.today().month < 10:
        auto.write(f'0{datetime.today().month - 1}/{datetime.today().year}')
    elif datetime.today().day < 7 and datetime.today().month > 10:
        auto.write(f'{datetime.today().month - 1}/{datetime.today().year}')
    elif datetime.today().month < 10:
        auto.write(f'0{datetime.today().month}/{datetime.today().year}')
    else:
        auto.write(f'{datetime.today().month}/{datetime.today().year}')
    #volta para o pdf
    auto.hotkey('alt', 'tab')
    #seleciona o valor
    auto.click(x=427, y=549, clicks=2)
    #copia o valor
    auto.hotkey('ctrl', 'c')
    #muda para o comprovante
    auto.hotkey('alt', 'tab')
    #clica na linha de valor
    auto.click(x=616, y=434)
    #cola o valor
    auto.hotkey('ctrl', 'v')
    #desce uma linha
    auto.press('tab')
    #cola a data
    auto.write(data_em_texto)
    # desce uma linha
    auto.press('tab')
    #põe o horario
    auto.write(horario)
    #clica em enviar
    auto.click(x=493, y=515)
    #abre o chrome
    web = webdriver.Chrome()
    web.get('https://www.ilovepdf.com/pt/word_para_pdf')
    #maximiza janela
    auto.hotkey('win', 'up')
    #clica para abrir os arquivos
    abrir = web.find_element_by_xpath('//*[@id="pickfiles"]')
    abrir.click()
    sleep(2)

    #clica na barra de diretorios
    auto.click(x=375, y=49)

    #escreve o diretorio
    auto.write('C:\\Users\\user\\Documents\\Desktop\\Trabalho\\Comprovantes')
    #dá enter
    auto.press('enter')
    #clica no documento
    auto.click(x=255, y=144)
    #clica em abrir
    auto.click(x=506, y=686)
    #clica em converter em pdf
    converter = web.find_element_by_xpath('//*[@id="processTask"]')
    converter.click()
    #baixar o arquivo
    baixar = web.find_element_by_xpath('//*[@id="pickfiles"]')
    baixar.click()


def myClick6():
    cnpjdata = cnpj.get()
    global razaodata
    razaodata = razao.get()
    logdata = log.get()
    bairrodata = bairro.get()
    cepdata = cep.get()
    global cidadedata
    cidadedata = cidade.get()
    ufdata = uf.get()
    ddddata = ddd.get()
    teldata = tel.get()
    cnaedata = cnae.get()

    if con.is_connected() and cnpjdata is not None and razaodata is not None and logdata is not None and bairrodata\
        is not None and cepdata is not None and cidadedata is not None and ufdata is not None and ddddata is not None\
        and teldata is not None and cnaedata is not None:
        cursor.execute(f"insert into empresas values ('{cnpjdata}', '{razaodata}', '{logdata}', '{bairrodata}', '{cidadedata}',\
        '{cepdata}', '{ufdata}', '{ddddata}', '{teldata}', '{cnaedata}');")
        con.commit()




#------------------------------------------------------------------------------------------------------------------
#janela2
def Funcionario():
    def Size(*args):
        logvalue = logValue.get()
        bairrovalue = bairroValue.get()
        cityvalue = cityValue.get()
        cepvalue = cepValue.get()
        if len(logvalue) > 49: logValue.set(logvalue[:49])
        if len(bairrovalue) > 19: bairroValue.set(bairrovalue[:19])
        if len(cityvalue) > 19: cityValue.set(cityvalue[:19])
        if len(cepvalue) > 8: cepValue.set(cepvalue[:8])

    logValue = StringVar()
    logValue.trace('w', Size)

    bairroValue = StringVar()
    bairroValue.trace('w', Size)

    cityValue = StringVar()
    cityValue.trace('w', Size)

    cepValue = StringVar()
    cepValue.trace('w', Size)


    janela2 = Tk()
    janela2.geometry('550x300')
    #empresa
    emptxt = Label(janela2, text='Empresa')
    emptxt.place(x=0, y=0)
    emp = Entry(janela2, width=38)
    emp.place(x=80, y=0)

    # Nome da pessoa
    nometxt = Label(janela2, text='Nome')
    nometxt.place(x=0, y=25)
    nome = Entry(janela2, width=40)
    nome.place(x=80, y=25)

    # Data de nascimento da pessoa
    nasctext = Label(janela2, text='D.Nascimento')
    nasctext.place(x=0, y=50)

    nasc = Entry(janela2, width=10)
    nasc.place(x=80, y=50)

    # CPF da pessoa
    cpftxt = Label(janela2, text='CPF')
    cpftxt.place(x=0, y=80)

    cpf = Entry(janela2, width=15)
    cpf.place(x=80, y=80)

    logtxt2 = Label(janela2, text='Logradouro')
    logtxt2.place(x=0, y=105)

    log2 = Entry(janela2, width=45, textvariable=logValue)
    log2.place(x=80, y=105)

    # Bairro
    bairrotxt2 = Label(janela2, text='Bairro')
    bairrotxt2.place(x=0, y=130)

    bairro2 = Entry(janela2, width=25, textvariable=bairroValue)
    bairro2.place(x=80, y=130)

    # cep
    ceptxt2 = Label(janela2, text='CEP')
    ceptxt2.place(x=235, y=130)

    cep2 = Entry(janela2, width=15, textvariable=cepValue)
    cep2.place(x=260, y=130)

    # cidade
    cidadetxt2 = Label(janela2, text='Cidade')
    cidadetxt2.place(x=0, y=155)

    cidade2 = Entry(janela2, width=25, textvariable=cityValue)
    cidade2.place(x=80, y=155)

    # UF
    uftxt2 = Label(janela2, text='UF')
    uftxt2.place(x=235, y=155)

    uf2 = Entry(janela2, width=15)
    uf2.place(x=260, y=155)

    #cbo
    cbotext = Label(janela2, text='CBO')
    cbotext.place(x=0, y=180)

    cbo = Entry(janela2, width = 6)
    cbo.place(x=80, y=180)

    def myClick2():
        dataname = nome.get()
        datanasc = nasc.get()
        global datacpf
        datacpf = cpf.get()
        datalog = log2.get()
        databairro = bairro2.get()
        datacep = cep2.get()
        datacidade = cidade2.get()
        datauf = uf2.get()
        aleatorio = randint(1000000, 9999999)

        auto.PAUSE = 3

        sleep(1)


        pyper.copy(dataname)
        #clica no chrome
        auto.click(x=469, y=751)
        #abre nova aba
        auto.hotkey('ctrl', 't')
        #escreve o site
        auto.write('cnisnet.inss.gov.br')
        #entra no site
        auto.press('enter')
        sleep(5)
        #clica em cidadao
        auto.click(x=200, y=293)
        sleep(5)
        #clica em inscrição
        auto.click(x=47, y=158)
        sleep(5)
        #clica em filiado
        auto.click(x=45, y=188)
        sleep(5)
        #cola o nome
        sleep(5)
        auto.hotkey('ctrl', 'v')
        #clica no campo para desmarcar a mãe
        auto.click(x=822, y=403)
        #clica no campo de nascimento
        auto.click(x=271, y=439)
        #escreve a data do nascimento
        auto.write(datanasc)
        #vai no campo de cpf
        auto.press('tab')
        auto.press('tab')
        #escreve cpf
        auto.write(datacpf)
        sleep(3)
        #nao sou um robo
        auto.click(x=292, y=541)
        sleep(15)
        #click em continuar
        auto.click(x=303, y=606)
        sleep(3)
        #clicar no PIS
        auto.click(x=836, y=381, clicks=2)
        #copiar o PIS
        auto.hotkey('ctrl', 'c')
        global pis
        pis = pyper.paste()
        #vai para o sefip novamente
        auto.keyDown('alt')
        auto.hotkey('tab', 'tab', 'tab')
        auto.keyUp('alt')

        #cola o pis
        if len(pis) == 11:
            auto.write(pis)
        else:
            web = webdriver.Chrome()
            web.get('https://www.4devs.com.br/gerador_de_pis_pasep')
            auto.hotkey('win', 'up')
            # clica para número sem pontos
            auto.click(x=457, y=435)
            global alepis
            alepis = pyper.paste()
            while True:
                if alepis[0] == '1' or alepis[0] == '2':
                    break
                else:
                    #click para gerar o pis
                    auto.click(x=798, y=464)
                    #clica em cima do pis
                    auto.click(x=785, y=573, clicks=2)
                    auto.hotkey('ctrl', 'c')
                    alepis = pyper.paste()
            auto.hotkey('alt', 'tab')
            auto.write(alepis)
        #vai para o nome
        auto.press('tab')
        #escreve o nome
        auto.write(dataname)
        #vai para categoria
        auto.press('tab')
        #escreve 0
        auto.press('0')
        #seleciona a categoria
        auto.press('enter')
        #vai para o logradouro
        auto.press('tab')
        #insere o nome da rua
        auto.write(datalog)
        #vai para bairro
        auto.press('tab')
        #escreve bairro
        auto.write(databairro)
        #vai para o cep
        if len(databairro) < 20:
            auto.press('tab')
        #escreve o cep
        auto.write(datacep)
        #nome da cidade
        auto.write(datacidade)
        #vai para uf
        if len(datacidade) < 20:
            auto.press('tab')
        #escreve a uf
        auto.write(datauf)
        #confirma uf
        auto.press('enter')
        #vai para o cbo
        auto.click(x=307, y=353)
        #escreve o cbo
        auto.write('04211')
        #clica no cbo
        auto.click(x=325, y=366)
        #vai pro ctps
        auto.press('tab')
        #escreve o ctps
        auto.write(str(aleatorio))
        #escreve a série
        auto.write(datacpf[-4:])
        #escreve a ocorrencia
        auto.click(x=1191, y=371)
        #seleciona a ocorrencia
        auto.click(x=701, y=390)
        #vai para a data de nascimento
        auto.press('tab')
        #escreve a data de nascimento
        auto.write(datanasc)
        #aperta tab
        auto.press('tab')
        #escreve a data de contratação
        if datetime.today().day < 7 and datetime.today().month < 10:
            auto.write(f'010{datetime.today().month - 1}{datetime.today().year}')
        elif datetime.today().day < 7 and datetime.today().month > 10:
            auto.write(f'01{datetime.today().month - 1}{datetime.today().year}')
        elif datetime.today().month < 10:
            auto.write(f'010{datetime.today().month}{datetime.today().year}')
        else:
            auto.write(f'01{datetime.today().month}{datetime.today().year}')
        #coloca novamente a competencia
        auto.press('tab')
        #clica em salvar
        auto.click(x=1236, y=690)
        #confirma ok
        auto.click(x=641, y=418)


    Botaojanela2 = Button(janela2, text='Coleta', command=myClick2)
    Botaojanela2.place(x=300, y=200)

    def myClick3():
        auto.PAUSE = 2
        sleep(1)
        # clica em movimento
        auto.click(x=181, y=84)
        # clica em novo
        auto.click(x=1027, y=688)
        # escreve a competencia
        if datetime.today().day < 7 and datetime.today().month < 10:
            auto.write(f'0{datetime.today().month - 1}{datetime.today().year}')
        elif datetime.today().day < 7 and datetime.today().month > 10:
            auto.write(f'{datetime.today().month - 1}{datetime.today().year}')
        elif datetime.today().month < 10:
            auto.write(f'0{datetime.today().month}{datetime.today().year}')
        else:
            auto.write(f'{datetime.today().month}{datetime.today().year}')
        # vai para codigo de recolhimento
        auto.press('tab')
        # escreve o codigo de recolhimento
        auto.write('1')
        #clica no codigo de recolhimento
        auto.click(x=559, y=172)
        # clica em salvar
        auto.click(x=1227, y=689)
        # clica em confirma
        auto.click(x=641, y=418)
        auto.click(x=680, y=423)
        # clicla no binoculos
        auto.click(x=198, y=60)
        # escreve a empresa que quer achar
        auto.write(razaodata)
        # clica em localizar
        auto.click(x=946, y=239)
        # clica na empresa que foi incluída
        auto.click(x=534, y=380, clicks=2)
        # clica em fechar
        auto.click(x=957, y=272)
        # clica em marcar
        auto.click(x=91, y=58)
        # clica em dados do movimento
        auto.click(x=1154, y=692)
        # aperta 0
        auto.press('0')
        #vai para a parte seguinte
        auto.press('tab')
        # aperta 2
        auto.press('2')
        # clica na segunda opção
        auto.click(x=664, y=232)
        # vai para a linha de baixo
        auto.press('tab')
        # escreve 1
        auto.write('1')
        # clica em salvar
        auto.click(x=1229, y=689)

    def myClick7():
        if pis is not None:
            pisdata = pis
        else:
            pisdata = alepis
        empdata = emp.get()
        dataname = nome.get()
        datanasc = nasc.get()
        datacpf = cpf.get()
        datalog = log2.get()
        databairro = bairro2.get()
        datacep = cep2.get()
        datacidade = cidade2.get()
        datauf = uf2.get()
        if cbo.get() == '':
            datacbo = '04211'
        else:
            datacbo = cbo.get()
        nasc_ano = datanasc[-4:]
        nasc_mes = datanasc[2:4]
        nasc_dia = datanasc[0:2]
        if datetime.today().day < 7 and datetime.today().month < 10:
            contratacao = (f'{datetime.today().year}-0{datetime.today().month - 1}-01')
        elif datetime.today().day < 7 and datetime.today().month > 10:
            contratacao =(f'{datetime.today().year}-{datetime.today().month - 1}-01')
        elif datetime.today().month < 10:
            contratacao = (f'{datetime.today().year}-0{datetime.today().month}-01')
        else:
            contratacao = (f'{datetime.today().year}-{datetime.today().month}-01')

        sleep(3)

        if con.is_connected() and pisdata is not None and empdata is not None and dataname is not None and datalog \
            is not None and databairro is not None and datacep is not None and datacidade is not None and datauf is not None\
            and datanasc is not None:
            cursor.execute(f"insert into titulares values ('{pisdata}', '{empdata}', '{dataname}', '{datalog}', '{databairro}',\
            '{datacidade}', '{datacep}', '{datauf}', '{datacbo}', '{nasc_ano}-{nasc_mes}-{nasc_dia}', '{contratacao}', '{datacpf[-4:]}')")
            con.commit()
        else:
            print('O servidor MySQL não está conectado, ou algum campo está vázio.')

    Botao2Janela2 = Button(janela2, text='Novo movimento', command=myClick3)
    Botao2Janela2.place(x=350, y=200)

    Botao3Janela2 = Button(janela2, text='Dados', command=myClick7)
    Botao3Janela2.place(x=460, y=200)



#botoes da janela1
Botao = Button(janela1, text='Coleta', command=myClick)
Botao.place(x=200, y=270)

Botao2 = Button(janela1, text='Funcionario', command=Funcionario)
Botao2.place(x=250, y=270)

Botao3 = Button(janela1, text='Executar', command=myClick4)
Botao3.place(x=330, y=270)

Botao4 = Button(janela1, text='Finalizar', command=myClick5)
Botao4.place(x=400, y=270)

Botao5 = Button(janela1, text='Dados', command=myClick6)
Botao5.place(x=470, y=270)

janela1.mainloop()



