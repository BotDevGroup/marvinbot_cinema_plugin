# -*- coding: utf-8 -*-
from marvinbot.utils import localized_date, get_message
from marvinbot.handlers import CommandHandler, CallbackQueryHandler
from marvinbot.plugins import Plugin
from marvinbot.models import User

from bs4 import BeautifulSoup

import logging
import re
import requests

log = logging.getLogger(__name__)


class MarvinBotCinemaPlugin(Plugin):
    def __init__(self):
        super(MarvinBotCinemaPlugin, self).__init__('marvinbot_cinema_plugin')
        self.bot = None

    def get_default_config(self):
        return {
            'short_name': self.name,
            'enabled': True,
            'base_url': 'https://cinema.com.do/'
        }

    def configure(self, config):
        self.config = config
        pass

    def setup_handlers(self, adapter):
        self.bot = adapter.bot
        self.add_handler(CommandHandler('cine', self.on_cine_command, command_description='Allow to watch the movies availables'))


    def setup_schedules(self, adapter):
        pass
    
    def on_cine_command(self, update, *args, **kwargs):
        log.info('Reply command caught')
        message = get_message(update)
        r = requests.get("http://www.cinema.com.do/")
        soup = BeautifulSoup(r.text, 'html.parser')
        movies = soup.select("li.text-center.img-container")
        movie_list = []

        try:
            for num, movie in enumerate(movies, start=1):
                movie_list.append("{} - {}".format(num, movie.strong.string.encode('iso-8859-1').decode('utf8')))
        except Exception as err:
            log.error("Parse error: {}".format(err))

        message.reply_text(text="\n".join(movie_list), parse_mode='HTML') 

