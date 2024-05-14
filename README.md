# Contrato de Locação - Gerador de Documentos

O **Contrato de Locação - Gerador de Documentos** é uma aplicação Flask simples que gera contratos de locação de imóveis em formato DOCX a partir de um formulário preenchido pelo usuário.

## Objetivo
Este projeto visa facilitar a vida de proprietários de imóveis que trabalham com aluguel direto de apartamentos, fornecendo uma ferramenta simples para a geração automatizada de contratos de locação. O objetivo é eliminar a necessidade de editar manualmente os contratos no Word, economizando tempo e esforço.

## Funcionalidades
- Geração dinâmica de contratos de locação em formato DOCX.
- Converte valores numéricos em extenso.
- Utiliza um formulário web para coletar informações do locatário.

## Tecnologias Utilizadas
- Python: Linguagem de programação utilizada para desenvolver a aplicação.
- Flask: Framework web utilizado para criar a aplicação web.
- Jinja2: Motor de template utilizado para renderizar os modelos HTML.
- python-docx: Biblioteca para criação e manipulação de documentos DOCX.
- num2words: Biblioteca para converter valores numéricos em palavras.
- HTML/CSS: Utilizado para criar o formulário de entrada e o layout da página.
- Bootstrap: Framework CSS utilizado para estilizar a interface do usuário.

## Instalação
1. Clone o repositório:
  git clone https://github.com/seu_usuario/contrato-locacao.git
2. Instale as dependências:
  cd contrato-locacao
  pip install -r requirements.txt

## Uso
1. Execute o aplicativo:
   python app.py
2. Acesse o aplicativo no navegador:
  Navegue até [http://localhost:5000](http://localhost:5000) para acessar o formulário de geração de contrato.
3. Preencha o formulário:
  Preencha todos os campos necessários no formulário e envie os dados.
4. Baixe o contrato:
  Após enviar o formulário, o contrato gerado estará disponível para download.

## Deploy
O **Contrato de Locação - Gerador de Documentos** foi implantado na plataforma Render. Você pode acessar o aplicativo em https://contratonahora.onrender.com

Para implantar o aplicativo em outras plataformas de hospedagem web, consulte a documentação oficial de cada plataforma para obter instruções específicas.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue para relatar problemas ou sugerir melhorias. Se desejar contribuir com código, faça um fork do repositório e envie um pull request.


