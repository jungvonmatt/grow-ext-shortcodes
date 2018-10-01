# -*- coding: utf-8 -*-
import os
import pkgutil
import sys

import bbcode
from grow import extensions
from grow.documents import document
from grow.extensions import hooks

SHORTCODES_DIR = 'shortcodes'

class ShortcodesPreRenderHook(hooks.PreRenderHook):
    """Handle the post-render hook."""

    def should_trigger(self, previous_result, doc, original_body, *_args,
                       **_kwargs):
        """Only trigger for non-empty documents"""
        # TODO: This is extremly ugly but without it Grow will cache
        # the result of rendered shortcodes
        doc.pod.podcache.reset()
        if original_body is not None:
            return True
        else:
            return False

    def trigger(self, previous_result, doc, raw_content, *_args, **_kwargs):
        content = previous_result if previous_result else raw_content

        return self.extension.parser.format(content, doc=doc)


class ShortcodesExtension(extensions.BaseExtension):
    """Shortcodes Extension."""

    def __init__(self, pod, config):
        super(ShortcodesExtension, self).__init__(pod, config)
        self.parser = bbcode.Parser(newline='\n', install_defaults=False, escape_html=False, replace_links=False)
        self.shortcodes = []

        self.load_shortcodes()

        # After init write extension to pod to have it widely available
        setattr(pod, 'shortcodes', self)

    def load_shortcodes(self):
        """Verifies the pod has a shortcode module and loads all shortcodes"""
        shortcodes_path = '{}/{}'.format(self.pod.root, SHORTCODES_DIR)
        if os.path.exists(shortcodes_path + '/__init__.py'):
            for importer, package_name, _ in pkgutil.iter_modules([shortcodes_path]):
                full_package_name = '{}.{}'.format(shortcodes_path, package_name)
                if full_package_name not in sys.modules:
                    module = importer.find_module(package_name).load_module(package_name)
                    self.register_shortcode(module)
        else:
            self.pod.logger.warning('There is no shortcode package in this pod')

    def register_shortcode(self, module):
        """Checks if a loaded module exports a shortcode class and if so instantiates
        one and tries to register it with the BBCode parser"""
        if module.shortcode:
            shortcode = module.shortcode(self.pod)
            self.shortcodes.append(shortcode)
            shortcode.register(self.parser)

    @property
    def available_hooks(self):
        """Returns the available hook classes."""
        return [
            ShortcodesPreRenderHook,
        ]
