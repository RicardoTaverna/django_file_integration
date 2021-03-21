<h1 align="center">
    <img alt="Django File Integration" title="Django File Integration" src="src\static\images\django.PNG" width="50%"/>
    
</h1>
<h2 align="center">Django File Integration</h2>

<p align="center">App que realiza o carregamento de aruivos, tratamentos dos dados e direcionada o envio de cada mensagem carregada para seu respectivo broker.</p>

<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/RicardoTaverna/django_file_integration?color=%2304D361&style=for-the-badge">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/RicardoTaverna/django_file_integration?style=for-the-badge">
  
  <a href="https://github.com/RicardoTaverna/django_file_integration/commits/main">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/RicardoTaverna/django_file_integration?color=%2304D361&style=for-the-badge">
  </a>

  <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen?color=%2304D361&style=for-the-badge">
   <a href="https://github.com/RicardoTaverna/django_file_integration/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/RicardoTaverna/django_file_integration?style=for-the-badge">
  </a>

  <img alt="Repository Issues" src="https://img.shields.io/github/issues/RicardoTaverna/django_file_integration?color=%2304D361&style=for-the-badge">
</p>


Tabela de conteúdos
=================
<!--ts-->
   * [Sobre](#Sobre)
   * [Tabela de Conteudo](#tabela-de-conteudo)
   * [Tecnologias](#tecnologias)
   * [Executar projeto](#executar-projeto)
        * [Pré-requisitos](#pré-requisitos)
        * [Execução](#execução)
   * [Como usar](#como-usar)
   * [Tests](#testes)

<!--te-->

## 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- <img src="https://simple-icons.github.io/simple-icons-website/icons/django.svg" width=13> [Django](https://www.djangoproject.com)
- <img src="https://simple-icons.github.io/simple-icons-website/icons/python.svg" width=13> [Python](https://www.python.org)

## 🚀 Executar projeto

Para executar esse pojeto você precisa de alguns pré-requisitos

### Pré-requisitos
Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Python](https://www.python.org). 
Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/).

### Execução
- pip install -r requirements.txt
- cd src
- docker-compose up -d
- python manage.py makemigrations
- python manage.py migrate
- python manage.py loaddata firstdata.json
- python manage.py runserver

## Testes
- coverage run --source='.' manage.py test integration