from libqtile import widget
from settings import AppSettings


def build_thermal_widget(settings: AppSettings):
    return [
        widget.TextBox(
            "󱃂",
            font=settings.fonts.font_icon,
            fontsize=settings.fonts.font_icon_size,
            padding=2,
            foreground=settings.colors.get("fg_ligth_blue"),
        ),
        widget.ThermalSensor(
            font=settings.fonts.font_icon,
            fontsize=settings.fonts.font_icon_size,
            format="{temp:.0f}{unit} ",
            padding=2,
            foreground=settings.colors.get("fg_normal"),
        ),
    ]
