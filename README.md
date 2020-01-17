# Teste Para Z-Tech

Este projeto foi criado para o teste dísponivel em https://github.com/ztech-company/backend-challenge.
O setup foi feito a partir de um boilerplate de Django previamente organizado por mim, disponível em
https://github.com/duiliofelix/django-template. O setup original inclui:

- [Django](https://docs.djangoproject.com/en/2.2/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Docker](https://docs.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- Postgres (Já conectado com Django)
- [Variáveis de ambiente](https://github.com/joke2k/django-environ)
- [CORS middleware](https://pypi.org/project/django-cors-headers/)
- [Django Rest Auth & AllAuth](https://django-rest-auth.readthedocs.io/)
- Módulo responsável por usuários (básico)

O módulo construído para o teste é o `movies`. Nele, estão os testes, rotas, modelos, serializadores e controladores
relevantes, organizados seguindo as convenções de arquivo do Django.

Para facilitar a instalação, mantive nos arquivos o `.env`, que normalmente seria incluído no `.gitignore`.
Além disto, o projeto também está com docker-compose configurado para rodá-lo.

## Instalação
Todos os requesitos de instalação estão no `requirements.txt`, porém, para rodar o projeto utilizando docker, execute:
```
git clone --depth=1 --branch=master https://github.com/duiliofelix/ztech-test
docker-compose build
docker-compose run python manage.py migrate
docker-compose up
```
O container principal está com o nome `web`. Caso haja

## Executando os testes
Para rodar os testes, basta usar:
```
docker-compose run python manage.py test
```
