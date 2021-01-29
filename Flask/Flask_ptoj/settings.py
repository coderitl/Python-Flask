# -*- coding:utf-8 -*-
class Config:
    ENV = 'development'
    DEBUG = True
    # mysql+pymysql://user:password@hostip:port/databasename
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0,0,1:3306/student'
    SQLALCHEMY_TRACK_MODIFICATIONS = False