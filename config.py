# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os
import re
import subprocess
import socket
from libqtile.config import Key, Screen, Group, Drag, Click, Rule
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
#from libqtile.widget import Spacer
#import arcomemory

#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

keys = [

# FUNCTION KEYS

    Key([], "F12", lazy.spawn('jgmenu_run')),

# SUPER + FUNCTION KEYS

    Key([mod], "e", lazy.spawn('atom')),
    Key([mod], "c", lazy.spawn('conky-toggle')),
#    Key([mod], "d", lazy.spawn("dmenu_run -i -fn 'JetBrains Mono Medium:size=11' -nb '#2F343F' -nf 'white' -sb '#5294E2' -sf 'white'")),
    Key([mod], "d", lazy.spawn("dmenu_run -i -fn 'Ubuntu Mono:size=16:style=Bold' -nb '#1b1e2b' -nf 'white' -sb '#0099ff' -sf 'white'")),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod], "r", lazy.spawn('rofi-theme-selector')),
    Key([mod], "v", lazy.spawn('pavucontrol')),
    Key([mod], "x", lazy.spawn('oblogout')),
    Key([mod], "Escape", lazy.spawn('xkill')),
    Key([mod], "Return", lazy.spawn('urxvt')),
    Key([mod], "KP_Enter", lazy.spawn('st')),
    Key([mod], "F1", lazy.spawn('chromium -no-default-browser-check')),
    Key([mod], "F2", lazy.spawn('code')),
    Key([mod], "F6", lazy.spawn('vlc --video-on-top')),
    Key([mod], "F7", lazy.spawn('virtualbox')),
    Key([mod], "F8", lazy.spawn('thunar')),
    Key([mod], "F10", lazy.spawn("spotify")),
    Key([mod], "F11", lazy.spawn('rofi -show run -fullscreen')),
    Key([mod], "F12", lazy.spawn('rofi -show run')),
#    Key([mod], "Tab", lazy.screen.next_group()),


# SUPER + SHIFT KEYS

    Key([mod, "shift"], "Return", lazy.spawn('thunar')),
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "control"], "r", lazy.restart()),
     Key([mod, "shift"], "x", lazy.shutdown()),

# CONTROL + ALT KEYS

    Key(["mod1", "control"], "Next", lazy.spawn('conky-rotate -n')),
    Key(["mod1", "control"], "Prior", lazy.spawn('conky-rotate -p')),
    Key(["mod1", "control"], "a", lazy.spawn('xfce4-appfinder')),
    Key(["mod1", "control"], "b", lazy.spawn('thunar')),
    Key(["mod1", "control"], "c", lazy.spawn('catfish')),
    Key(["mod1", "control"], "e", lazy.spawn('arcolinux-tweak-tool')),
    Key(["mod1", "control"], "f", lazy.spawn('firefox')),
    Key(["mod1", "control"], "g", lazy.spawn('chromium -no-default-browser-check')),
    Key(["mod1", "control"], "i", lazy.spawn('nitrogen')),
    Key(["mod1", "control"], "k", lazy.spawn('slimlock')),
    Key(["mod1", "control"], "m", lazy.spawn('xfce4-settings-manager')),
    Key(["mod1", "control"], "o", lazy.spawn(home + '/.config/qtile/scripts/compton-toggle.sh')),
    Key(["mod1", "control"], "p", lazy.spawn('pamac-manager')),
    Key(["mod1", "control"], "r", lazy.spawn('rofi-theme-selector')),
    Key(["mod1", "control"], "s", lazy.spawn('spotify')),
    Key(["mod1", "control"], "t", lazy.spawn('st')),
    Key(["mod1", "control"], "u", lazy.spawn('pavucontrol')),
    Key(["mod1", "control"], "Return", lazy.spawn('termite')),

# ALT + ... KEYS

    Key(["mod1"], "F3", lazy.spawn('xfce4-appfinder')),

