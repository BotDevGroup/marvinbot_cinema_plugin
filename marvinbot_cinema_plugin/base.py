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
            'base_url': 'http://cinema.com.do/'
        }

    def configure(self, config):
        self.config = config
        pass

    def setup_handlers(self, adapter):
        self.bot = adapter.bot
        self.add_handler(CommandHandler('cine', self.on_cine_command, command_description='Allow to see what movies are now playing'))


    def setup_schedules(self, adapter):
        pass
    
    def on_cine_command(self, update, *args, **kwargs):
        log.info('Reply command caught')
        message = get_message(update)
        url = self.config.get('base_url')
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        movies = soup.select("li.text-center.img-container")
        movie_list = []

        try:
            for num, movie in enumerate(movies, start=1):
                movie_detail = ('<a href="{}">Detalles</a>').format(url+movie.a['href'])
                #for futures implementations
                #movie_list.append(("{} - {}: 🎞 {}").format(num, movie.strong.string.encode('iso-8859-1').decode('utf8'), movie_detail))
                movie_list.append(("🎬 {}: {}").format(movie.strong.string.encode('iso-8859-1').decode('utf8'), movie_detail))
        except Exception as err:
            log.error("Parse error: {}".format(err))

        message.reply_text(text="\n".join(movie_list), parse_mode='HTML', disable_web_page_preview = True)
        
        
