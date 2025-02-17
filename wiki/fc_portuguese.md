# [Linux] Bash fc Uso: Editar e reexecutar comandos anteriores

## Overview
O comando `fc` no Bash é utilizado para listar, editar e reexecutar comandos que foram executados anteriormente no shell. Ele permite que os usuários façam modificações em comandos passados antes de executá-los novamente, facilitando a correção de erros ou a reutilização de comandos.

## Usage
A sintaxe básica do comando `fc` é a seguinte:

```bash
fc [opções] [argumentos]
```

## Common Options
Aqui estão algumas opções comuns do comando `fc`:

- `-l`: Lista os comandos anteriores.
- `-s`: Executa o comando sem abrir um editor.
- `-e`: Especifica um editor diferente para editar o comando.

## Common Examples

### Listar comandos anteriores
Para listar os últimos 10 comandos executados, você pode usar:

```bash
fc -l -n -10
```

### Editar o último comando
Para editar o último comando executado no seu editor padrão, use:

```bash
fc
```

### Executar o último comando sem editar
Se você deseja reexecutar o último comando sem abri-lo para edição, utilize:

```bash
fc -s
```

### Editar um comando específico
Para editar um comando específico, você pode especificar o número do comando. Por exemplo, para editar o comando número 5:

```bash
fc 5
```

### Usar um editor específico
Para usar um editor específico, como `nano`, ao editar o último comando, você pode fazer:

```bash
fc -e nano
```

## Tips
- Utilize `fc -l` frequentemente para revisar rapidamente seus comandos anteriores.
- Combine `fc` com outros comandos, como `grep`, para encontrar comandos específicos na sua história.
- Lembre-se de que o `fc` apenas funciona com comandos que estão na história do shell atual. Se você reiniciar o terminal, a história pode ser perdida, dependendo da configuração.