# 📄 Gerador de Orçamentos em PDF com Flask
-> Você pode acessar a aplicação online clicando aqui: https://joaovianasouza.pythonanywhere.com/

## 📝 Sobre o Projeto
-> Este projeto é uma aplicação web completa desenvolvida em Python com o microframework Flask. A sua principal funcionalidade é permitir que prestadores de serviço criem, preencham e gerem orçamentos profissionais em formato PDF de forma rápida e segura.

Este projeto foi construído como um exercício prático para solidificar conhecimentos em desenvolvimento web com Python, desde a criação da interface até a publicação (deploy) em um servidor online.

## ✨ Funcionalidades
- Autenticação de Usuários: Sistema de login seguro para garantir que apenas usuários autorizados possam criar orçamentos.
- Criação de Orçamentos: Formulário intuitivo para inserir dados do cliente, do prestador de serviço, lista de serviços e materiais.
- Geração de PDF: Conversão automática dos dados do formulário em um documento PDF com layout profissional, pronto para ser impresso ou enviado ao cliente.
- Interface Responsiva: Utilização do Bootstrap 5 para uma experiência agradável em desktops e dispositivos móveis.

## 🚀 Tecnologias Utilizadas
Este projeto foi desenvolvido com as seguintes tecnologias:

Backend:
- Python 3.10
- Flask
- Flask-Login (para autenticação)

Geração de PDF:
- WeasyPrint

Frontend:
- HTML5
- Bootstrap 5

Hospedagem (Deploy):
- PythonAnywhere

## 💻 Como Executar Localmente
Para executar este projeto no seu ambiente local, siga os passos abaixo:

Clone o repositório:

Bash

git clone https://github.com/JoaoVianaSouza/Gerador_Orcamento.git
cd Gerador_Orcamento
Crie e ative um ambiente virtual:

Bash

## Para Windows
python -m venv venv
.\venv\Scripts\activate

## Para Linux/macOS
python3 -m venv venv
source venv/bin/activate
Instale as dependências:

Bash

pip install -r requirements.txt
Obs: Para o WeasyPrint funcionar no Windows, pode ser necessário instalar o GTK+. Veja a documentação oficial.

Execute a aplicação:

Bash

python app.py
Abra seu navegador e acesse http://127.0.0.1:5000.

## 👨‍💻 Autor
João Pedro Gonçalves Viana de Souza
