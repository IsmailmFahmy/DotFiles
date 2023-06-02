# Ismail Fahmy's Qtile config

from libqtile import bar, layout, widget, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy, LazyCall
from libqtile.utils import guess_terminal

powermenu = "rofi -show power-menu -modi power-menu:rofi-power-menu"
screenshot = "maim -s | xclip -selection clipboard -t image/png"
wallpaper_image = '~/Downloads/wallpaperflare.com_wallpaper.jpg'
mod = "mod4"
browser = "firefox"
terminal = guess_terminal()
keys = [
        # A list of available commands that can be bound to keys can be found
        # at https://docs.qtile.org/en/latest/manual/config/lazy.html

        # Open Browser
        Key([mod], "b", lazy.spawn(browser), desc="Open set browser"),
        Key([mod, "shift"], "s",lazy.spawn(f"kitty ls"  )),




        # Switch between windows
        Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
        Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

        # Move windows between left/right columns or move up/down in current stack.
        # Moving out of range in Columns layout will create new column.
        Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
        Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
        Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
        Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
        Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
        Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
        Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
        Key([mod, "control"], "left", lazy.layout.grow_left(), desc="Grow window to the left"),
        Key([mod, "control"], "right", lazy.layout.grow_right(), desc="Grow window to the right"),
        Key([mod, "control"], "down", lazy.layout.grow_down(), desc="Grow window down"),
        Key([mod, "control"], "up", lazy.layout.grow_up(), desc="Grow window up"),
        Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes
        Key(
            [mod, "shift"],
            "Return",
            lazy.layout.toggle_split(),
            desc="Toggle between split and unsplit sides of stack",
            ),
        Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
        # Toggle between different layouts as defined below
        Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
        Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
        Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
        Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
        Key([mod], "r", lazy.spawn("rofi -show run")),
        Key([mod, "shift"], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
        Key(["control", "mod1"], "delete", lazy.spawn(powermenu)),
        # MEDIA KEYS
        Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset Master 5%-"), desc="Lower Volume by 5%"),

        Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master 5%+"), desc="Raise Volume by 5%"),

        Key([], "XF86AudioMute", lazy.spawn("amixer sset Master 1+ toggle"), desc="Mute/Unmute Volume"),
        Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play/Pause player"),

        Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Skip to next"),

        Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Skip to previous"),


]


groups = [Group(i) for i in "123456789"]
for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

group_labels = ["", "", "", "", "﨣", "", "", ""]

groups.append(ScratchPad("scratchpad", [
    DropDown("term", "kitty --class=scratch", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.95),
    DropDown("ranger", "kitty --class=ranger -e ranger", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.95),
    DropDown("volume", "kitty --class=volume -e pulsemixer", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.95),
    DropDown("mus", "kitty --class=mus -e ncmpcpp", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.95),

]))

keys.extend([
    Key([mod], "t", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([mod], "e", lazy.group['scratchpad'].dropdown_toggle('ranger')),
    Key([mod], "v", lazy.group['scratchpad'].dropdown_toggle('volume')),
    Key([mod], "m", lazy.group['scratchpad'].dropdown_toggle('mus')),
])

colors = [["#91A2AA", "#91A2AA"], # 0
          ["#E86864", "#E86864"], # 1
          ["#282c34", "#282c34"], # 2
          ["#1c1f24", "#1c1f24"], # 3
          ["#dfdfdf", "#dfdfdf"], # 4
          ["#ff6c6b", "#ff6c6b"], # 5
          ["#98be65", "#98be65"], # 6
          ["#da8548", "#da8548"], # 7
          ["#51afef", "#51afef"], # 8
          ["#c678dd", "#c678dd"], # 9
          ["#46d9ff", "#46d9ff"], # 10
          ["#a9a1e1", "#a9a1e1"], # 11
          ["#282a36", "#282a36"], # 12
          ["#434758", "#434758"], # 13
          ["#ffffff", "#ffffff"], # 14
          ["#ff5555", "#ff5555"], # 15
          ["#8d62a9", "#8d62a9"], # 16
          ["#668bd7", "#668bd7"], # 17
          ["#e1acff", "#e1acff"]] # 18


layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": colors[6],
                "border_normal": "#1D2330",
                "font" : "JetBrainsMonoNerdFont"
                }


layouts = [
    layout.Columns(**layout_theme),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]









# =================================== BAR ===================================  
widget_defaults = dict(
    font="Caskaydia Cove Nerd Font Bold",
    # font = "JetBrainsMonoNerdFont Bold",
    fontsize=14,
    padding=8,
    background=colors[13],

)

extension_defaults = widget_defaults.copy()

screens = [
        Screen(
            top=bar.Bar(
                [
                    widget.Sep(
                        linewidth = 0,
                        padding = 6,
                        ),
                    widget.GroupBox(font="Ubuntu Bold",
                                    fontsize = 10,
                                    margin_y = 1,
                                    margin_x = 0,
                                    padding_y = 5,
                                    padding_x = 5,
                                    borderwidth = 3,
                                    highlight_method = "line",
                                    this_current_screen_border=colors[1],
                                    ),
                    widget.Sep(
                        linewidth = 0,
                        padding = 6,
                        ),

                    widget.Prompt(),
                    widget.WindowName(
                        format="{name}",
                        max_chars=90,
                        ),
                    widget.Battery(charge_char="󰂄", discharge_char="󰂍", empty_char="󱃍", format="{percent:2.0% {char}}"),
                    widget.Wlan(disconnected_message="󰖪",format='{essid} {percent:2.0%}'),
                    widget.ThermalZone(),
                    widget.Volume(
                        fmt="\uf026 {}",
                        mouse_callbacks={
                            "Button3": lambda: qtile.cmd_spawn("pavucontrol")
                            }
                        ),
                    widget.Systray(
                        icon_size=22,
                        margin=8,
                        padding=8
                        ),
                    widget.Clock(format="󰃭 %d/%m/%Y   %H:%M"),

                    # widget.CurrentLayout(),
                    # widget.WindowName(),
                    # widget.TextBox("default config", name="default"),
                    ],
                24,
                border_width=[2, 0, 2, 0],  # Draw top and bottom borders
                border_color=["#000000", "#000000", "#E86864", "#000000"]  # Borders are magenta
                ),
            # wallpaper = wallpaper_image,
            # wallpaper_mode = 'fill',
            ),
        ]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None
wmname = "LG3D"
