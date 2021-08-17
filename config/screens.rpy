init python:
    def wks_on_load_callback(slot):
        try:
            persistent.timeofday = persistent.wks_on_save_timeofday[slot][0]
            persistent.sprite_time = persistent.wks_on_save_timeofday[slot][1]
            persistent.font_size = persistent.wks_on_save_timeofday[slot][2]
            _preferences.volumes['music'] = persistent.wks_on_save_timeofday[slot][3]
            _preferences.volumes['sfx'] = persistent.wks_on_save_timeofday[slot][4]
            _preferences.volumes['voice'] = persistent.wks_on_save_timeofday[slot][5]
        except:
            pass
    def wks_on_save_callback(slot):
        if not persistent.wks_on_save_timeofday:
            persistent.wks_on_save_timeofday={}
        persistent.wks_on_save_timeofday[slot] = (persistent.timeofday, persistent.sprite_time, persistent.font_size, _preferences.volumes['music'], _preferences.volumes['sfx'], _preferences.volumes['voice'])
    def wks__screen_save():
        for name in ["game_menu_selector","say", 'main_menu', 'quit','preferences', 'save', 'yesno_prompt', 'load']:
            renpy.display.screen.screens[("wks_old_"+name, None)] = renpy.display.screen.screens[(name, None)]
    def wks__screen_act():
        config.window_title = u"Восполненный надеждой"
        config.name = "from ashes to paradise"
        config.version = '0.0.1'
        save_name = 'Восполненный надеждой'
        # renpy.display.screen.screens[("say", None)] = renpy.display.screen.screens[("wks_say", None)]
        #renpy.display.screen.screens[("game_menu_selector", None)] = renpy.display.screen.screens[("wks_game_menu_selector", None)]
        renpy.display.screen.screens[('main_menu', None)] = renpy.display.screen.screens[('wks_main_menu', None)]
        renpy.display.screen.screens[('quit', None)] = renpy.display.screen.screens[('wks_exit', None)]
        # renpy.display.screen.screens[('preferences', None)] = renpy.display.screen.screens[('wks_preferences', None)]
        # renpy.display.screen.screens[('save', None)] = renpy.display.screen.screens[('wks_save', None)]
        # renpy.display.screen.screens[('load', None)] = renpy.display.screen.screens[('wks_load', None)]
        # renpy.display.screen.screens[('yesno_prompt', None)] = renpy.display.screen.screens[('wks_yesno_prompt', None)]
        persistent._file_page = "wks_FilePage_1"
        _game_menu_screen = "wks_game_menu_selector"
        layout.LOADING = "Потерять несохраненые данные?"
        config.main_menu_music = "mods/Workers_Council/gui/main_menu/wks_main_menu.mp3"
        config.linear_saves_page_size = None
        #config.mouse = {'default' : [("mods/wks/gui/misc/mouse.png",  0, 0)]}
    def wks__after_load_srceen():
        global save_name
        if save_name.find(u'Восполненный надеждой') != -1:
            wks__screen_act()
    config.after_load_callbacks.append(wks__after_load_srceen)
    def wks__screens_diact():
        try:
            config.window_title = u"Бесконечное лето"
            config.name = "Everlasting_Summer"
            config.version = "1.2"
            for name in ["game_menu_selector","say", 'main_menu', 'quit', 'preferences', 'preferences', 'save', 'yesno_prompt', 'load']:
                renpy.display.screen.screens[(name, None)] = renpy.display.screen.screens[("wks_old_"+name, None)]
            layout.LOADING = "Загрузка приведёт к потере несохранённых данных.\nВы уверены, что хотите сделать это?"
            _main_menu_screen = "main_menu"
            _game_menu_screen = "game_menu_selector"
            config.mouse = {'default' : [("images/misc/mouse/1.png",  0, 0)]}
            config.main_menu_music = "sound/music/blow_with_the_fires.ogg"
            persistent._file_page = 1
            renpy.music.stop("ambience")
            renpy.music.stop("music")
            renpy.music.stop("sound")
            renpy.play(music_list["blow_with_the_fires"], channel = "music")
        except:
            renpy.quit()
    def wks__screens_save_act():
        wks__screen_save()
        wks__screen_act()

    class WKSLighters(object):

        def __init__(self):

            self.sm = SpriteManager(update=self.update)

            self.glows = [ ]
            self.rd = im.Scale("mods/Workers_Council/gui/main_menu/lighter (2).png", 45, 46)

            d = Transform(self.rd, zoom=0.25)
            for i in range(0, 20):
                self.add(d, renpy.random.randint(20, 40))

            d = Transform(self.rd, zoom=0.5)
            for i in range(0, 20):
                self.add(d, renpy.random.randint(35, 55))

        def add(self, d, speed):
            s = self.sm.create(d)

            start = renpy.random.randint(0, 1080)
            s.x = renpy.random.randint(0, 1920)

            self.glows.append((s, start, speed))

        def update(self, st):
            for s, start, speed in self.glows:
                s.y = (start + speed/2 * st) % 1080 - 20
                s.x = s.x + math.sin(s.y/speed*2)

            return 0
    renpy.image("wks_lighters", WKSLighters().sm)

init:
    style wks_button is default
    style wks_button_text is default:
        color '#f4dc26'
        hover_color '#e9bf32'
        font 'mods/Workers_Council/fonts/Bony Regular.ttf'
        size 70
        bold True
        outlines [( 1, '#400080', 1, 1)]
        hover_outlines [(1,'#4e009b', 1, 1)]

    transform wks_button_hover:
        on idle:
            ease .75 zoom 1 alpha .8
        on hover:
            ease .75 zoom 1.3 alpha 1.0


init:
    screen wks_main_menu():
        tag menu
        modal True

        style_prefix 'wks'


        add im.Blur('mods/Workers_Council/gui/main_menu/wks_main_menu.jpg', 1.3)
        add 'wks_lighters'


        vbox align(0.5, 0.5) spacing 25:
            textbutton 'Начать игру' action Start('hope_prologue') at wks_button_hover
            textbutton 'Выбор дня' action  NullAction() #ShowMenu('hope_prologue') 
            textbutton 'Настройки' action ShowMenu('preferences') at wks_button_hover
            textbutton 'Выход' action ShowMenu('wks_exit') at wks_button_hover


    screen wks_exit():
            modal True
            tag menu

            style_prefix "wks"

            key "game_menu":
                action Return()

            add im.Blur('mods/Workers_Council/gui/main_menu/wks_main_menu.jpg', 1.5)

            text "Ты хочешь уйти?":
                size 100
                style 'wks_button_text'
                xalign 0.7
                yalign 0.33

                antialias True
                kerning 2

            hbox:
                xpos 0.55
                ypos 0.55
                spacing 80

                textbutton "Да" text_size 70 action (Hide("wks_exit", fade), Function(wks__screens_diact), Start("wks_true_exit")) at wks_button_hover
                textbutton "Нет" text_size 70 action Return() at wks_button_hover



label wks_index:
    window hide dissolve
    scene black with fade3
    $ set_mode_adv()
    $ wks__screens_save_act()

label wks_true_exit:

    window hide dissolve
    stop music fadeout 3
    scene black with fade
    pause 1

    $ MainMenu(confirm=False)()