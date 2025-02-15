# [리눅스] Bash cmake 사용법

## Overview
O `cmake` é uma ferramenta de automação de compilação que utiliza arquivos de configuração para gerar arquivos de projeto específicos para diferentes plataformas. Seu principal objetivo é simplificar o processo de construção de software, permitindo que os desenvolvedores especifiquem as dependências e configurações do projeto de forma independente do sistema operacional e do compilador.

## Usage
A sintaxe básica do comando `cmake` é a seguinte:

```bash
cmake [opções] <caminho_para_o_diretorio_do_projeto>
```

### Opções Comuns
- `-S <caminho>`: Especifica o diretório de origem onde os arquivos `CMakeLists.txt` estão localizados.
- `-B <caminho>`: Especifica o diretório de construção onde os arquivos de saída serão gerados.
- `-D <variável>=<valor>`: Define uma variável que pode ser utilizada no arquivo `CMakeLists.txt`.
- `--build <caminho>`: Compila o projeto a partir do diretório de construção especificado.
- `--target <alvo>`: Compila um alvo específico definido no projeto.

## Examples
### Exemplo 1: Configurando um Projeto
Para configurar um projeto localizado no diretório atual e gerar os arquivos de construção em um diretório chamado `build`, você pode usar o seguinte comando:

```bash
cmake -S . -B build
```

### Exemplo 2: Compilando o Projeto
Após a configuração, você pode compilar o projeto utilizando o comando:

```bash
cmake --build build
```

## Tips
- Sempre crie um diretório separado para a construção do projeto (como `build`) para manter os arquivos de origem e os arquivos gerados organizados.
- Utilize a opção `-D` para personalizar as configurações do seu projeto, como definir caminhos de bibliotecas ou habilitar/desabilitar recursos.
- Consulte a documentação do seu projeto para verificar se há opções específicas que podem ser definidas durante a configuração com `cmake`.