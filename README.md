# py_app 项目简介
python程序框架:
- ### tools.log 日志打印
- ### tools.file 文件操作
- ### tools.utils 通用模块
  
  
# github下载代码和添加到pycharm方法

## 1.在空文件夹运行  
git init  
git pull https://github.com/fly2700/py_app.git  
git branch -M main  
  
## 2.修改源码后  
在pycharm中  
文件右键 -> Git -> "show diff"  
文件右键 -> Git -> "commit"  
  
## 3.push  
在pycharm中 文件右键 -> Git -> “push"  
或  
git push https://github.com/fly2700/py_app.git main  
input token  
  
  
# github new

create a new repository on the command line  
echo "# test" >> README.md  
git init  
git add README.md  
git commit -m "first commit"  
git branch -M main  
git remote add origin https://github.com/fly2700/py_app.git  
git push -u origin main  
  
or push an existing repository from the command line  
git remote add origin https://github.com/fly2700/py_app.git  
git branch -M main  
git push -u origin main  
