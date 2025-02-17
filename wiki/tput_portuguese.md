# [Linux] Bash tput Uso: Controle de terminal e formatação de texto

## Overview
O comando `tput` é utilizado para controlar a aparência do terminal e formatar texto em ambientes de linha de comando. Ele permite que os usuários alterem as propriedades do terminal, como cores, estilos de texto e movimentação do cursor, proporcionando uma experiência mais rica e interativa.

## Usage
A sintaxe básica do comando `tput` é a seguinte:

```bash
tput [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do `tput`:

- `setaf [n]`: Define a cor do texto (foreground) para o número especificado `n`.
- `setab [n]`: Define a cor do fundo (background) para o número especificado `n`.
- `bold`: Ativa o estilo de texto em negrito.
- `smso`: Ativa o modo de destaque (standout mode).
- `rmso`: Desativa o modo de destaque.
- `cup [x] [y]`: Move o cursor para a posição especificada nas coordenadas `x` e `y`.

## Common Examples
Aqui estão alguns exemplos práticos do uso do `tput`:

1. **Alterar a cor do texto para vermelho:**
   ```bash
   tput setaf 1
   echo "Este texto é vermelho!"
   ```

2. **Alterar a cor do fundo para azul e o texto para branco:**
   ```bash
   tput setab 4
   tput setaf 7
   echo "Texto branco em fundo azul!"
   ```

3. **Ativar o estilo de texto em negrito:**
   ```bash
   tput bold
   echo "Este texto está em negrito!"
   tput sgr0  # Reseta as configurações de estilo
   ```

4. **Mover o cursor para a linha 5, coluna 10:**
   ```bash
   tput cup 5 10
   echo "Texto na linha 5, coluna 10."
   ```

5. **Ativar e desativar o modo de destaque:**
   ```bash
   tput smso
   echo "Texto em destaque!"
   tput rmso
   ```

## Tips
- Sempre use `tput sgr0` após aplicar estilos para resetar as configurações e evitar que o estilo se aplique a textos subsequentes.
- Experimente diferentes números para `setaf` e `setab` para ver as várias cores disponíveis no seu terminal.
- Combine `tput` com outros comandos para criar scripts interativos e visualmente atraentes.