# [Linux] Bash cmake Uso: Ferramenta de construção de software

## Overview
O comando `cmake` é uma ferramenta de automação de compilação que utiliza arquivos de configuração para gerar arquivos Makefile e outros sistemas de construção. Ele é amplamente utilizado para compilar projetos de software em várias plataformas, facilitando o gerenciamento de dependências e a configuração do ambiente de construção.

## Usage
A sintaxe básica do comando `cmake` é a seguinte:

```bash
cmake [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que você pode usar com o `cmake`:

- `-S <diretório>`: Especifica o diretório fonte onde os arquivos CMakeLists.txt estão localizados.
- `-B <diretório>`: Define o diretório de construção onde os arquivos gerados serão colocados.
- `-D <variável>=<valor>`: Define uma variável para ser usada no processo de configuração.
- `--build <diretório>`: Compila o projeto no diretório especificado.
- `--target <alvo>`: Especifica um alvo específico a ser construído.

## Common Examples
Aqui estão alguns exemplos práticos de como usar o `cmake`:

### Exemplo 1: Configurar um projeto
Para configurar um projeto localizado em um diretório chamado `meu_projeto`, você pode usar:

```bash
cmake -S meu_projeto -B meu_projeto/build
```

### Exemplo 2: Compilar o projeto
Após a configuração, você pode compilar o projeto com:

```bash
cmake --build meu_projeto/build
```

### Exemplo 3: Definir uma variável
Se você precisar definir uma variável durante a configuração, como `CMAKE_BUILD_TYPE`, você pode fazer assim:

```bash
cmake -S meu_projeto -B meu_projeto/build -D CMAKE_BUILD_TYPE=Release
```

### Exemplo 4: Construir um alvo específico
Para construir um alvo específico, como `install`, você pode usar:

```bash
cmake --build meu_projeto/build --target install
```

## Tips
- Sempre crie um diretório separado para a construção do seu projeto para manter os arquivos organizados.
- Utilize a opção `-D` para ajustar configurações específicas do seu projeto sem modificar os arquivos de origem.
- Consulte a documentação do seu projeto para verificar se há opções específicas recomendadas para a configuração e construção.