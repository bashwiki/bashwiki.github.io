# [Linux] Bash g++ Uso: Compilar programas em C++

## Overview
O comando `g++` é um compilador para a linguagem de programação C++. Ele é parte do projeto GNU e é amplamente utilizado para compilar código fonte escrito em C++ em arquivos executáveis. O `g++` é conhecido por sua eficiência e suporte a diversas funcionalidades da linguagem.

## Usage
A sintaxe básica do comando `g++` é a seguinte:

```bash
g++ [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns que podem ser usadas com o `g++`:

- `-o <arquivo>`: Especifica o nome do arquivo de saída.
- `-Wall`: Ativa todos os avisos recomendados.
- `-g`: Gera informações de depuração para uso com depuradores.
- `-std=<padrão>`: Define o padrão da linguagem C++ a ser utilizado (por exemplo, `-std=c++11`).
- `-I<diretório>`: Adiciona um diretório à lista de diretórios onde o compilador procura arquivos de cabeçalho.

## Common Examples
Aqui estão alguns exemplos práticos de como usar o `g++`:

1. Compilar um único arquivo C++:
   ```bash
   g++ meu_programa.cpp -o meu_programa
   ```

2. Compilar vários arquivos C++:
   ```bash
   g++ arquivo1.cpp arquivo2.cpp -o meu_programa
   ```

3. Compilar com avisos ativados:
   ```bash
   g++ -Wall meu_programa.cpp -o meu_programa
   ```

4. Compilar com informações de depuração:
   ```bash
   g++ -g meu_programa.cpp -o meu_programa
   ```

5. Usar um padrão específico da linguagem:
   ```bash
   g++ -std=c++17 meu_programa.cpp -o meu_programa
   ```

## Tips
- Sempre utilize a opção `-Wall` para ajudar a identificar possíveis problemas no seu código.
- Mantenha seu código organizado em múltiplos arquivos para facilitar a manutenção e a compilação.
- Utilize a opção `-g` durante o desenvolvimento para facilitar a depuração do seu código.
- Verifique a documentação do `g++` para explorar opções avançadas que podem ser úteis para seu projeto.