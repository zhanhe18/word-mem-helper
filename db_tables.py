# -*- coding:utf-8 -*-
'''
Auth  : zhanhe18@gmail.com
Date  : 2020-08-25
Brief : 
'''
import datetime
import sqlalchemy
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime,Text,TIMESTAMP,ForeignKey

Base = declarative_base()


class Paragraph(Base):
    __tablename__ = "paragraph"
    id = Column(Integer,primary_key=True)
    text = Column(Text)
    created = Column(DateTime(timezone=True), default=datetime.now())
    modified = Column(DateTime(timezone=True), onupdate=datetime.now())
    doc = Column(Text)

class Word(Base):

    __tablename__ = "word"
    id = Column(Integer,primary_key=True)
    text = Column(String)
    created = Column(DateTime(timezone=True), default=datetime.now())
    modified = Column(DateTime(timezone=True), onupdate=datetime.now())
    lookup_time = Column(Integer,default=0)

class ParagraphWord(Base):
    __tablename__ = "paragraph_word"
    id = Column(Integer,primary_key=True)
    para_id = Column(Integer,ForeignKey("paragraph.id"))
    word_id = Column(Integer,ForeignKey("word.id"))

class Tag(Base):
    __tablename__ = "tag"
    id = Column(Integer,primary_key=True)
    text = Column(String)
    para_id = Column(Integer,ForeignKey("paragraph.id"),nullable=True)
    word_id = Column(Integer,ForeignKey("word.id"),nullable=True)
    created = Column(DateTime(timezone=True), default=datetime.now())
    modified = Column(DateTime(timezone=True), onupdate=datetime.now())


class Note(Base):
    __tablename__ = "note"
    id = Column(Integer,primary_key=True)
    text = Column(Text)
    created = Column(DateTime(timezone=True), default=datetime.now())
    modified = Column(DateTime(timezone=True), onupdate=datetime.now())
    word_id = Column(Integer,ForeignKey("word.id"))

