"""This file is used to import AppConfig and to further fulfil requirements for the login feature"""
from django.apps import AppConfig


class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
