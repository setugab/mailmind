# Mail Mind: Uma nova forma de utilizar o e-mail!

Este projeto consiste em realizarmos a leitura e classificação de e-mails mediante a um upload que poderá ser feito além de digitar no campo de texto aberto!

## O que é o Mail Mind?

Mail Mind é uma nova forma de analisar e-mails de forma inteligente, rápida e ágil. Com sua arquitetura hospedada na AWS, temos agilidade, escalabilidade e inovação, além de termos a IA mais famosa do mercado ao nosso lado: o GPT.
Contendo uma interface agradável e simples porém com uma infraestrutura e lógicas robustas. Espero que gostem do projeto apresentado!

O projeto estará hospedado na AWS, logo, será possível acessá-lo pelo [link](https://d3r739i9kikprl.cloudfront.net/)

O frontend foi pensado para ser simples porém intuitivo e funcional, tendo sido hospedado em um S3 e tendo sua disponibilidade aumentada com um CloudFront, os e-mails serão encaminhados para uma Lambda, onde será feito todo o processo lógico de leitura, classificação e retorno para o usuário com as saídas esperadas:
  - Categoria -> Produtivo / Improdutivo;
  - Resposta automática baseada na classificação;

## Tecnologias usadas:
  - Python 3.12;
  - PyPDF - Disponibiliza as ações de leitura de arquivos PDF;
  - OpenAI GPT (3.5 - Turbo) - A IA Generativa que fará as classificações e respostas;
  - NLTK - Biblioteca voltada para realizar a NLP dos arquivos;
  - Terraform - Usado para subir todos os códigos e layers na AWS;
  - AWS - Ambiente Cloud de extrema robustez e tecnologia;

# Como instalar e fazer o uso de forma local

Como o código está operando integralmente na AWS, estarei disponibilizando os códigos para que rode neste ambiente, sendo assim necessário adaptação do código para rodar localmente.

⚠️ Observações
O código está preparado para rodar na AWS; para execução local, será necessário adaptação do código.

Faça o pip install do *requirements.txt* pelo seguinte comando:

``` pip install -r requirements.txt -t . ```

Assim que instalado as depêndencias, só importar os códigos e realizar as devidas alterações para rodar localmente.

``` git clone https://github.com/setugab/mailmind.git ```

``` cd mailmind ```
