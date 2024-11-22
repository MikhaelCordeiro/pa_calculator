# Calculadora de Progressão Aritmética (PA)

Este projeto é uma aplicação web desenvolvida com Django para calcular termos e soma de uma **Progressão Aritmética (PA)**. O usuário insere o primeiro termo, a razão e o número de termos, e o sistema retorna a sequência gerada e a soma de todos os termos.

## Funcionalidades

- **Cálculo da sequência da PA**: O usuário fornece o primeiro termo, a razão e o número de termos. A aplicação gera a sequência de termos e a soma total.
- **Interface simples e prática**: Interface responsiva focada em dispositivos móveis, com um design inspirado em calculadoras de celular.
- **Fácil de usar**: Basta preencher os campos de entrada e clicar no botão para calcular a PA.

## Tecnologias Utilizadas

- **Django**: Framework web em Python utilizado para a construção da aplicação.
- **HTML/CSS**: Utilizado para a construção da interface de usuário.
- **Python**: Para as lógicas de cálculo e backend.

## Como Executar Localmente

### Requisitos

- **Python 3.x** ou superior
- **Django** (instalado via pip)
- **Banco de Dados SQLite** (já configurado por padrão)

### Passos

1. Clone o repositório:
   ´´´bash
   git clone https://github.com/SEU_USUARIO/calculadora-pa.git
   cd calculadora-pa

2. Crie e ative um ambiente virtual (recomendado):
  ´´´bash
  python3 -m venv venv
  source venv/bin/activate  # Para Linux/macOS
  venv\Scripts\activate  # Para Windows

3. Instale as dependências:
´´´bash
  pip install -r requirements.txt

4. Realize as migrações do banco de dados:
´´´bash
  python manage.py migrate

5. Inicie o servido:
´´´bash
  python manage.py runserver

6. Acesse a aplicação em:
´´´bash
  http://127.0.0.1:8000/calculadora/.    
