#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 22:48:55 2022

@author: tonydev_
"""

import datetime
import hashlib
import json
from flask import Flask, jsonify

#Part 1: Create blockchain

class Blockchain:
    
    def __init__(self):
        self.chain=[]
        self.create_block(proof=1, previous_hash='0')
        
    def create_block(self, proof, previous_hash):
        block={'index' : len(self.chain)+1,
               'timestamp' : str(datetime.datetime.now()),
               'proof' : proof,
               'previous_hash' : previous_hash}
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]
    
    
    
    
#Part 2: Blockchain minning