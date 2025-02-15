# [리눅스] Bash tput 사용법

## Overview
O comando `tput` é uma ferramenta utilizada em sistemas Unix e Linux para controlar a interface de terminal. Ele permite que os usuários configurem a aparência e o comportamento do terminal, como a manipulação de cores, o posicionamento do cursor e a formatação do texto. O principal propósito do `tput` é fornecer uma interface de alto nível para as capacidades do terminal, facilitando a criação de scripts que interagem de forma mais rica com o ambiente do terminal.

## Usage
A sintaxe básica do comando `tput` é a seguinte:

```bash
tput [opção] [argumento]
```

### Opções Comuns
- `setaf N`: Define a cor do texto para o número da cor `N` (0-7 para cores padrão).
- `setab N`: Define a cor do fundo para o número da cor `N`.
- `cup X Y`: Move o cursor para a posição na linha `X` e coluna `Y`.
- `clear`: Limpa a tela do terminal.
- `bold`: Ativa o texto em negrito.
- `smso`: Ativa o modo de destaque (standout mode).
- `rmso`: Desativa o modo de destaque.

## Examples
### Exemplo 1: Mudando a Cor do Texto
Para mudar a cor do texto para verde, você pode usar o seguinte comando:

```bash
tput setaf 2
echo "Este texto está em verde!"
tput sgr0  # Reseta as configurações de formatação
```

### Exemplo 2: Movendo o Cursor
Para mover o cursor para a linha 5 e coluna 10 e imprimir um texto, você pode usar:

```bash
tput cup 5 10
echo "Texto na linha 5, coluna 10"
```

## Tips
- Sempre use `tput sgr0` após aplicar formatações para garantir que o terminal retorne ao estado padrão.
- Teste as cores disponíveis no seu terminal, pois a representação de cores pode variar entre diferentes emuladores de terminal.
- Combine `tput` com outros comandos de shell para criar scripts interativos e visualmente atraentes.