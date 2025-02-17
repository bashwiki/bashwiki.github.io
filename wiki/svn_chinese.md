# [Linux] Bash svn 使用指南: 版本控制命令

## 概述
`svn`（Subversion）是一个流行的版本控制系统，用于管理文件和目录的版本。它允许用户跟踪文件的变化，协作开发，并恢复到以前的版本。

## 使用方法
基本语法如下：
```bash
svn [选项] [参数]
```

## 常用选项
- `checkout`：从版本库中检出工作副本。
- `commit`：将本地更改提交到版本库。
- `update`：更新工作副本以与版本库同步。
- `add`：将新文件或目录添加到版本控制中。
- `delete`：从版本控制中删除文件或目录。

## 常见示例
1. 检出版本库：
   ```bash
   svn checkout https://example.com/svn/myproject/trunk
   ```

2. 提交更改：
   ```bash
   svn commit -m "修复了一个bug"
   ```

3. 更新工作副本：
   ```bash
   svn update
   ```

4. 添加新文件：
   ```bash
   svn add newfile.txt
   ```

5. 删除文件：
   ```bash
   svn delete oldfile.txt
   ```

## 小贴士
- 在提交之前，使用 `svn status` 查看工作副本的状态。
- 定期更新工作副本，以避免与其他开发者的更改冲突。
- 使用有意义的提交信息，以便将来能够清楚地了解更改的目的。