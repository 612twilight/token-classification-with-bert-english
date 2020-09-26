#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : config.py
@Author: gaoyongwei
@Date  : 2020/9/20 14:44
@Desc  : 
"""

import os

if os.name == "nt":
    bert_model_dir = "E:\pretrainmodel/trainsformers/pytorchversion/bert-base-english"
else:
    bert_model_dir = ""  # 服务器上模型地址
