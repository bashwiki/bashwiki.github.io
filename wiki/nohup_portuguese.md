# [리눅스] Bash nohup 사용법

## Overview
O comando `nohup` (no hang up) é utilizado no ambiente Unix/Linux para executar processos que não são interrompidos quando o usuário sai da sessão. Isso é especialmente útil para executar scripts ou programas de longa duração em segundo plano, garantindo que eles continuem rodando mesmo que a conexão com o terminal seja encerrada. O `nohup` redireciona a saída padrão e a saída de erro para um arquivo chamado `nohup.out`, a menos que especificado de outra forma.

## Usage
A sintaxe básica do comando `nohup` é a seguinte:

```bash
nohup comando [argumentos] &
```

### Opções Comuns:
- `&`: Coloca o comando em segundo plano, permitindo que você continue usando o terminal.
- `-o arquivo`: Especifica um arquivo para redirecionar a saída padrão (substitui `nohup.out`).
- `-e arquivo`: Especifica um arquivo para redirecionar a saída de erro.

## Examples
### Exemplo 1: Executando um script em segundo plano
Se você tem um script chamado `meu_script.sh` que leva muito tempo para ser executado, você pode usar o `nohup` da seguinte forma:

```bash
nohup ./meu_script.sh &
```

Isso executará `meu_script.sh` em segundo plano e você poderá sair do terminal sem interromper a execução do script.

### Exemplo 2: Redirecionando a saída para um arquivo específico
Se você deseja que a saída do seu comando seja gravada em um arquivo específico, você pode fazer assim:

```bash
nohup python meu_programa.py > saida.txt 2>&1 &
```

Neste exemplo, a saída padrão e a saída de erro do programa Python serão redirecionadas para `saida.txt`.

## Tips
- Sempre verifique o arquivo `nohup.out` ou o arquivo de saída que você especificou para verificar os logs e mensagens de erro do seu comando.
- Utilize o comando `jobs` para listar os processos em segundo plano e `fg` para trazê-los de volta ao primeiro plano, se necessário.
- Combine o `nohup` com o comando `screen` ou `tmux` para uma gestão ainda mais robusta de sessões em segundo plano, permitindo que você desconecte e reconecte sem perder o progresso.