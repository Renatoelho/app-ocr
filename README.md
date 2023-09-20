
# Aplicação Web para conversão de imagens em texto

![Streamlit e Tesseract](https://drive.google.com/uc?export=view&id=12V733jQZavjJFfvKxn1ia-KrraINi3H3)

Este projeto utiliza o poder e a facilidade de criação de aplicativos do Streamlit, juntamente com a versatilidade do Tesseract na conversão de imagens em texto (OCR). É uma aplicação muito simples, onde você faz o upload de uma imagem que contém textos e, em seguida, é disponibilizado para download um arquivo de texto com o conteúdo da imagem original.

[![Tesseract](https://img.shields.io/badge/Tesseract-4.1.1-E3E3E3)](https://github.com/tesseract-ocr/tesseract)
[![Pytesseract](https://img.shields.io/badge/Pytesseract-0.3.10-E3E3E3)](https://pypi.org/project/pytesseract/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.23.1-E3E3E3)](https://docs.streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8-E3E3E3)](https://www.python.org/downloads/release/python-3810/)


### Requisitos

+ ![Docker](https://img.shields.io/badge/Docker-23.0.3-E3E3E3)

+ ![Docker-compose](https://img.shields.io/badge/Docker--compose-1.25.0-E3E3E3)

+ ![Git](https://img.shields.io/badge/Git-2.25.1%2B-E3E3E3)

+ ![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04-E3E3E3)

# Implantação

Existem duas formas de construir a imagem da sua aplicação. A primeira é executar o build através do comando ```docker build```, que requer dois passos para ativar a sua aplicação. A outra é realizar o build diretamente pelo Docker Compose, onde, em um único passo, você constrói e ativa a sua aplicação. Essas são as duas abordagens existentes:

### Abordagem com Docker Build + Docker Compose

+ Clonando o repositório:

```bash
git clone https://github.com/Renatoelho/app-ocr.git app-ocr
```

+ Acessando o repositório:

```bash
cd app-ocr/
```

+ Fazendo o Build da imagem da aplicação

```bash
docker build -f dockerfile -t app-ocr:0.0.1 .
```

+ Ativando a aplicação:

```bash
docker compose -p app_ocr -f docker-compose-abor-1.yaml up -d
```

> Tecnicamente, a diferença entre as duas abordagens está na ausência das linhas 5, 6 e 7 do arquivo [docker-compose-abor-2.yaml](/docker-compose-abor-2.yaml) em relação ao [docker-compose-abor-1.yaml](/docker-compose-abor-1.yaml). Já na segunda abordagem, essas linhas são fundamentais para que não seja necessário executar o comando ```docker build```.


### Abordagem somente com Docker Compose (mais objetiva)

+ Clonando o repositório:

```bash
git clone https://github.com/Renatoelho/app-ocr.git app-ocr
```

+ Acessando o repositório:

```bash
cd app-ocr/
```

+ Ativando a aplicação (1ª ativação):

```bash
docker compose -p app_ocr -f docker-compose-abor-2.yaml up -d --build
```

+ Ativando a aplicação (demais ativações):

```bash
docker compose -p app_ocr -f docker-compose-abor-2.yaml up -d
```


### Acessando a aplicação

Se a implantação for feita com sucesso, é só acessar a seguinte URL [http://localhost:8000](http://localhost:8000) que a aplicação já estará em execução.

![App OCR Web](https://drive.google.com/uc?export=view&id=1h9Ox5j87eZwRjaorwne4id2qhO1L1zy5)

### Desativando aplicação:

Na desativação da aplicação, ambas as abordagens exigem apenas um único passo. 

+ Abordagem com Docker Build + Docker Compose

```bash
docker compose -p app_ocr -f docker-compose-abor-1.yaml down
```

+ Abordagem somente com Docker Compose

```bash
docker compose -p app_ocr -f docker-compose-abor-2.yaml down
```


# Referências

Tesseract OCR, ***Tesseract***. Disponível em: <https://github.com/tesseract-ocr/tesseract>. Acesso em: 01 de set. 2023.

Streamlit documentation, ***Streamlit***. Disponível em: <https://docs.streamlit.io/>. Acesso em: 14 jun. 2023.

How to Successfully Implement A Healthcheck In Docker Compose, ***Linuxhint***. Disponível em: <https://linuxhint.com/how-to-successfully-implement-healthcheck-in-docker-compose/>. Acesso em: 24 abr. 2023.

Install Docker Desktop on Ubuntu, ***docs.docker.com***. Disponível em: <https://docs.docker.com/desktop/install/ubuntu/>. Acesso em: 15 de abr. 2023.

The Compose file, ***docs.docker.com***. Disponível em: <https://docs.docker.com/compose/compose-file/03-compose-file/>. Acesso em: 15 de abr. 2023.

Service unit configuration, ***systemd.service***. Disponível em: <https://www.freedesktop.org/software/systemd/man/systemd.service.html>. Acesso em: 05 jun. 2023.
