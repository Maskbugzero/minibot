"""
配置:
      fire_vip_users = ["xxx","xxx"]    # 必填 vip联系人QQ
      fire_users = ["xxx","xxx"]    # 必填 联系人QQ
      fire_sentence_vip_moring = ["句子1","句子2","..."]    # 早上随机发送该字段中的一句
      fire_sentence_moring = ["句子1","句子2","..."]    # 早上随机发送该字段中的一句
      fire_time_vip_moring = "8 0"    # 选填 早上发送时间默认为7:00            
      fire_time_moring = "8 0"    # 选填 早上发送时间默认为7:00           
"""

import asyncio
import random
from nonebot import require, get_bot, get_driver
from nonebot.log import logger
import requests
import json
import nonebot.plugin

try:
    scheduler = require ( "nonebot_plugin_apscheduler" ).scheduler
except BaseException:
    scheduler = None

logger.opt ( colors=True ).info (
    "已检测到软依赖<y>nonebot_plugin_apscheduler</y>, <g>开启定时任务功能</g>"
    if scheduler
    else "未检测到软依赖<y>nonebot_plugin_apscheduler</y>，<r>禁用定时任务功能</r>"
)

# 获取_vip_联系人QQ
try:
    fire_vip_user_id = get_driver ().config.fire_vip_users  # <-填写需要收发的QQ联系人,利用for循环遍历QQ发送
except Exception as e:
    logger.error ( "ValueError:{}", e )
    logger.error ( "请配置fire_vip_user_id" )

# 获取联系人QQ
try:
    fire_user_id = get_driver ().config.fire_users  # <-填写需要收发的QQ联系人,利用for循环遍历QQ发送
except Exception as e:
    logger.error ( "ValueError:{}", e )
    logger.error ( "请配置fire_user_id" )

# 取_vip_自定义句子
try:
    fire_sentence_vip_moring = get_driver ().config.fire_sentence_vip_moring
except Exception as e:
    logger.error ( "读取_vip_句子失败" )

# 取自定义句子
try:
    fire_sentence_moring = get_driver ().config.fire_sentence_moring
except Exception as e:
    logger.error ( "读取自定义句子失败" )


# 获取_vip_自定义时间，默认早上七点
try:
    fire_time_vip_moring = get_driver ().config.fire_time_vip_moring
    assert fire_time_vip_moring is not None
except (AttributeError, AssertionError):
    fire_time_vip_moring = "7 0"
vip_hour, vip_minute = fire_time_vip_moring.split ( " " )

# 获取自定义时间，默认早上七点
try:
    fire_time_moring = get_driver ().config.fire_time_moring
    assert fire_time_moring is not None
except (AttributeError, AssertionError):
    fire_time_moring = "7 0"
m_hour, m_minute = fire_time_moring.split ( " " )

async def fire_vip_morning():
    sendSuccess = False
    while not sendSuccess:
        try:
            await asyncio.sleep ( random.randint ( 1, 600 ) )
            for gid in fire_vip_user_id:
                await get_bot ().send_private_msg ( user_id=gid,
                                                    message=f"{random.choice ( fire_sentence_vip_moring )}" )
            logger.info ( "发送_vip_火花" )
            sendSuccess = True
        except ValueError as e:
            logger.error ( "ValueError:{}", e )
            logger.error ( "续火花_vip_插件获取bot失败，60s后重试" )
            await asyncio.sleep ( 60 )  # 重试前时延，防止阻塞

async def fire_morning():
    sendSuccess = False
    while not sendSuccess:
        try:
            await asyncio.sleep ( random.randint ( 1, 600 ) )
            for gid in fire_user_id:
                await get_bot ().send_private_msg ( user_id=gid,
                                                    message=f"{random.choice ( fire_sentence_moring )}" )
            logger.info ( "发送火花" )
            sendSuccess = True
        except ValueError as e:
            logger.error ( "ValueError:{}", e )
            logger.error ( "续火花插件获取bot失败，60s后重试" )
            await asyncio.sleep ( 60 )  # 重试前时延，防止阻塞


if scheduler:
    scheduler.add_job ( fire_vip_morning, "cron", hour=vip_hour, minute=vip_minute, id="fire_vip_morning" )  # _vip_早安
    scheduler.add_job ( fire_morning, "cron", hour=m_hour, minute=m_minute, id="fire_morning" )  # 早安
