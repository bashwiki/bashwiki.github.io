# [리눅스] Bash timeout 사용법

## Visão Geral
O comando `timeout` é utilizado no Bash para executar um comando e limitar o tempo de execução desse comando. Se o comando não for concluído dentro do tempo especificado, o `timeout` irá interrompê-lo. Isso é especialmente útil em scripts onde é necessário evitar que um comando fique em execução indefinidamente, o que pode causar bloqueios ou consumo excessivo de recursos.

## Uso
A sintaxe básica do comando `timeout` é a seguinte:

```bash
timeout [DURAÇÃO] [COMANDO] [ARGUMENTOS...]
```

### Opções Comuns
- `DURAÇÃO`: Especifica o tempo máximo que o comando pode ser executado. O formato pode ser em segundos (s), minutos (m), horas (h) ou dias (d). Por exemplo, `5s` para 5 segundos, `2m` para 2 minutos.
- `COMANDO`: O comando que você deseja executar.
- `ARGUMENTOS`: Qualquer argumento adicional que o comando possa precisar.

## Exemplos
### Exemplo 1: Limitar a execução de um comando simples
Se você deseja executar um script que pode levar muito tempo, mas quer garantir que ele não exceda 10 segundos, você pode usar:

```bash
timeout 10s ./meu_script.sh
```

### Exemplo 2: Interromper um comando que não responde
Caso você esteja executando um comando que pode travar, como um download, e deseja limitá-lo a 30 segundos, você pode fazer:

```bash
timeout 30s wget http://exemplo.com/arquivo.zip
```

## Dicas
- Sempre teste seus comandos com `timeout` em um ambiente controlado antes de usá-los em produção para garantir que o tempo limite esteja configurado corretamente.
- Utilize um valor de tempo que seja razoável para o comando que você está executando. Um tempo muito curto pode resultar em interrupções desnecessárias.
- O `timeout` pode ser combinado com outros comandos e ferramentas, como `grep` ou `find`, para limitar a execução de operações que podem demorar.
- Lembre-se de que o `timeout` pode enviar um sinal de término padrão (SIGTERM) para o comando. Se o comando não responder a esse sinal, você pode usar a opção `-s` para especificar um sinal diferente, como SIGKILL, para forçar a interrupção.

Com essas informações, você está pronto para usar o comando `timeout` de forma eficaz em seus scripts e tarefas no Bash!