# git的用法



## 1.配置git

查看所有配置

```console
git config --list   
```
### 全局配置

```console
git config --global user.name "John Doe"
```

如果使用了 `--global` 选项，那么该命令只需要运行一次，因为之后无论你在该系统上做任何事情， Git 都会使用那些信息。 当你想针对特定项目使用不同的用户名称与邮件地址时，可以在那个项目目录下运行没有 `--global` 选项的命令来配置。

如果想要查看全局配置有哪些，需要

```console
git config --global -l
```

如果想要取消全局配置，需要

```console
git config --global --unset user.name
```

## 2.初始化仓库和克隆仓库

克隆仓库

```console
git clone https://github.com/GalaxyM87/study-python
```

## 3.更新仓库

### 检查当前文件状态

```console
git status
```

如果刚刚下载完仓库，会出现

```console
On branch master
Your branch is up-to-date with 'origin/master'.
nothing to commit, working directory clean
```

我们现在新建一个README文件，并且看一下状态变化

### 新建一个文件

```console
echo 'My Project' > README
```

```console
On branch master
Your branch is up-to-date with 'origin/master'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)

    README

nothing added to commit but untracked files present (use "git add" to track)
```

在状态报告中可以看到新建的 `README` 文件出现在 `Untracked files` 下面。 未跟踪的文件意味着 Git 在之前的快照（提交）中没有这些文件；Git 不会自动将之纳入跟踪范围

### 跟踪文件

```console
git add README
```

我们对新建的文件进行跟踪后，会出现

```console
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

    new file:   README
```

如果我们对一开始克隆进来的东西进行修改，会出现

```console
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

    modified:   CONTRIBUTING.md
```

说明已跟踪文件的内容发生了变化，但还没有放到暂存区。 要暂存这次更新，需要运行 `git add` 命令。

```console
git add README.md
```

会出现

```console
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   README
        modified:   README.md
```

`git add` 是个多功能命令：可以用它开始跟踪新文件，或者把已跟踪的文件放到暂存区，还能用于合并时把有冲突的文件标记为已解决状态等。 将这个命令理解为“精确地将内容添加到下一次提交中”而不是“将一个文件添加到项目中”要更加合适。

**强调：运行了 `git add` 之后又作了修订的文件，需要重新运行 `git add` 把最新版本重新暂存起来**

### 提交文件

```console
git commit -m "First commit"
```

  引号内为提交的名字

### 更新到远程git-hub

```console
git push -u origin main
```

origin是在克隆仓库默认的名字，可以自己设置。

## 查看自己仓库的名字

```console
git remote -v
```









