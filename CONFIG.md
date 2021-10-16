# AKShare install

pip install akshare -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com  --upgrade

# VS Code python 路径配置
shift + cmd + P => python: select Interpreter

akshare 文档
https://www.akshare.xyz/ 

akshare 使用docker配置

拉取
docker pull registry.cn-hangzhou.aliyuncs.com/akshare/akdocker
运行
docker run -it registry.cn-hangzhou.aliyuncs.com/akshare/akdocker python

打开打开后再浏览器可以使用 docker， 其中 home 文件夹映射到了 /User/lizhe 中
docker run -it -p 8888:8888 --name akdocker -v /Users/lizhe/workspace:/home registry.cn-hangzhou.aliyuncs.com/akshare/akdocker jupyter-lab --allow-root --no-browser --ip=0.0.0.0

容器建好后先按一波需要的，比如zsh
apt-get update && apt-get install -y vim zsh git   
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

下次打开时，先使用docker打开容器，再使用下面的命令连接到容器，默认就是zsh啦
docker exec -it akdocker /bin/zsh