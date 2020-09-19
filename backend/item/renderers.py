
import json
from rest_framework.renderers import JSONRenderer
import logging
import sys

class DishJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        try:
            logger = logging.getLogger('')
            return json.dumps({
                'status': 0,
                'dishes': data,
                'message': ''
            },ensure_ascii=False)
        except:
            function_name = sys._getframe().f_code.co_name
            log_message = function_name + '\n'\
                          + sys.exc_info()
            logger.error(log_message)
            return json.dumps({
                'status': 2,
                'dishes': [],
                'message': function_name + ' is failed'
            })

class InteriorJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    def render(self, data, accepted_media_type=None, renderer_context=None):
        try:
            logger = logging.getLogger('')
            return json.dumps({
                'status': 0,
                'interiors': data,
                'message': ''
            },ensure_ascii=False)
        except:
            function_name = sys._getframe().f_code.co_name
            log_message = function_name + '\n'\
                          + sys.exc_info()
            logger.error(log_message)
            return json.dumps({
                'status': 2,
                'interior': [],
                'interiors': [],
                'message': function_name + ' is failed'
            })

class SkillJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        try:
            logger = logging.getLogger('')
            return json.dumps({
                'status': 0,
                'skills': data,
                'message': ''
            },ensure_ascii=False)
        except:
            function_name = sys._getframe().f_code.co_name
            log_message = function_name + '\n'\
                          + sys.exc_info()
            logger.error(log_message)
            return json.dumps({
                'status': 2,
                'skills': [],
                'message': function_name + ' is failed'
            })

class SlideJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        try:
            logger = logging.getLogger('')
            return json.dumps({
                'status': 0,
                'slides': data,
                'message': ''
            },ensure_ascii=False)
        except:
            function_name = sys._getframe().f_code.co_name
            log_message = function_name + '\n'\
                          + sys.exc_info()
            logger.error(log_message)
            return json.dumps({
                'status': 2,
                'slides': [],
                'message': function_name + ' is failed'
            })

class WallpaperJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        try:
            logger = logging.getLogger('')
            return json.dumps({
                'status': 0,
                'wallpapers': data,
                'message': ''
            },ensure_ascii=False)
        except:
            function_name = sys._getframe().f_code.co_name
            log_message = function_name + '\n'\
                          + sys.exc_info()
            logger.error(log_message)
            return json.dumps({
                'status': 2,
                'wallpapers': [],
                'message': function_name + ' is failed'
            })

class WorkJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        try:
            logger = logging.getLogger('')
            return json.dumps({
                'status': 0,
                'works': data,
                'message': ''
            },ensure_ascii=False)
        except:
            function_name = sys._getframe().f_code.co_name
            log_message = function_name + '\n'\
                          + sys.exc_info()
            logger.error(log_message)
            return json.dumps({
                'status': 2,
                'works': [],
                'message': function_name + ' is failed'
            })