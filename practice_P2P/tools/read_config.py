#!/usr/bin/python
#-*- coding:utf-8 -*-
#@Author：zhuxiujie

import configparser

class ReadConfig:

    @staticmethod
    def get_config(file_path,section,option):
        cf = configparser.ConfigParser()
        cf.read(file_path,encoding='utf-8')
        return cf[section][option]

if __name__ == '__main__':
    from practice_P2P.tools import project_path
    print(eval(ReadConfig.get_config(project_path.test_config_path,'DATABASE','user')))