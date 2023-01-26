##Desafio Back-End - Data Parse de Transações

O projeto é uma especie de banco onde é armazenado as transações e informações do cliente.

Stacks: Python, Django, HTML5, CSS3, JavaScript

Passos para configuração:

Dependências:
pip install -r requirements.txt

Gerar banco de dados local:

python manage.py migrate


Rodar o server

python manage.py runserver


Testar pelo template no endereço http://127.0.0.1:8000/api/


Ou por um API Client como Insomnia em http://127.0.0.1:8000/api/company/

Para GET não enviar body.

Para POST enviar arquivo binary file com content-type text/plain


Dentro do projeto, na pasta assets está um arquivo exemplo.