# VARIETY KEYS WITH PYWAL

    Key(["mod1", "shift"], "f", lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -f')),
    Key(["mod1", "shift"], "p", lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -p')),
    Key(["mod1", "shift"], "n", lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -n')),
    Key(["mod1", "shift"], "u", lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -u')),

# CONTROL + SHIFT KEYS

    Key([mod2, "shift"], "Escape", lazy.spawn('xfce4-taskmanager')),

# SCREENSHOTS

    Key([], "Print", lazy.spawn("scrot 'ArcoLinux-%Y-%m-%d-%s_screenshot_$wx$h.jpg' -e 'mv $f $$(xdg-user-dir PICTURES)'")),
    Key([mod2], "Print", lazy.spawn('xfce4-screenshooter')),
    Key([mod2, "shift"], "Print", lazy.spawn('gnome-screenshot -i')),

# MULTIMEDIA KEYS

# INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),

# INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

#    Key([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
#    Key([], "XF86AudioNext", lazy.spawn("mpc next")),
#    Key([], "XF86AudioPrev", lazy.spawn("mpc prev")),
#    Key([], "XF86AudioStop", lazy.spawn("mpc stop")),

# QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),

# CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
#    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),


# RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod], "semicolon",
        lazy.layout.grow(),                   # Shrink size of current window (XmonadTall)
        lazy.layout.increase_nmaster(),         # Decrease number in master pane (Tile)
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod], "h",
        lazy.layout.shrink(),                     # Grow size of current window (XmonadTall)
        lazy.layout.decrease_nmaster(),         # Increase number in master pane (Tile)
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),


# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),

# FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),

# MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

# TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),]

groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8",]

group_labels = ["1", "2", "3", "4", "5", "6", "7", "8",]
#group_labels = ["", "", "", "", "", "", "", "", "", "",]

group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])


def init_layout_theme():
    return {"margin": 8,
            "border_width": 2,
            "border_focus": "#ffb26b",
            "border_normal": "#4c566a"
            }

layout_theme = init_layout_theme()


layouts = [
    layout.MonadTall(margin=7, border_width=2, border_focus="#ffb26b", border_normal="#4c566a"),
    #layout.MonadWide(margin=8, border_width=3, border_focus="#0099ff", border_normal="#4c566a"),
    #layout.Matrix(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Floating(fullscreen_border_width=0, max_border_width=1, border_width=1, border_focus="#0099ff", border_normal="#4c566a"),
    #layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme)
]

# COLORS FOR THE BAR

def init_colors():
    return [["#3c4457", "#3c4457"], # color 0
            ["#1b1e2b", "#1b1e2b"], # color 1
            ["#c0c5ce", "#c0c5ce"], # color 2
            ["#ffcb6b", "#ffcb6b"], # color 3
            ["#0099ff", "#0099ff"], # color 4
            ["#ffffff", "#ffffff"], # color 5
            ["#cd1f3f", "#cd1f3f"], # color 6
            ["#b7e07c", "#b7e07c"], # color 7
            ["#719eff", "#719eff"], # color 8
            ["#6D7A8A", "#6D7A8A"]] # color 9


colors = init_colors()


# WIDGETS FOR THE BAR

def init_widgets_defaults():
    return dict(font="Ubuntu Mono Bold",
                fontsize = 22,
                padding = 3,
                background=colors[1])

widget_defaults = init_widgets_defaults()

def init_widgets_list():
    #prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
#               widget.Sep(
#                        linewidth = 0,
#                        padding = 0,
#                        foreground = colors[1],
#                        background = colors[1]
#                        ),
               widget.Image(
                        filename = "/home/kbc/.config/qtile/icons/python.png",
                        mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn('jgmenu_run')},
                        margin_x = 6,
                        margin_y = 3
                        ),
               widget.GroupBox(
                       font = "Operator Mono Medium",
                       fontsize = 19,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 1,
                       padding_x = 5,
                       borderwidth = 3,
                       active = '#f07178',
                       inactive = colors[2],
                       rounded = False,
                       highlight_color = colors[0],
                       highlight_method = "line",
                       this_current_screen_border = colors[4],
#                       this_screen_border = colors [8],
#                       other_current_screen_border = colors[0],
#                       other_screen_border = colors[0],
                       foreground = colors[5],
                       background = colors[1]
#                        font="Cantarell Bold",
#                        fontsize = 16,
#                        margin_y = 2,
#                        margin_x = 0,
#                        padding_y = 0,
#                        padding_x = 8,
#                        borderwidth = 2,
#                        disable_drag = True,
#                        center_aligned = True,
#                        active = '#F07178',
#                        inactive = colors[4],
#                        highlight_method = "block",
#                        block_highlight_text_color = '#ffffff',
#                        highlight_color	= ['#FFFFFF', '#0099ff'],
#                        this_screen_border = '#FFFFFF',
#                        this_current_screen_border = '#0099ff',
#                        foreground = colors[4],
#                        background = colors[1]
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[8],
                        background = colors[1]
                        ),
               widget.CurrentLayout(
                        fontsize = 16,
                        font = "Ubuntu Mono Bold",
                        foreground = colors[7],
                        background = colors[1]
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[8],
                        background = colors[1]
                        ),
