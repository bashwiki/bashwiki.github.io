# [Linux] Bash git 用法：版本控制工具

## 概述
`git` 是一个分布式版本控制系统，用于跟踪文件的更改，特别是源代码。它允许多个开发者在同一个项目中协作，管理代码的版本历史。

## 用法
基本语法如下：
```
git [选项] [参数]
```

## 常用选项
- `clone`：克隆一个远程仓库到本地。
- `add`：将文件添加到暂存区。
- `commit`：提交暂存区的更改。
- `push`：将本地提交推送到远程仓库。
- `pull`：从远程仓库获取并合并更改。
- `status`：查看当前工作目录和暂存区的状态。

## 常见示例
1. 克隆远程仓库：
   ```bash
   git clone https://github.com/username/repo.git
   ```

2. 添加文件到暂存区：
   ```bash
   git add filename.txt
   ```

3. 提交更改：
   ```bash
   git commit -m "添加了新功能"
   ```

4. 推送更改到远程仓库：
   ```bash
   git push origin main
   ```

5. 从远程仓库拉取更改：
   ```bash
   git pull origin main
   ```

6. 查看当前状态：
   ```bash
   git status
   ```

## 提示
- 在提交之前，使用 `git status` 检查文件状态，以确保所有更改都已正确添加。
- 使用有意义的提交信息，以便将来更容易理解更改的目的。
- 定期推送更改到远程仓库，以避免数据丢失。
- 学习使用分支（`git branch` 和 `git checkout`）来管理不同的开发任务。