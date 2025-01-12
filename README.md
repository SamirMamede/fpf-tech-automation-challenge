# fpf-tech-automation-challenge
Cenários de teste e automação de testes funcionais  utilizando o Selenium WebDriver

<p>Crie os cenários de teste e implemente a automação de testes funcionais 
utilizando o Selenium WebDriver e algum framework de teste unitário em 
qualquer linguagem de programação para a aplicação triângulo disponível 
em http://www.vanilton.net/triangulo/. Os testes devem cobrir o requisito:  
Dados os três lados de um triângulo, o programa informará se o triângulo é equilátero, 
isósceles ou escaleno. Lembre-se que os lados só formam um triângulo se o comprimento 
de um lado for sempre menor do que a soma dos outros dois (o programa deve exibir uma 
mensagem de erro caso essa propriedade não seja satisfeita) 
Por fim compartilhe o link do código fonte no github ou gitlab e documente o que é 
preciso e como realizar a sua execução.</p>  

# Documentação para Execução de Testes de Automação

## Repositório

Você pode clonar o repositório usando o seguinte link:
https://github.com/SamirMamede/fpf-tech-automation-challenge.git

   ```bash
   git clone https://github.com/SamirMamede/fpf-tech-automation-challenge.git
   ```


## Pré-requisitos

Antes de executar os testes, você precisa ter o seguinte instalado em sua máquina:

1. **Python**: Certifique-se de que você tenha o Python 3.x instalado. Você pode baixar o Python em [python.org](https://www.python.org/downloads/).

2. **Pip**: O `pip` é o gerenciador de pacotes do Python e geralmente é instalado automaticamente com o Python. Você pode verificar se o `pip` está instalado executando o seguinte comando no terminal:

   ```bash
   pip --version
   ```

# Instalação de Dependências
Após clonar o repositório, navegue até o diretório do projeto e instale as dependências necessárias usando o pip. Execute os seguintes comandos no terminal:

   ```bash
    # Navegue até o diretório do projeto
    cd fpf-tech-automation-challenge

    # Instale as dependências
    pip install -r requirements.txt
  ```
# Execução dos Testes
Para executar os testes, você pode usar o pytest. Execute o seguinte comando no terminal:

   ```bash
    pytest
  ```