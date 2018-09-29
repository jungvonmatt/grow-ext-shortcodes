# grow-ext-shortcodes
Extension for [Grow](https://github.com/grow/grow) allowing markdown documents to have BBCode styled shortcodes to be a bit more flexible and consistent with the default markdown syntax rather than having to fallback to {% callouts %}.

## Concept
The extension works by looking for a `shortcodes` Python package inside your Grow pod. All contained modules get automatically imported and are searched for a module-level variable `shortcode` which should hold a class that is inheriting from `shortcodes.Shortcode` just like this:

```python
from shortcodes import Shortcode

class StageShortcode(Shortcode):
    name = 'stage'
    prerender_markdown = True
    template = 'partials/stage.j2'

shortcode = StageShortcode
```

Please see `shortcodes.Shortcode` or one of the examples for all the available hooks and functions.

## Usage
### Initial setup
1. Create an `extensions.txt` file within your pod.
1. Add to the file: `git+git://github.com/jungvonmatt/grow-ext-shortcodes`
1. Run `grow install`.
1. Add the following section to `podspec.yaml`:

```
ext:
- extensions.shortcodes.ShortcodesExtension
```
