# Ismail Fahmy's Qtile config

import os
import subprocess
from libqtile import bar, layout, widget, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import LazyCall, lazy
from libqtile.utils import guess_terminal

# import os
# import subprocess
# from typing import List  # noqa: F401
# from libqtile import bar, layout, widget
# from libqtile import hook



#---------------#
#   SUPER KEY   #
#---------------#

mod = "mod4"

#---------------#
# MISCELLANEOUS #
#---------------#
def powermenu_key(qtile):
    script = os.path.expanduser('~/.config/rofi/powermenu')
    subprocess.call([script])


# Clipboard = """rofi -modi "clipboard:greenclip print" -show clipboard -run-command '{cmd}'"""
# screenshot = "flameshot gui -s -c"
# wallpaper_image = '~/Downloads/wallpaperflare.com_wallpaper.jpg'
# browser = "firefox"
# whatsapp = 'firefox --new-window "https://web.whatsapp.com/"'
# terminal = guess_terminal()


#---------------#
#   KEYBINDINGS #
#---------------#

keys = [

        # Open Browser
        # Key([mod], "b", lazy.spawn(browser), desc="Open set browser"),

        # Take a screenshot
        # Key([mod, "shift"], "s",lazy.spawn(screenshot)),

        # Open Whatsapp
        # Key([mod, "shift"], "w",lazy.spawn(whatsapp)),

        # Open Clipboard manager
        # Key([mod], "c",lazy.spawn(Clipboard)),

        # File Manager
        # Key([mod, "shift"], "e",lazy.spawn("thunar")),

        # Run
        # Key([mod], "r", lazy.spawn("rofi -show run")),
        Key([mod, "shift"], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

        # Power Menu
        # Key(["control", "mod1"], "delete", lazy.function(powermenu_key) ),


        # Switch between windows
        Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
        Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

        Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
        Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
        # Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

        #
        #
        # # Move windows between left/right columns or move up/down in current stack.
        # # Moving out of range in Columns layout will create new column.
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
    Key([mod, "shift"], "t",    lazy.window.toggle_floating(), desc='Toggle floating'),
    Key([mod], "f",             lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window" ),

    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    # Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # 
    # # Media Keys
    # Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play/Pause player"),
    # Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Skip to next"),
    # Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Skip to previous"),
    #
    # #---    Brightness    ---#
    # Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 10")),
    # Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 10")),
    # 
    # #---    Sleep machine ---#
    # Key([], "XF86Sleep", lazy.spawn("systemctl suspend")),
    # 
    # #---    Volume        ---#
    # Key([mod], "o", lazy.function(volume_set,"up")),
    # Key([], "XF86AudioRaiseVolume", lazy.function(volume_set,"up")),
    # Key([], "XF86AudioLowerVolume", lazy.function(volume_set,"down")),
    # Key([], "XF86AudioMute", lazy.function(volume_set, "mute")),
    # # Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    # # Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    # # Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    #
    #
    # # ScratchPads
    Key([mod], "t", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([mod], "e", lazy.group['scratchpad'].dropdown_toggle('lf')),
    Key(["control", "shift"], "Escape", lazy.group['scratchpad'].dropdown_toggle('btop')),
    # Key([mod], "v", lazy.group['scratchpad'].dropdown_toggle('volume')),
    # Key([mod], "m", lazy.group['scratchpad'].dropdown_toggle('mus')),
    #
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
    DropDown("term", "kitty --class=scratch", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.95, on_focus_lost_hide=False),
    DropDown("lf", "kitty --class=lf -e lf", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.95, on_focus_lost_hide=False),
    DropDown("volume", "kitty --class=volume -e pulsemixer", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.95, on_focus_lost_hide=False),
    # DropDown("mus", "kitty --class=mus -e ncmpcpp", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.95, on_focus_lost_hide=False),
    DropDown("btop", "kitty btop", width=0.55, height=0.8, x=0.22, y=0.1, opacity=0.95, on_focus_lost_hide=False),
    DropDown("pavu", "pavucontrol", width=0.4, height=0.4, x=0.55, y=0.005, opacity=0.95, on_focus_lost_hide=True),
    DropDown("calender", "kitty --hold -e cal", width=0.106, height=0.16, x=0.8595, y=0.005, opacity=0.95, on_focus_lost_hide=False),
    ]))

# colors = [["#91A2AA", "#91A2AA"], # 0
#           ["#E86864", "#E86864"], # 1
#           ["#282c34", "#282c34"], # 2
#           ["#1c1f24", "#1c1f24"], # 3
#           ["#dfdfdf", "#dfdfdf"], # 4
#           ["#ff6c6b", "#ff6c6b"], # 5
#           ["#98be65", "#98be65"], # 6
#           ["#da8548", "#da8548"], # 7
#           ["#51afef", "#51afef"], # 8
#           ["#c678dd", "#c678dd"], # 9
#           ["#46d9ff", "#46d9ff"], # 10
#           ["#a9a1e1", "#a9a1e1"], # 11
#           ["#282a36", "#282a36"], # 12
#           ["#434758", "#434758"], # 13
#           ["#ffffff", "#ffffff"], # 14
#           ["#ff5555", "#ff5555"], # 15
#           ["#8d62a9", "#8d62a9"], # 16
#           ["#668bd7", "#668bd7"], # 17
#           ["#e1acff", "#e1acff"]] # 18
#
colors =  [
        ["#00000000", "#00000000", "#00000000"],     # color 0
        ["#2e3440", "#2e3440", "#2e3440"], # color 1
        ["#B591B0", "#B591B0", "#B591B0"], # color 2
        ["#A480B2", "#A480B2", "#A480B2"], # color 3
        ["#aed1dc", "#98B7C0", "#aed1dc"], # color 4
        ["#f3f4f5", "#f3f4f5", "#f3f4f5"], # color 5
        ["#bb94cc", "#AB87BB", "#bb94cc"], # color 3
        ["#81658C", "#81658C", "#81658C"], # color 6
        ["#614C69", "#614C69", "#614C69"], # color 8
        ["#0ee9af", "#0ee9af", "#0ee9af"], # color 9
        ["#5aec79", "#5aec79", "#5aec79"]] # color 10

layout_theme = {"border_width": 2,
                "margin": 4,
                "border_focus": colors[9],
                "border_normal": "#1D2330",
                "font" : "JetBrainsMonoNerdFont"
                }


layouts = [
        layout.Columns(**layout_theme),
        layout.Max(),
        ]











# =================================== BAR ===================================  
widget_defaults = dict(
        font="Caskaydia Cove Nerd Font Bold",
        # font = "JetBrainsMonoNerdFont Bold",
        fontsize=14,
        padding=8,
        background=colors[3],

        )

extension_defaults = widget_defaults.copy()

# screens = [
#         Screen(
#             top=bar.Bar(
#                 [
#                 widget.Sep(
#                         linewidth = 0,
#                         padding = 6,
#                         ),
#                widget.GroupBox(font="Ubuntu Bold",
#                         # fontsize = 10,
#                        fontsize=13,
#                        margin_y=4,
#                        margin_x=4,
#                        padding_y=5,
#                        padding_x=3,
#                        borderwidth=7,
#                        highlight_method="block",
#                         this_current_screen_border=colors[1],
#                        rounded=True,
#                         ),
#                 widget.Sep(
#                         linewidth = 0,
#                         padding = 6,
#                         ),
#
#                     widget.Prompt(),
#                     widget.WindowName(
#                         format="{name}",
#                         max_chars=90,
#                         ),
#                     widget.Volume(
#                         fmt="\uf026 {}",
#                         mouse_callbacks={
#                             "Button3": lambda: qtile.cmd_spawn("pulsemixer")
#                             }
#                         ),
#                     widget.Systray(
#                         icon_size=22,
#                         margin=8,
#                         padding=8
#                         ),
#                     widget.Net(
#                         interface="enp1s0",
#                         format=" {interface}: {down} ↓↑ {up}",
#                         background="#9ccfd8",
#                         foreground="#191724",
#                         update_interval=1.0
#                         ),
#
#                     widget.Clock(format="󰃭 %d/%m/%Y   %H:%M"),
#
#                     # widget.CurrentLayout(),
#                     # widget.WindowName(),
#                     # widget.TextBox("default config", name="default"),
#                     ],
#                 24,
#                 border_width=[2, 0, 2, 0],  # Draw top and bottom borders
#                 border_color=["#000000", "#000000", "#E86864", "#000000"]  # Borders are magenta
#                 ),
#             # wallpaper = wallpaper_image,
#             # wallpaper_mode = 'fill',
#             ),
#
# ]

# Shutdown
def shutdown_now():
    qtile.cmd_spawn('shutdown now')
# Reboot
def reboot_now():
    qtile.cmd_spawn('reboot')
# Brightness Up 
def brightup():
    qtile.cmd_spawn('brightnessctl set +5%')
# Brightness Down
def brightdown():
    qtile.cmd_spawn('brightnessctl set 5%-')
def powermenu():
    script = os.path.expanduser('~/.config/rofi/powermenu')
    subprocess.call([script])


screens = [
        Screen(
            top=bar.Bar(
                [
                    widget.Spacer(
                        length = 6,
                        background = colors[0],
                        ),                
                    widget.GroupBox(
                        fontsize = 20,
                        margin_x = 1,
                        margin_y = 4,
                        padding_y = 0,
                        padding_x = 1,
                        borderwidth = 2.5,
                        active = colors[2],
                        inactive = colors[1],
                        rounded = True,
                        highlight_color = colors[0],
                        highlight_method = "line",
                        this_current_screen_border = colors[8],
                        this_screen_border = colors [0],
                        foreground = colors[2],
                        center_aligned = True,
                        disable_drag = True,
                        background = colors[0]
                        ),
                    widget.Systray(
                        background = colors[0],
                        icon_size = 16,
                        foreground = colors[1],
                        padding = 3),
                    widget.Spacer(
                        background = colors[0],
                        ),
                    widget.TextBox(
                        text=' ',
                        foreground = colors[2],
                        background = colors[0],
                        fontsize = 18,
                        padding = 0,
                        mouse_callbacks = {'Button1': lazy.group['scratchpad'].dropdown_toggle('pavu')},
                        ),
                    widget.PulseVolume(
                        background = colors[0],
                        foreground = colors[2],
                        limit_max_volume = True,
                        padding_y = 1,
                        fontsize = 14
                        ),
                    widget.TextBox(
                        text='⏽',
                        background = colors[0],
                        foreground = colors[8],
                        fontsize = 35,
                        padding = 2
                        ),
              widget.TextBox(
                      text=' ',
                      background = colors[0],
                      foreground = colors[2],
                      fontsize = 18,
                      padding = 1,
                      mouse_callbacks = {'Button1': lazy.group['scratchpad'].dropdown_toggle('btop')},
                      ),
              widget.Memory(
                      background = colors[0],
                      foreground = colors[2],
                      format = '{MemUsed: .0f}{mm} /{MemTotal: .0f}{mm}',
                      padding = 0,
                      fontsize = 14
                      ),
              widget.TextBox(
                      text='⏽',
                      background = colors[0],
                      foreground = colors[8],
                      fontsize = 35,
                      padding = 2
                      ),

              #   text='',
              #   background = colors[0],
              #   foreground = colors[2],
              #   fontsize = 27,
              #   padding = 0,
              #   ),
              # widget.Battery(
              #   background = colors[0],
              #   foreground = colors[2],
              #   format = '{percent:2.0%}',
              #   full_char = "100%",
              #   update_interval = 1,
              #   fontsize = 12,
              #   ),
              # widget.TextBox(
              #   text='⏽',
              #   background = colors[0],
              #   foreground = colors[8],
              #   fontsize = 35,
              #   padding = 2
              #   ),

             # widget.Wlan(
             #        disconnected_message = '',
             #        background = colors[0],
             #        foreground = colors[2],
             #        format = ' {percent:2.0%}',
             #        fontsize = 12,
             #         ),
             #
              # widget.TextBox(
              #   text='⏽',
              #   background = colors[0],
              #   foreground = colors[8],
              #   fontsize = 35,
              #   padding = 2
              #   ),

             widget.TextBox(
                     text=' ',
                     foreground = colors[2],
                     background = colors[0],
                     fontsize = 18,
                     padding = 1,
                     ),
             widget.Clock(
                     format='%H:%M',
                     foreground = colors[2],
                     background = colors[0],
                     fontsize = 14,
                     ),
             widget.TextBox(
                     text='⏽',
                     background = colors[0],
                     foreground = colors[8],
                     fontsize = 35,
                     padding = 2
                     ),
             widget.TextBox(
                     text='󰃭 ',
                     foreground = colors[2],
                     background = colors[0],
                     fontsize = 18,
                     padding = 1,
                     mouse_callbacks = {'Button1': lazy.group['scratchpad'].dropdown_toggle('calender')},
                     ),
             widget.Clock(
                     format='%d/%m/%Y',
                     foreground = colors[2],
                     background = colors[0],
                     fontsize = 14,
                     ),
             widget.TextBox(
                     text='⏽',
                     background = colors[0],
                     foreground = colors[8],
                     fontsize = 35,
                     padding = 2
                     ),
             widget.TextBox(
                     text=' ',
                     foreground = colors[2],
                     background = colors[0],
                     fontsize = 16,
                     padding = 1,
                     mouse_callbacks = {'Button1': powermenu},
                     ),
             widget.Spacer(
                     length = 6,
                     background = colors[0],
                     ),                
             ],
            25,
            margin = [0,0,0,0],
        ),
    ),
]



# Drag floating layouts.
#-----------------------#
#   FLOATING WINDOWS    #
#-----------------------#

mouse = [
        Drag([mod], "Button1", lazy.window.set_position_floating(),
             start=lazy.window.get_position()),
        Drag([mod], "Button3", lazy.window.set_size_floating(),
             start=lazy.window.get_size()),
        Click([mod], "Button2", lazy.window.bring_to_front()),
        ]
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
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
            ],
        border_focus="#9ccfd8",
        border_normal="#31748f"
        )
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True



# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None
wmname = "LG3D"
