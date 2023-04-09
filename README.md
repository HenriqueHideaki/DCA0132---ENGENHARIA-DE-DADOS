# DCA0132 - Engenharia de Dados - Atividade 2 - Prática com Docker Compose
Esta prática consiste na criação de arquivos Docker Compose para a execução automática de containers Docker.
O objetivo desta prática é criar um arquivo YAML (docker-compose.yml), onde serão criados 3 containers, sendo um destes containers um Servidor TCP e os demais sendo Clientes TCP. Os scripts Cliente e Servidor devem ser baixados em:
[https://www.dca.ufrn.br/~viegas/disciplinas/DCA0132/files/Sockets/](https://www.dca.ufrn.br/~viegas/disciplinas/DCA0132/files/Sockets/)
### Objetivos
* Criar as imagens referentes ao ServidorTCP e ClienteTCP a partir de Dockerfile.
* Criar um arquivo YAML (docker-compose.yml) que execute as 3 aplicações, sendo um servidor e dois clientes. Cada cliente irá enviar uma mensagem para o servidor.
#### Exemplo de docker-compose.yml para iniciar
````Docker
# Indica a versão do Docker Compose que será utilizada
version: '3.9'
# Serviços que serão executados nos containers
services:
# Nome do serviço a ser criado
servidor:
# Nome do container que será executado
container_name: <nome-do-container>
# Imagem que será executada no container
# A imagem é obtida localmente ou a partir do Dockerhub
image: <nome-do-usuario-dockerhub>/<nome-do-repositorio:tag>
# Permite a exibição de texto na tela do terminal
tty: true
...
# Nome do segundo serviço a ser criado
cliente:
container_name: <nome-do-container>
# O depends_on faz com que este serviço seja executado após outro
depends_on:
- servidor
image: <nome-do-usuario-dockerhub>/<nome-do-repositorio:tag>
tty: true
# Quando o container terminar a sua execução, sempre irá reiniciar
restart: always
...
# Nome do terceiro serviço a ser criado
cliente2:
container_name: <nome-do-container>
# O depends_on faz com que este serviço seja executado após outro
depends_on:
- servidor
- cliente
image: <nome-do-usuario-dockerhub>/<nome-do-repositorio:tag>
tty: true
restart: always
...
````

#### Para execução da atividade

Para criar uma nova rede Docker "my-network" e inspeciona-la, execute:  
````shell
$ docker network create -d bridge my-network
$ docker inspect my-network
````

````
"IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "172.19.0.0/16",
                    "Gateway": "172.19.0.1"
                }
            ]
        },
````
Qualquer container que se conectar a esta rede obterá um IP padrão no intervalo de 172.19.0.1 a 172.18.255.254 .

Para executar a aplicação:

````
$ docker compose up
````
Saída:

![](\approdando.png)

Para parar a aplicação: 

````
$ docker compose down
````
Saída:
![](\dockercomposedown.png)