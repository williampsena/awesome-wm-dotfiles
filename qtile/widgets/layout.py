from libqtile import bar, widget
from libqtile.log_utils import logger
from settings import AppSettings


def build_current_layout_widget(settings: AppSettings):
    return widget.CurrentLayoutIcon(padding=5, scale=0.7)
