# [Linux] Bash break 用法: 退出循环

## 概述
`break` 命令用于退出当前的循环结构（如 `for`、`while` 或 `until` 循环）。当满足特定条件时，可以使用 `break` 提前结束循环。

## 用法
基本语法如下：
```bash
break [n]
```
其中 `n` 是一个可选参数，表示退出的循环层级，默认为 1。

## 常用选项
- `n`：指定要退出的循环层级。如果在嵌套循环中使用，`n` 可以用来指定要退出的外层循环的数量。

## 常见示例
1. **基本示例**：退出一个简单的 `for` 循环。
   ```bash
   for i in {1..5}; do
       if [ $i -eq 3 ]; then
           break
       fi
       echo $i
   done
   ```
   输出：
   ```
   1
   2
   ```

2. **嵌套循环示例**：退出外层循环。
   ```bash
   for i in {1..3}; do
       for j in {1..3}; do
           if [ $i -eq 2 ]; then
               break 2
           fi
           echo "i=$i, j=$j"
       done
   done
   ```
   输出：
   ```
   i=1, j=1
   i=1, j=2
   i=1, j=3
   ```

3. **使用条件退出**：在 `while` 循环中使用 `break`。
   ```bash
   count=1
   while true; do
       echo $count
       if [ $count -ge 5 ]; then
           break
       fi
       ((count++))
   done
   ```
   输出：
   ```
   1
   2
   3
   4
   5
   ```

## 提示
- 在使用 `break` 时，确保清楚哪个循环将被退出，特别是在嵌套循环中。
- 使用 `break` 可以提高脚本的效率，避免不必要的循环迭代。
- 结合 `continue` 命令使用，可以更灵活地控制循环的执行流程。