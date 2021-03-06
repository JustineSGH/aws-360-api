#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class Config(object):
    # Flask config
    VERSION = '2.00'
    BASE_DIR = os.path.abspath(os.path.dirname(__file__) + '../..')
    DEBUG = False
    TESTING = False
    THREADS_PER_PAGE = 2
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = 'ESek8UX78YbAiURX4HTb+La5JXYHmQ5KDKxCXBXXVqw'
    SECRET_KEY = 'vx5ZLhCWh7f0UAWEcu63ayWMpR/O9KcpKVPjWcZ2Q0g'

    # Specific App section

class DevelopmentConfig(Config):
    DEBUG = True
