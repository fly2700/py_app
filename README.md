# py_app
python基本命令行程序
有简单日志打印、文件处理、命令行参数处理等基本功能

pycharm 添加 github 方法

1.在空文件夹运行
git init
git pull https://github.com/fly2700/py_app.git
git branch dev
git checkout dev


2.修改源码后运行
文件右键  Git  "show diff"
文件右键  Git  "commit"


3.push
git push https://github.com/fly2700/py_app.git master
input token




# github

…or create a new repository on the command line
echo "# test" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/fly2700/py_app.git
git push -u origin main

…or push an existing repository from the command line
git remote add origin https://github.com/fly2700/py_app.git
git branch -M main
git push -u origin main