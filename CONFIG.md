# AKShare install

pip install akshare -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com  --upgrade

# VS Code python 路径配置
shift + cmd + P => python: select Interpreter

akshare 使用docker配置

拉取
docker pull registry.cn-hangzhou.aliyuncs.com/akshare/akdocker
运行
docker run -it registry.cn-hangzhou.aliyuncs.com/akshare/akdocker python

打开打开后再浏览器可以使用 docker， 其中 home 文件夹映射到了 ./ 中
docker run -it -p 8888:8888 --name akdocker -v ./:/home registry.cn-hangzhou.aliyuncs.com/akshare/akdocker jupyter-lab --allow-root --no-browser --ip=0.0.0.0
