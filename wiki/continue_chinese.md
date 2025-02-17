# [Linux] Bash continue 用法: 继续循环执行

## 概述
`continue` 命令用于在循环中跳过当前迭代的剩余部分，直接进入下一次迭代。这在需要根据特定条件跳过某些操作时非常有用。

## 用法
基本语法如下：
```bash
continue [n]
```
其中 `n` 是一个可选参数，表示跳过的循环层级，默认为 1。

## 常用选项
- `n`：指定要跳过的循环层级。如果在嵌套循环中使用，可以指定跳过外层循环的次数。

## 常见示例

### 示例 1：基本用法
在一个简单的 `for` 循环中，跳过偶数：
```bash
for i in {1..10}; do
    if (( i % 2 == 0 )); then
        continue
    fi
    echo $i
done
```
输出：
```
1
3
5
7
9
```

### 示例 2：跳过外层循环
在嵌套循环中，跳过外层循环的迭代：
```bash
for i in {1..3}; do
    for j in {1..3}; do
        if (( j == 2 )); then
            continue 2
        fi
        echo "i: $i, j: $j"
    done
done
```
输出：
```
i: 1, j: 1
i: 1, j: 3
i: 2, j: 1
i: 2, j: 3
i: 3, j: 1
i: 3, j: 3
```

### 示例 3：结合其他命令
在处理文件时，跳过特定条件的文件：
```bash
for file in *; do
    if [[ $file == *.tmp ]]; then
        continue
    fi
    echo "Processing $file"
done
```

## 小贴士
- 使用 `continue` 时，确保条件判断逻辑清晰，以避免意外跳过重要的操作。
- 在嵌套循环中使用 `continue n` 时，注意 `n` 的值，以确保跳过正确的循环层级。
- 结合 `break` 命令使用，可以更灵活地控制循环的执行流程。