#               widget.WindowCount(
#                        fontsize = 16,
#                        font = "Ubuntu Mono Bold",
#                        foreground = colors[7],
#                        background = colors[1]
#                        ),
#               widget.Sep(
#                        linewidth = 1,
#                        padding = 10,
#                        foreground = colors[8],
#                        background = colors[1]
#                        ),
               widget.WindowName(
                        font="Ubuntu Mono Bold",
                        fontsize = 16,
                        foreground = "#f07178",
                        background = colors[1]
                        ),
              widget.YahooWeather(
                        #location = "Gainesville, FL",
                        woeid = '12771812',
                        format = '{current_observation_condition_symbol} {current_observation_condition_text} {current_observation_condition_temperature}°{units_temperature}',
                        fontsize = 16,
                        foreground = "#000000",
                        json = 'True',
                        background = "#ffcb6b",
                        padding = 6,
                       # woeid = '12771812',
                        metric = False,
                        update_interval = '600'
                        ),
               widget.Sep(
                        linewidth = 0,
                        padding = 5,
                        foreground = colors[8],
                        background = colors[1]
                        ),
               widget.TextBox(
                        font="FontAwesome",
                        text=" ",
                        foreground="#000000",
                        background="#82dbff",
                        padding = 2,
                        fontsize=18
                        ),
              widget.GenPollText(
                        update_interval = 12000,
                        func = lambda: subprocess.check_output(["uname", "-r"]).decode("utf-8").strip(),
                        fontsize = 16,
                        padding = 6,
                        foreground = "#000000",
                        background = "#82dbff"
                        ),
               widget.Sep(
                        linewidth = 0,
                        padding = 5,
                        foreground = colors[8],
                        background = colors[1]
                        ),
               widget.TextBox(
                        font="FontAwesome",
                        text=" ",
                        foreground="#000000",
                        background="#c792ea",
                        padding = 2,
                        fontsize = 18
                        ),
               widget.Volume(
                        font="Ubuntu Mono Bold",
                        foreground="#000000",
                        background="#c792ea",
                        padding = 6,
                        fontsize = 16
                        ),
               widget.Sep(
                        linewidth = 0,
                        padding = 5,
                        foreground = colors[8],
                        background = colors[1]
                        ),
                widget.TextBox(
                        font="FontAwesome",
                        text=" ",
                        foreground="#000000",
                        background="#82aaff",
                        padding = 2,
                        fontsize=18
                        ),
               widget.Memory(
                        font = "Ubuntu Mono Bold",
                        format = '{MemUsed}M',
                        update_interval = 5,
                        fontsize = 16,
                        padding = 6,
                        foreground = "#000000",
                        background = "#82aaff",
                        ),
               widget.Sep(
                        linewidth = 0,
                        padding = 5,
                        foreground = colors[8],
                        background = colors[1]
                        ),
               widget.TextBox(
                        font="FontAwesome",
                        text="  ",
                        foreground="#000000",
                        background="#f07178",
                        padding = 2,
                        fontsize=18
                        ),
               widget.TextBox(
                        text="Updates:",
                        foreground="#000000",
                        background="#f07178",
                        padding = 0,
                        fontsize = 16
                        ),
               widget.Pacman(
                        foreground = "#000000",
                        background = "#f07178",
                        fontsize = 16,
                        execute = 'urxvt',
                        update_interval = "600",
                        padding = 6,
                        colour_have_updates = colors[5]
                        ),
#               widget.CheckUpdates(
#                        distro='Arch',
#                        format = 'Updates: {updates}',
#                        foreground = colors[5],
#                        background = colors[1],
#                        colour_have_updates = colors[3],
#                        fontsize = 16,
#                        execute = 'urxvt',
#                        update_interval = "600"
#                        ),
               widget.Sep(
                        linewidth = 0,
                        padding = 5,
                        foreground = colors[8],
                        background = colors[1]
                        ),
               widget.TextBox(
                        font="FontAwesome",
                        text="  ",
                        foreground="#000000",
                        background="#c3e88d",
                        padding = 0,
                        fontsize=18
                        ),
               widget.Clock(
                        foreground = "#000000",
                        background = "#c3e88d",
                        fontsize = 16,
                        padding = 6,
                        format="%b %d, %I:%M %p"
                        ),
               widget.Systray(
                        background=colors[1],
                        icon_size=20,
                        padding = 4
                        ),
              ]
    return widgets_list

widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

#def init_widgets_screen2():
#    widgets_screen2 = init_widgets_list()
#    return widgets_screen2

widgets_screen1 = init_widgets_screen1()
#widgets_screen2 = init_widgets_screen2()

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=24))]
screens = init_screens()



# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

dgroups_key_binder = None
dgroups_app_rules = []

# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
# BEGIN

# @hook.subscribe.client_new
# def assign_app_group(client):
#     d = {}
#     #########################################################
#     ################ assgin apps to groups ##################
#     #########################################################
#     d["1"] = ["Navigator", "Firefox", "Vivaldi-stable", "Vivaldi-snapshot", "Chromium", "Google-chrome", "Brave", "Brave-browser",
#               "navigator", "firefox", "vivaldi-stable", "vivaldi-snapshot", "chromium", "google-chrome", "brave", "brave-browser", ]
#     d["2"] = [ "Atom", "Subl3", "Geany", "Brackets", "Code-oss", "Code", "TelegramDesktop", "Discord",
#                "atom", "subl3", "geany", "brackets", "code-oss", "code", "telegramDesktop", "discord", ]
#     d["3"] = ["Inkscape", "Nomacs", "Ristretto", "Nitrogen", "Feh",
#               "inkscape", "nomacs", "ristretto", "nitrogen", "feh", ]
#     d["4"] = ["Gimp", "gimp" ]
#     d["5"] = ["Meld", "meld", "org.gnome.meld" "org.gnome.Meld" ]
#     d["6"] = ["Vlc","vlc", "Mpv", "mpv" ]
#     d["7"] = ["VirtualBox Manager", "VirtualBox Machine", "Vmplayer",
#               "virtualbox manager", "virtualbox machine", "vmplayer", ]
#     d["8"] = ["Thunar", "Nemo", "Caja", "Nautilus", "org.gnome.Nautilus", "Pcmanfm", "Pcmanfm-qt",
#               "thunar", "nemo", "caja", "nautilus", "org.gnome.nautilus", "pcmanfm", "pcmanfm-qt", ]
#     d["9"] = ["Evolution", "Geary", "Mail", "Thunderbird",
#               "evolution", "geary", "mail", "thunderbird" ]
#     d["0"] = ["Spotify", "Pragha", "Clementine", "Deadbeef", "Audacious",
#               "spotify", "pragha", "clementine", "deadbeef", "audacious" ]
#     ##########################################################
#     wm_class = client.window.get_wm_class()[0]
#
#     for i in range(len(d)):
#         if wm_class in list(d.values())[i]:
#             group = list(d.keys())[i]
#             client.togroup(group)
#             client.group.cmd_toscreen()

# END
# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME



main = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])


@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'Arcolinux-welcome-app.py'},
    {'wmclass': 'Arcolinux-tweak-tool.py'},
    {'wmclass': 'audacious'},
    {'wmclass': 'vlc'},
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},
    {'wmclass': 'makebranch'},
    {'wmclass': 'maketag'},
    {'wmclass': 'Nitrogen'},
    {'wmclass': 'Arandr'},
    {'wmclass': 'feh'},
    {'wmclass': 'lxappearance'},
    {'wmclass': 'qt5ct'},
    {'wmclass': 'xfce4-appfinder'},
    {'wmclass': 'viewnior'},
    {'wmclass': 'gsimplecal'},
    {'wmclass': 'Io.github.celluloid_player.Celluloid'},
    {'wmclass': 'mpv'},
    {'wmclass': 'Galculator'},
    {'wmclass': 'Oblogout'},
    {'wname': 'branchdialog'},
    {'wname': 'Open File'},
    {'wname': 'pinentry'},
    {'wmclass': 'ssh-askpass'},

],  fullscreen_border_width=0, max_border_width=0, border_width=2, border_focus="#ffb26b", border_normal="#4c566a")
auto_fullscreen = True

#focus_on_window_activation = "focus" # or smart

wmname = "LG3D"
