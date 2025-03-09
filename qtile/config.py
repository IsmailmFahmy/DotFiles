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
from libqtile import hook

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home]) 

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
    Key([mod], "k", lazy.group['scratchpad'].dropdown_toggle('keyboard')),
    Key([mod], "n", lazy.group['scratchpad'].dropdown_toggle('though_bursts')),
    Key([mod], "e", lazy.group['scratchpad'].dropdown_toggle('lf')),
    Key(["control", "shift"], "Escape", lazy.group['scratchpad'].dropdown_toggle('btop')),
    # Key([mod], "v", lazy.group['scratchpad'].dropdown_toggle('volume')),
    Key([mod], "m", lazy.group['scratchpad'].dropdown_toggle('music')),
    # Key([mod], "u", lazy.group['scratchpad'].dropdown_toggle('ramboxx')),
    #
]



# groups = [Group(i) for i in "123456789"]
groups = [
    Group("1", label="  "),  # Add other groups similarly
    Group("2", label="  ", matches=[Match(wm_class="firefox")]),  # Add firefox to group 8
    Group("3", label="  "),
    Group("4", label=" 4 "),
    Group("5", label=" 5"),
    Group("6", label=" 6 "),
    Group("7", label="  "),
    Group("8", label="  ", matches=[Match(wm_class="obsidian")]),  # Add Obsidian to group 8
    Group("9", label=" 9 ", matches=[Match(wm_class="rambox")]),  # Add Rambox to group 9
]

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
    DropDown("keyboard", "feh /home/fahmy/.local/German_Keyboard.png", width=0.38, height=0.31, x=0.3, y=0.3, opacity=1, on_focus_lost_hide=False),
    DropDown("though_bursts", 'alacritty -e "nvim ~/Documents/Obsidian/Thought_Bursts.md"', width=0.38, height=0.9, x=0.6, y=0.05, opacity=0.95, on_focus_lost_hide=False),
    DropDown("lf", "kitty --class=lf -e lf", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.95, on_focus_lost_hide=False),
    DropDown("volume", "kitty --class=volume -e pulsemixer", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.95, on_focus_lost_hide=False),
    DropDown("music", "spotify", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.95, on_focus_lost_hide=False),
    # DropDown("ramboxx", "rambox", width=0.99, height=0.99, x=0.005, y=0.0045, opacity=0.95, on_focus_lost_hide=False),
    DropDown("btop", "kitty btop", width=0.6, height=0.8, x=0.2, y=0.1, opacity=0.95, on_focus_lost_hide=False),
    DropDown("pavu", "pavucontrol", width=0.4, height=0.4, x=0.55, y=0.000, opacity=0.95, on_focus_lost_hide=True),
    DropDown("calender", "alacritty --hold -e cal", width=0.156, height=0.16, x=0.84, y=0.005, opacity=0.95, on_focus_lost_hide=False),
    ]))

colors =  [
            ["#000000", "#000000", "#000000"],  # color 0
            ["#2e3440", "#2e3440", "#2e3440"],  # color 1
            ["#B591B0", "#B591B0", "#B591B0"],  # color 2
            ["#A480B2", "#A480B2", "#A480B2"],  # color 3
            ["#aed1dc", "#98B7C0", "#aed1dc"],  # color 4
            ["#f3f4f5", "#f3f4f5", "#f3f4f5"],  # color 5
            ["#bb94cc", "#AB87BB", "#bb94cc"],  # color 3
            ["#81658C", "#81658C", "#81658C"],  # color 6
            ["#614C69", "#614C69", "#614C69"],  # color 8
            ["#0ee9af", "#0ee9af", "#0ee9af"],  # color 9
            ["#5aec79", "#5aec79", "#5aec79"],  # color 10
            ["#91A2AA", "#91A2AA"],             # color 11
            ["#E86864", "#E86864"],             # color 12
            ["#282c34", "#282c34"],             # color 13
            ["#1c1f24", "#1c1f24"],             # color 14
            ["#dfdfdf", "#dfdfdf"],             # color 15
            ["#ff6c6b", "#ff6c6b"],             # color 16
            ["#98be65", "#98be65"],             # color 17
            ["#da8548", "#da8548"],             # color 18
            ["#51afef", "#51afef"],             # color 19
            ["#c678dd", "#c678dd"],             # color 20
            ["#46d9ff", "#46d9ff"],             # color 21
            ["#a9a1e1", "#a9a1e1"],             # color 22
            ["#282a36", "#282a36"],             # color 23
            ["#434758", "#434758"],             # color 24
            ["#ffffff", "#ffffff"],             # color 25
            ["#ff5555", "#ff5555"],             # color 26
            ["#8d62a9", "#8d62a9"],             # color 27
            ["#668bd7", "#668bd7"],             # color 28
            ["#e1acff", "#e1acff"]]             # color 29


bg = 24
fg = 25
bar_color = 28


layout_theme = {"border_width": 4,
                "margin": 6,
                "border_focus": colors[9],
                "border_normal": "#1D2330",
                "font" : "JetBrainsMonoNerdFont"
                }


layouts = [
        layout.Columns(**layout_theme),
        layout.Max(),
        ]




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








# =================================== BAR ===================================  
widget_defaults = dict(
        font="Caskaydia Cove Nerd Font Bold",
        # font = "JetBrainsMonoNerdFont Bold",
        fontsize=28,
        padding=16,
        background=colors[3],
        )


