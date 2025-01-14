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
# Casos de Teste Implementados

### 1. Teste: Identificar Triângulo Equilátero
- **Descrição**: Verifica se o programa identifica corretamente um triângulo equilátero quando todos os lados são iguais.
- **Entradas**: 10, 10, 10
- **Resultado Esperado**: "Equilátero"

### 2. Teste: Identificar Triângulo Isósceles
- **Descrição**: Verifica se o programa identifica corretamente um triângulo isósceles quando dois lados são iguais.
- **Entradas**: 10, 10, 5
- **Resultado Esperado**: "Isósceles"

### 3. Teste: Identificar Triângulo Escaleno
- **Descrição**: Verifica se o programa identifica corretamente um triângulo escaleno quando todos os lados são diferentes.
- **Entradas**: 10, 8, 5
- **Resultado Esperado**: "Escaleno"

### 4. Teste: Identificar Triângulo com Letras
- **Descrição**: Verifica se o programa exibe uma mensagem de erro ao receber entradas não numéricas.
- **Entradas**: "a", "b", "c"
- **Resultado Esperado**: Uma mensagem de erro é exibida.

### 5. Teste: Identificar Triângulo com Espaços
- **Descrição**: Verifica se o programa exibe uma mensagem de erro ao receber entradas apenas com espaços.
- **Entradas**: "   ", "   ", "   "
- **Resultado Esperado**: Uma mensagem de erro é exibida.

### 6. Teste: Identificar Triângulo Degenerado
- **Descrição**: Verifica se o programa exibe uma mensagem de erro quando os lados não formam um triângulo (quando a soma de dois lados é menor ou igual ao comprimento do terceiro lado).
- **Entradas**: 5, 5, 10
- **Resultado Esperado**: Uma mensagem de erro é exibida.

### 7. Teste: Identificar Triângulo com Lado Zero
- **Descrição**: Verifica se o programa exibe uma mensagem de erro ao receber um lado igual a zero.
- **Entradas**: 0, 5, 5
- **Resultado Esperado**: Uma mensagem de erro é exibida.

### 8. Teste: Identificar Triângulo com Lado Negativo
- **Descrição**: Verifica se o programa exibe uma mensagem de erro ao receber um lado negativo.
- **Entradas**: -5, 5, 5
- **Resultado Esperado**: Uma mensagem de erro é exibida.
  
# Execução dos Testes
Para executar os testes, você pode usar o pytest. Execute o seguinte comando no terminal:

   ```bash
    pytest
  ```
