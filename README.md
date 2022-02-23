# Busca Médico

![Lincença do projeto](	https://img.shields.io/github/license/robsonleal/pedroreceitas)
![Bagde status desenvolvimento](https://img.shields.io/static/v1?label=status&message=CONCLUÍDO&color=green)

## Índice

* [Título](#Título)
* [Badges](#badges)
* [Índice](#índice)
* [Descrição do Projeto](#descrição-do-projeto)
* [Funcionalidades e Demonstração da Aplicação](#funcionalidades-e-demonstração-da-aplicação)
* [Acesso ao Projeto](#acesso-ao-projeto)
* [Tecnologias utilizadas](#tecnologias-utilizadas)

## Descrição do Projeto

Aplicação web para consulta de médicos. 

Ela permitirá que usuários consultem os médicos mais próximos de sua localidade ou uma localidade específica, podendo filtrá-los por nome, especialidade, estado, cidade e bairro do médico. 
 
Veremos no Django como criar um painel administrativo para a aplicação, além da criação de telas HTML também usando a tecnologia de templates do Django.

## Funcionalidades e Demonstração da Aplicação
- `Funcionalidade 1`: Login de usuário cadastrado;
- `Funcionalidade 2`: Cadastrado de novos usuários;
- `Funcionalidade 3`: Busca por médicos cadastrados (por nome e outros filtros);
- `Funcionalidade 4`: Adicionar/remover médicos dos favoritos;
- `Funcionalidade 5`: Avaliar médico;
- `Funcionalidade 6`: Editar perfil do usuário cadastrado;

Pagina de login da aplicação: </br>
![Screenshot_20220223_163637](https://user-images.githubusercontent.com/27708175/155396054-9149e514-f0f2-438b-950b-bf53b8f95d30.png)

Página de busca da aplicação: </br>
![Screenshot_20220223_163706](https://user-images.githubusercontent.com/27708175/155396129-e07bdadf-e0d9-4a42-b81a-281e125f4a1a.png)

Página de perfil do usuário de está logado na aplicação: </br>
![Screenshot_20220223_164301](https://user-images.githubusercontent.com/27708175/155396150-f806fb76-b62c-4a61-a181-a0154a2e5f3e.png)

Página de edição do perfil do usuário que está logado na aplicação: </br>
![Screenshot_20220223_164405](https://user-images.githubusercontent.com/27708175/155396195-855d40a1-b1e7-4195-909c-058e983e2990.png)

Página de perfil de um médico cadastrado na aplicação: </br>
![Screenshot_20220223_164342](https://user-images.githubusercontent.com/27708175/155396159-10a625f7-3f71-4ae8-9375-338ecbc6f7b9.png)


## Acesso ao Projeto

Deploy - https://dashboard.heroku.com/apps/medic-search

```console
git clone git@github.com:robsonleal/medic_search.git
cd medic_search
python -m venv ./venv
source venv/bin/activate
pip install -r 'requirements.txt'
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
- Abrir o endereço localhost:8000 no navegador de sua preferência;

## Tecnologias utilizadas
`Django 4`
`Python 3`
`PostgreSQL`
`Heroku`
