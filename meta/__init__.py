from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app,db)

    from . import model
    from meta.model import Naver

    @app.route('/') #127.0.0.1:5000/
    def index():
        blog1 = Naver(title='블로그1 제목', description='블로그1 내용')
        print(blog1.title)
        print(blog1.description)
        db.session.add(blog1)
        db.session.commit()
        return 'index page'

    @app.route('/getdb')
    def getdb():
        '''
        naverdata = Naver.query.all() #전부 가져오기
        print(len(naverdata))

        for temp in naverdata:
            print(temp.id)
            print(temp.title)
            print(temp.description)
            print('-'*20)

        return 'getdb'
        '''
        '''
        result = Naver.query.filter(Naver.id==3).all() #조건에 맞는 값 가져오기
        for temp in result:
            print(temp.id)
            print(temp.title)
            print(temp.description)
            print('-'*20)

        return 'getdb'
        '''
        '''
        result = Naver.query.get(1) # 유일값 가져오기
        print(result.title)
        return 'getdb'
        '''
        '''
        result = Naver.query.filter(Naver.title.like('%블로그%')).all() #특정 단어 있는 값 가져오기
        for temp in result:
            print(temp.id)
            print(temp.title)
            print(temp.description)
            print('-'*20)
        return 'getdb'
        '''
        '''
        result = Naver.query.get(1) # db값 삭제
        db.session.delete(result)
        db.session.commit()
        return 'getdb'
        '''

        result = Naver.query.get(2) # db값 수정
        result.title = '블로그 제목 수정 2번'
        db.session.commit()
        return 'getdb'

    return app