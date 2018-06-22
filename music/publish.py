# -*- coding: -utf8 -*-

import json
import os
import sys
import time

import shutil


def createFile(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False


def copyfile(copyPath, targetPath):
    shutil.copyfile(copyPath, targetPath)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    path = '/Users/huangxingwei/hxw-blog/source/music'
    configPath = path + '/music_config.json'

    # 创建文件夹
    createFile(path)
    # config.json 文件
    musicConfigFile = file(configPath)

    result = json.load(musicConfigFile)

    contentPath = path + '/' + result['music_name'] + '.md'
    # 创建md文件
    contentFile = file(contentPath, 'w+')
    # 写入markdown
    contentFile.write(
        '---\n' + 'title: ' + result['music_name'] + '\n' + "date: " + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                          time.localtime()) + '\n' + 'category:\n' + '\t - music' + '\n---')
    contentFile.write('\n\n\n')

    contentFile.write('![](' + result['music_icon'] + ')' + '\n\n\n')

    contentFile.write('### 歌手：' + result['music_author'] + '\n')
    contentFile.write('### 作曲：' + result['music_write_song'] + '\n')
    contentFile.write('### 作词：' + result['music_write_work'] + '\n\n\n\n')

    contentFile.write('---' + '\n\n\n')

    contentFile.write('<iframe name="music" src="http://link.hhtjim.com/163/')
    contentFile.write(result['music_id'] + '.mp3" ')
    contentFile.write(
        'marginwidth="1px" marginheight="10px" width=70% height="60px" frameborder=1 　scrolling="yes"></iframe>')
    contentFile.write('\n\n\n')

    contents = result['music_content']

    if (contents.find(',')):
        contentResult = contents.split(',')
        for str in contentResult:
            contentFile.write('**' + str + '**' + '\n\n\n')
    else:
        contentFile.write('**' + contents + '**')

    contentFile.flush()

    # copy文件到Hexo文件夹里面去
    publishMarkdownFile = '/' + result['music_name'] + '.md'
    publishFilePath = '/Users/huangxingwei/hxw-blog/source/_posts/' + publishMarkdownFile
    copyfile(contentPath, publishFilePath)

    #
    os.remove(contentPath)
