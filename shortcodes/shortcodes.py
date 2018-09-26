# -*- coding: utf-8 -*-
from grow import extensions
from grow.documents import document
from grow.extensions import hooks


class ShortcodesPreRenderHook(hooks.PreRenderHook):
    """Handle the post-render hook."""

    def should_trigger(self, previous_result, doc, original_body, *_args,
                       **_kwargs):
        """Should the hook trigger with current document?"""
        return True

    def trigger(self, previous_result, doc, raw_content, *_args, **_kwargs):
        content = previous_result if previous_result else raw_content
        return content


class ShortcodesPostRenderHook(hooks.PostRenderHook):
    """Handle the post-render hook."""

    def should_trigger(self, previous_result, doc, original_body, *_args,
                       **_kwargs):
        """Should the hook trigger with current document?"""
        return True

    def trigger(self, previous_result, doc, raw_content, *_args, **_kwargs):
        content = previous_result if previous_result else raw_content
        return content

class ShortcodesExtension(extensions.BaseExtension):
    """Shortcodes Extension."""

    def __init__(self, pod, config):
        super(ShortcodesExtension, self).__init__(pod, config)

    @property
    def available_hooks(self):
        """Returns the available hook classes."""
        return [
            ShortcodesPreRenderHook,
            ShortcodesPostRenderHook,
        ]
