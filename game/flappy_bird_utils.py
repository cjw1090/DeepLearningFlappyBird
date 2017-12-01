#!/usr/bin/python
# -*- coding: 949 -*-
import pygame
import sys
def load():
    # 날개 위치가 조금씩 다른 사진들의 경로 
    PLAYER_PATH = (
            'assets/sprites/redbird-upflap.png',
            'assets/sprites/redbird-midflap.png',
            'assets/sprites/redbird-downflap.png'
    )

    # 배경의 경로
    BACKGROUND_PATH = 'assets/sprites/background-black.png'

    # 파이프 사진의 경로 
    PIPE_PATH = 'assets/sprites/pipe-green.png'

    IMAGES, SOUNDS, HITMASKS = {}, {}, {}

    # 점수를 보여주기 위해 투명도 올려서 점수를 사진을 저장  
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

    # 바닥의 배경 투명도를 올려서 load
    IMAGES['base'] = pygame.image.load('assets/sprites/base.png').convert_alpha()

    # 소리 
    if 'win' in sys.platform:
        soundExt = '.wav'
    else:
        soundExt = '.ogg'

    SOUNDS['die']    = pygame.mixer.Sound('assets/audio/die' + soundExt) # 죽었을 때 소리
    SOUNDS['hit']    = pygame.mixer.Sound('assets/audio/hit' + soundExt)    # 맞았을 때 
    SOUNDS['point']  = pygame.mixer.Sound('assets/audio/point' + soundExt)  # 뛸 때 나는 소리 
    SOUNDS['swoosh'] = pygame.mixer.Sound('assets/audio/swoosh' + soundExt) # 휙 하는 소리 
    SOUNDS['wing']   = pygame.mixer.Sound('assets/audio/wing' + soundExt) # 날개 

    # 배경 load
    IMAGES['background'] = pygame.image.load(BACKGROUND_PATH).convert()

    # 날개를 움직이는 모양을 하기 위해 날개 모양이 다른 사진을 투명도를 올려서 저장, 여기서 선택  
    IMAGES['player'] = (
        pygame.image.load(PLAYER_PATH[0]).convert_alpha(),
        pygame.image.load(PLAYER_PATH[1]).convert_alpha(),
        pygame.image.load(PLAYER_PATH[2]).convert_alpha(),
    )

    # 거꾸로 붙은 파이프와 일반 파이프를 선택 
    IMAGES['pipe'] = (
        pygame.transform.rotate(
            pygame.image.load(PIPE_PATH).convert_alpha(), 180),  
        pygame.image.load(PIPE_PATH).convert_alpha(),
    )

    # 파이프의 hitmask
    HITMASKS['pipe'] = (
        getHitmask(IMAGES['pipe'][0]),
        getHitmask(IMAGES['pipe'][1]),
    )

    # 플레이어(새)의 hitmask
    HITMASKS['player'] = (
        getHitmask(IMAGES['player'][0]),
        getHitmask(IMAGES['player'][1]),
        getHitmask(IMAGES['player'][2]),
    )

    return IMAGES, SOUNDS, HITMASKS


def getHitmask(image):
    # 파이프와 플레이어(새)가 어디있는지 알기 위하여 만든 함수 
    """returns a hitmask using an image's alpha."""
    mask = [] 
    # 이미지의 넓이만큼 계속한다
    for x in range(image.get_width()):  
        mask.append([]) # mask의 리스트 증가
        # 이미지의 높이만큼 계속한다.
        for y in range(image.get_height()): 
            mask[x].append(bool(image.get_at((x,y))[3]))
            # 단일 픽셀에서 색상값을 가져오는 것인데 이것이 있다면 true 추가 
    return mask
