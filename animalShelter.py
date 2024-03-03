#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 21:48:02 2024

@author: maryebierbaum_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32236
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print ("Connection Successful")

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            try:
                self.database.animals.insert_one(data)  # data should be dictionary
                return True
            except Exception as e:
                return False # returns False if create was not successful
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, data):
        try:
            found = self.database.animals.find(data)
            return found # if nothing is found, an empty string will return
        except Exception as e:
            raise Exception("An error has returned, please try again.") # error handling
            
# Method for U in CRUD - Update
    def update(self, query, update):
        # see how many documents are found with query
        count = self.database.animals.find(query).count()
        if count > 0:
            try:
                updated = self.database.animals.update_many(query, { "$set": update })
                return updated.modified_count
            except Exception as e:
                raise Exception("An error has returned, please try again.") # error handling
                
# Method for D in CRUD - Delete
    def delete(self, query):
        # see how many documents are found with query
        count = self.database.animals.find(query).count()
        if count > 1:
            try:
                deleted = self.database.animals.delete_many(query)
                return deleted.deleted_count
            except Exception as e:
                raise Exception("An error has returned, please try again.") # error handling
        