import importlib.resources
import logging
import random

import yaml


_logger = logging.getLogger(__name__)


quotes_stream = importlib.resources.open_text(__package__, "quotes.yaml")
quotes = yaml.load(quotes_stream, Loader=yaml.SafeLoader)["quotes"]


def get_quote() -> str:
    """return random Marvin quote"""

    _logger.info("Getting quote from Marvin")

    quote = random.choice(quotes)

    _logger.info(f"Got quote from Marvin (len={len(quote)})")

    return quote
