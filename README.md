# Mail Mind: Uma nova forma de utilizar o e-mail!

Este projeto consiste em realizarmos a leitura e classificação de e-mails mediante a um upload que estará disponível neste <link>

*OBS: Todas as tecnologias necessárias estarão dispostas no arquivo requirements.txt, trazendo assim facilidade na hora da instalação além do passo-a-passo aqui descrito.*

## O que é o Mail Mind?

Mail Mind é uma nova forma de analisar e-mails de forma inteligente, rápida e ágil. Com sua arquitetura hospedada na AWS, temos agilidade, escalabilidade e inovação, além de termos a IA mais famosa do mercado ao nosso lado: o GPT.
Contendo uma interface agradável e simples porém com uma infraestrutura e lógicas robustas. Espero que gostem do projeto apresentado!

O projeto estará hospedado na AWS, logo, será possível acessá-lo pelo <link>. 

O frontend foi pensado para ser simples porém intuitivo e funcional, tendo sido hospedado em um CloudFront + S3 para armazenamento dos arquivos temporários que serão encaminhados para uma Lambda, onde será feito todo o processo lógico de leitura, classificação e retorno para o usuário com as saídas esperadas:
  - Categoria -> Produtivo / Improdutivo;
  - Resposta automática baseada na classificação;

## Tecnologias usadas:
  - Python;
  - FastAPI;
  - PyPDF;
  - OpenAI GPT;
  - AWS;

# Como instalar e fazer o uso de forma local

Atente-se ao arquivo **requirements.txt** ele será extremamente necessário para a execução do código localmente!

Vamos começar então pela lista dos frameworks e bibliotecas utilizados no projeto, fazendo a devido instalação em seu ambiente.

*OBS: Pensando de forma que você já tenha o python instalado em sua máquina*


  pip install "fastapi[standard]"
  pip install langchain 
  pip install langchain-openai 
  pip install pypdf


Após ter todo o seu ambiente com as devidas dependências, será necessário fazer o download do código, que estará disponível na branch main, e após é só abri-lo dentro da sua IDE (no meu caso estou utilizando o VSCode)
