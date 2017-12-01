#!/usr/bin/python
# -*- coding: 949 -*-
import pygame
import sys
def load():
    # ���� ��ġ�� ���ݾ� �ٸ� �������� ��� 
    PLAYER_PATH = (
            'assets/sprites/redbird-upflap.png',
            'assets/sprites/redbird-midflap.png',
            'assets/sprites/redbird-downflap.png'
    )

    # ����� ���
    BACKGROUND_PATH = 'assets/sprites/background-black.png'

    # ������ ������ ��� 
    PIPE_PATH = 'assets/sprites/pipe-green.png'

    IMAGES, SOUNDS, HITMASKS = {}, {}, {}

    # ������ �����ֱ� ���� ���� �÷��� ������ ������ ����  
    IMAGES['numbers'] = (
        pygame.image.load('assets/sprites/0.png').convert_alpha(),
        pygame.image.load('assets/sprites/1.png').convert_alpha(),
        pygame.image.load('assets/sprites/2.png').convert_alpha(),
        pygame.image.load('assets/sprites/3.png').convert_alpha(),
        pygame.image.load('assets/sprites/4.png').convert_alpha(),
        pygame.image.load('assets/sprites/5.png').convert_alpha(),
        pygame.image.load('assets/sprites/6.png').convert_alpha(),
        pygame.image.load('assets/sprites/7.png').convert_alpha(),
        pygame.image.load('assets/sprites/8.png').convert_alpha(),
        pygame.image.load('assets/sprites/9.png').convert_alpha()
    )

    # �ٴ��� ��� ������ �÷��� load
    IMAGES['base'] = pygame.image.load('assets/sprites/base.png').convert_alpha()

    # �Ҹ� 
    if 'win' in sys.platform:
        soundExt = '.wav'
    else:
        soundExt = '.ogg'

    SOUNDS['die']    = pygame.mixer.Sound('assets/audio/die' + soundExt) # �׾��� �� �Ҹ�
    SOUNDS['hit']    = pygame.mixer.Sound('assets/audio/hit' + soundExt)    # �¾��� �� 
    SOUNDS['point']  = pygame.mixer.Sound('assets/audio/point' + soundExt)  # �� �� ���� �Ҹ� 
    SOUNDS['swoosh'] = pygame.mixer.Sound('assets/audio/swoosh' + soundExt) # �� �ϴ� �Ҹ� 
    SOUNDS['wing']   = pygame.mixer.Sound('assets/audio/wing' + soundExt) # ���� 

    # ��� load
    IMAGES['background'] = pygame.image.load(BACKGROUND_PATH).convert()

    # ������ �����̴� ����� �ϱ� ���� ���� ����� �ٸ� ������ ������ �÷��� ����, ���⼭ ����  
    IMAGES['player'] = (
        pygame.image.load(PLAYER_PATH[0]).convert_alpha(),
        pygame.image.load(PLAYER_PATH[1]).convert_alpha(),
        pygame.image.load(PLAYER_PATH[2]).convert_alpha(),
    )

    # �Ųٷ� ���� �������� �Ϲ� �������� ���� 
    IMAGES['pipe'] = (
        pygame.transform.rotate(
            pygame.image.load(PIPE_PATH).convert_alpha(), 180),  
        pygame.image.load(PIPE_PATH).convert_alpha(),
    )

    # �������� hitmask
    HITMASKS['pipe'] = (
        getHitmask(IMAGES['pipe'][0]),
        getHitmask(IMAGES['pipe'][1]),
    )

    # �÷��̾�(��)�� hitmask
    HITMASKS['player'] = (
        getHitmask(IMAGES['player'][0]),
        getHitmask(IMAGES['player'][1]),
        getHitmask(IMAGES['player'][2]),
    )

    return IMAGES, SOUNDS, HITMASKS


def getHitmask(image):
    # �������� �÷��̾�(��)�� ����ִ��� �˱� ���Ͽ� ���� �Լ� 
    """returns a hitmask using an image's alpha."""
    mask = [] 
    # �̹����� ���̸�ŭ ����Ѵ�
    for x in range(image.get_width()):  
        mask.append([]) # mask�� ����Ʈ ����
        # �̹����� ���̸�ŭ ����Ѵ�.
        for y in range(image.get_height()): 
            mask[x].append(bool(image.get_at((x,y))[3]))
            # ���� �ȼ����� ������ �������� ���ε� �̰��� �ִٸ� true �߰� 
    return mask