extension_defaults = widget_defaults.copy()



screens = [
        Screen(
            top=bar.Bar(
                [
                    widget.Spacer(
                        length = 6,
                        background = colors[bg],
                        ),                
                    widget.GroupBox(
                        fontsize = 40,
                        margin_x = 2,
                        margin_y = 8,
                        padding_y = 0,
                        padding_x = 2,
                        borderwidth = 5,
                        active = colors[fg],
                        inactive = colors[1],
                        rounded = True,
                        highlight_color = colors[bg],
                        highlight_method = "line",
                        this_current_screen_border = colors[bar_color],
                        this_screen_border = colors[bg],
                        foreground = colors[fg],
                        center_aligned = True,
                        disable_drag = True,
                        background = colors[bg]
                        ),
                    widget.Spacer(
                        background = colors[bg],
                        ),
                    widget.Systray(
                        background = colors[bg],
                        icon_size = 32,
                        foreground = colors[fg],
                        padding = 6
                        ),
                    widget.TextBox(
                        text='⏽',
                        background = colors[bg],
                        foreground = colors[bar_color],
                        fontsize = 70,
                        padding = 4
                        ),
                    widget.TextBox(
                        text=' ',
                        foreground = colors[fg],
                        background = colors[bg],
                        fontsize = 36,
                        padding = 0,
                        mouse_callbacks = {'Button1': lazy.group['scratchpad'].dropdown_toggle('pavu')},
                        ),
                    widget.Volume(
                        background = colors[bg],
                        foreground = colors[fg],
                        limit_max_volume = True,
                        padding_y = 2,
                        fontsize = 28
                        ),
                    widget.TextBox(
                        text='⏽',
                        background = colors[bg],
                        foreground = colors[bar_color],
                        fontsize = 70,
                        padding = 4
                        ),
              # widget.TextBox(
              #         text=' ',
              #         background = colors[bg],
              #         foreground = colors[fg],
              #         fontsize = 36,
              #         padding = 2,
              #         mouse_callbacks = {'Button1': lazy.group['scratchpad'].dropdown_toggle('btop')},
              #         ),
              # widget.Memory(
              #         background = colors[bg],
              #         foreground = colors[fg],
              #         format = '{MemUsed: .0f}{mm} /{MemTotal: .0f}{mm}',
              #         padding = 0,
              #         fontsize =28 
              #         ),
              # widget.TextBox(
              #         text='⏽',
              #         background = colors[bg],
              #         foreground = colors[bar_color],
              #         fontsize = 70,
              #         padding = 4
              #         ),

                widget.BatteryIcon(
                        theme_path='~/.config/qtile/Assets/Battery/',
                        background = colors[bg],
                        foreground = colors[fg],
                        scale=0.7,
                        ),

                widget.Battery(
                        background = colors[bg],
                        foreground = colors[fg],
                        format = '{percent:2.0%}',
                        full_char = "100%",
                        update_interval = 1,
                        fontsize = 24,
                        ),

                widget.TextBox(
                        text='⏽',
                        background = colors[bg],
                        foreground = colors[bar_color],
                        fontsize = 70,
                        padding = 4
                        ),

                # widget.Wlan(
                #         disconnected_message = '󰖪 ',
                #         interface="wlan0",
                #         ethernet_interface = 'enp4s0f4u1u3',
                #         use_ethernet = True,
                #         ethernet_message = '󰈁 ',
                #         background = colors[bg],
                #         foreground = colors[fg],
                #         format = '  {percent:2.0%}',
                #         ),
                #
                # widget.TextBox(
                #         text='⏽',
                #         background = colors[bg],
                #         foreground = colors[bar_color],
                #         fontsize = 70,
                #         padding = 4
                #         ),

                widget.TextBox(
                        text=' ',
                        foreground = colors[fg],
                        background = colors[bg],
                        fontsize = 36,
                        padding = 2,
                        ),

                widget.Clock(
                        format='%H:%M',
                        foreground = colors[fg],
                        background = colors[bg],
                        fontsize = 28,
                        ),

                widget.TextBox(
                        text='⏽',
                        background = colors[bg],
                        foreground = colors[bar_color],
                        fontsize = 70,
                        padding = 4
                        ),
                
                widget.TextBox(
                        text='󰃭 ',
                        foreground = colors[fg],
                        background = colors[bg],
                        fontsize = 36,
                        padding = 2,
                        mouse_callbacks = {'Button1': lazy.group['scratchpad'].dropdown_toggle('calender')},
                        ),

                widget.Clock(
                        format='%d/%m',
                        #format='%d/%m/%Y',
                        foreground = colors[fg],
                        background = colors[bg],
                        fontsize = 28,
                        ),

                widget.TextBox(
                        text='⏽',
                        background = colors[bg],
                        foreground = colors[bar_color],
                        fontsize = 70,
                        padding = 4
                        ),

                widget.TextBox(
                        text=' ',
                        foreground = colors[fg],
                        background = colors[bg],
                        fontsize = 32,
                        padding = 2,
                        mouse_callbacks = {'Button1': powermenu},
                        ),

                widget.Spacer(
                        length = 12,
                        background = colors[bg],
                        ),                
             ],
            50,
            margin = [8,50,8,50],
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
dgroups_app_rules = []
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
