#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2019/3/9

import sys

import pygame


def run_event():
    # 初始化屏幕
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('event key')
    bgcolor = (200, 200, 200)

    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type:
                print(pygame)
        # 渲染屏幕
        screen.fill(bgcolor)
        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_event()
