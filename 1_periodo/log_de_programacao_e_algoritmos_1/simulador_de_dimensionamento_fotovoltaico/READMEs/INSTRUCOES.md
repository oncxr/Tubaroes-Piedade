# Instruções

Esse arquivo contém as tarefas que deverão ser executadas por cada membro do grupo.  

Cada pessoa será responsável por um arquivo, sendo eles:

* **main.py** (Arthur)
* **crm.py** (Carlos)
* **motor_solar.py** (Vitor)
* **catalogo_poo.py** (Antônio)
* **proposta.py** (Juan)

O workflow será da seguinte forma:

```txt
  Vitor─┐
        ├─Carlos──Arthur
Antonio─┘            │
                Juan─┘
```

**OBS.: Caso você não tenha tarefas para a milestone 1, pode ficar tranquilo, não precisa fazer.**

## 1. main.py (Arthur)

Vai juntar tudo no `main.py`, vai pegar as funções de outros arquivos e chamar eles na ordem certa.

### Tarefas (Arthur)

#### Milestone 1 (Arthur)

~~1. Chama `crm.py` para coletar nome, consumo médio e HSP~~  
~~2. Recebe a potência do painel manualmente (ex.: O usuário digita 500 para 500W)~~  
~~3. Chama as funções do `motor_solar` com os dados coletados~~  
~~4. Calcula custo total e payback~~  
~~5. Imprime os resultados direto no terminal (sem proposta formatada ainda)~~  

#### Milestone 2 (Arthur)

1. Mostra o catálogo do `catalogo_poo` e deixa o usuário escolher o painel, inversor e bateria pelo número
2. Pergunta se é On-Grid ou Off-Grid e redireciona o fluxo
3. Se Off-Grid, chama o cálculo de baterias do `motor_solar`
4. Chama o `proposta.py` para imprimir o ticket final formatado

## 2. crm.py (Carlos)

Vai criar o formulário com as perguntas pro usuário responder.

### Tarefas (Carlos)

#### Milestone 1 (Carlos)

~~1. Pede o nome do cliente~~  
~~2. Pede o consumo dos 12 meses um por um usando `for`, recusando qualquer valor negativo~~  
~~3. Calcula a média dos 12 meses automaticamente~~  
~~4. Pede o HSP da cidade e recusa valor zero ou negativo (evita divisão por zero no motor_solar)~~  

#### Milestone 2 (Carlos)

1. Pergunta se o sistema é On-Grid ou Off-Grid
2. Se Off-Grid, pede a autonomia em dias e a tensão do sistema (ex.: 24V ou 48V)

## 3. motor_solar.py (Vitor)

Vai criar todas as funções de cálculo do sistema.

### Tarefas (Vitor)

#### Milestone 1 (Vitor)

~~1. Função que calcula o consumo diário (`consumo_mensal/30`)~~  
~~2. Função que calcula o kWp (`consumo_diário / (HSP * 0.80)`), com proteção contra divisão por zero~~  
~~3. Função que calcula a quantidade de painéis e arredonda pra cima sem usar bibliotecas (int() + lógica manual)~~  

#### Milestone 2 (Vitor)

1. Função que calcula o banco de baterias em Ah (`(consumo_diario * 1000 * autonomia) / (tensao * 0.80)`)

## 4. catalogo_poo.py (Antônio)

Vai criar os produtos que o cliente pode escolher

### Tarefas (Antônio)

#### Milestone 1 (Antônio)

Nenhuma entrega, não é exigido na Milestone 1

#### Milestone 2 (Antônio)

1. Criar a classe `PainelSolar` com atributos `modelo`, `potencia_kw` e `preco`
2. Criar a classe `Inversor` com atributos `modelo`, `potencia_kw` e `preco`
3. Criar a classe `Bateria` com atributos `modelo`, `capacidade_ah`, `tensao_v` e `preco`
4. Cirar listas com 2 ou 3 objetod de cada classe pra o usuário escolher pelo número
5. Garantir que os atributos seguem o padrão que o main.py e o motor_solar esperam (ex.: `painel`, `potencia_kw`, `painel_preco`)

## 5. proposta.py (Juan)

Vai pegar todos os resultados e imprimir o recibo final no terminal.

### Tarefas (Juan)

#### Milestone 1 (Juan)

Nenhuma entrega, não é exigido na Milestone 1

#### Milestone 2 (Juan)

1. Recebe todos os dados calculados como parâmetro (nome, tipo, kWp, painéis, custos, payback)
2. Imprime nome do cliente e tipo do sistema (On-Grid / Off-Grid)
3. Imprime quantidade de painéis e kWp calculado
4. Imprime o custo total de cada item separado (painéis, inversor, mão de obra) e o total geral
5. Imprime a economia mensal e o payback em meses
6. Toda a formtação usa alinhamento de colunas com f-strings (`f"{texto:<20}"`) no estilo ticket impresso
