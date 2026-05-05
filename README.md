# Tubaroes-Piedade

Grupo formado por 6 pessoas pro curso de ADS na faculdade Universo, com o objetivo de fazer trabalhos.  

Cada periodo contém uma pasta com a matéria e o projeto dedicado.  

## Sincronizando o git
**(OBS.: Talvez necessite fazer o cadastro no git)**

Primeiro, faça um fork desse repositório, lá em cima tem um botão chamado `fork`, clique nele para clonar esse repositório na sua conta pessoal.

Antes de tudo, é preciso colocar esse repositório no seu pc, para isso coloque o comando no terminal:
```sh
git clone https://github.com/SEU_USUARIO/Tubaroes-Piedade
```

Após colocar, abra a pasta do projeto:
```
Tubaroes-Piedade
 └─1_periodo
    └─log_de_programacao_e_algoritmos_1
       └─simulador_de_dimensionamento_fotovoltaico
          └─arquivos .py
```

Depois de abrir o projeto, é necessário atualizar seu repositório local com o repositório remoto, digite esses 4 comandos em sequência:
```sh
git remote add upstream https://github.com/Vit0ncio/Tubaroes-Piedade 
git checkout main
git pull upstream main
git push origin main
```

Caso você já tenha o repositório pronto e configurado no seu computador, mas deseja sincronizar com o repositório do github, use esses comandos:
```sh
git pull upstream main
git push origin main
```
**(OBS: É necessário que você faça isso toda vez que for mexer com o programa)**

Quando você tiver alguma alteração para fazer em algum arquivo e deseja colocar no seu repositório, digite esses comandos:
```sh
git add . # ou git add <nome_arquivo> para um arquivo específico
git commit -m "Mensagem descrevendo o que você fez no código"
git push origin main
```

Depois do push, vá até o GitHub, vá ao repositório que você fez o fork, lá terá um aviso pedindo para você fazer um pull request, junto com um botão verde escrito "Compare & pull request", clique nesse botão e aceite para fazer o pull request que eu irei analisá-lo.
