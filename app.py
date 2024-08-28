#!/usr/bin/env python3

from flask import Flask
app = Flask.app()
app.run(8088)

class APP():
    def init(self):
        self.port = 8088