# 设置基础镜像为Python官方的轻量级镜像
FROM python:3.9-slim

# 设置工作目录为/app
WORKDIR /app

# 复制当前目录下的所有文件到容器的/app目录下
COPY . /app

# 设置Python镜像
RUN python3 -m pip config set global.index-url https://mirrors.aliyun.com/pypi/simple

# 安装Python依赖包
RUN python3 -m pip install -r requirements.txt

# 设置时区为Asia/Shanghai
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 运行Python应用程序
CMD ["python3", "bot.py"]
