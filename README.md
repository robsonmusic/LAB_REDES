# LAB_REDES 

## Aluno: Jose Robson

## **Projeto Container**

### 1. O que é Contêiner:
#### Um contêiner ou contentor  é um recipiente padronizado para facilitar o transporte em operações logísticas.  O conceito de contêiner é utilizado analogamente em sistemas computacionais para associar em pacotes de software todos os processos, sistemas de arquivo, bibliotecas e recursos necessários para executar a aplicação em um sistema operacional (SO). 

#### Um contêiner é um processo associado a recursos do SO que é executado isoladamente dos demais contêineres.  Funciona como uma camada de software que virtualiza recursos do SO, mas compartilha o mesmo kernel com os demais contêineres do SO hospedeiro.

#### Quando um contêiner é implantado na nuvem, ou outro hospedeiro, não é necessário reinstalar bibliotecas específicas da aplicação. Todas as bibliotecas necessárias já estão no contêiner.

### 2. O que é Docker:

#### Docker é uma plataforma de virtualização de nível de sistema operacional  para para criação, execução e implantação (deploy) de contêineres. Os contêineres são leves e contêm tudo o que é necessário para executar o aplicativo,.

#### Existem 4 componentes do Docker que são necessários para a compreensão dos comandos da plataforma: docker daemon, imagens, registros e contêineres.

#### Na página do Docker (2021) existe uma documentação sobre a arquitetura de Docker, comandos de gerenciamento e desenvolvimento em linguagens específicas.


### 3. Implementação do Docker:
 * #### Para criar o docker foi implementado um Dockerfile para construir a imagem do servidor python, usando a porta escolhida em aula, que foi a porta 61021.
 * #### o comando usando para gerar a imagem foi "$~ docker build -t servrob ."
 * #### Após criar a imagem usei o comando  "$~ docker run -d -p 61021:61000 -it --rm --name servR servrob "

