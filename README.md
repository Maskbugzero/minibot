<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>

<div align="center">
<h1 align="center">🔥 minibot</h1>

✨ 自用定时发送QQ消息的机器人 ✨

</div>

## 项目地址
[minibot](https://github.com/maskbugzero/minibot)

## 功能描述
一款基于[nonebot_plugin_firexN](https://github.com/GC-ZF/nonebot_plugin_firexN)自用定时发送QQ消息的机器人


定时早上发一条信息,具有vip联系人以及普通联系人，可以自定义发送消息的内容及时间。


## 安装以及依赖
```shell
git clone https://github.com/maskbugzero/minibot
cd minibot
pip install -r requirements.txt
```

配置完成后运行
```shell
nohup python3 bot.py > minibot.log 2>&1 &
```
## 配置

在`.env`中配置参数说明

```python
ENVIRONMENT=dev # 配置文件使用.env.dev
DRIVER=~fastapi        
```

新建一个`.env.dev`文件

在`.env.dev`中配置参数说明

```python
HOST=0.0.0.0
PORT=8080

fire_vip_users = ["xxx","xxx"]    # 必填 vip联系人QQ
fire_users = ["xxx","xxx"]    # 必填 联系人QQ
fire_sentence_vip_moring = ["句子1","句子2","..."]    # 早上随机发送该字段中的一句
fire_sentence_moring = ["句子1","句子2","..."]    # 早上随机发送该字段中的一句
fire_time_vip_moring = "8 0"    # 选填 早上发送时间默认为7:00            
fire_time_moring = "8 0"    # 选填 早上发送时间默认为7:00           
```


## 基于
[Nonebot2](https://github.com/nonebot/nonebot2)
[nonebot_plugin_firexN](https://github.com/GC-ZF/nonebot_plugin_firexN)