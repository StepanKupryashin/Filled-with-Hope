init:
    $ mods["wks_index"] = u"Восполненный надеждой"
    # ПЕРСОНАЖИ
    $ names["polina"] = u"Полина"
    $ colors["polina"] = {
        "day": (30, 144, 255, 255),
        "sunset": (30, 144, 255, 255),
        "night": (30, 144, 255, 255),
        "prolog": (30, 144, 255, 255) }
    $ store.names_list.append("polina")

    $ names["anya"] = u"Аня"
    $ colors["anya"] = {
        "day": (255, 0, 0, 255),
        "sunset": (255, 0, 0, 255),
        "night": (255, 0, 0, 255),
        "prolog": (255, 0, 0, 255) }
    $ store.names_list.append("anya")

    $ names["nik"] = u"Николай"
    $ colors["nik"] = {
        "day": (139, 69, 19, 255),
        "sunset": (139, 69, 19, 255),
        "night": (139, 69, 19, 255),
        "prolog": (139, 69, 19, 255) }
    $ store.names_list.append("nik")

    $ names["ilya"] = u"Илья"
    $ colors["ilya"] = {
        "day": (245, 245, 245, 255),
        "sunset": (245, 245, 245, 255),
        "night": (245, 245, 245, 255),
        "prolog": (245, 245, 245, 255) }
    $ store.names_list.append("ilya")

    $ names["ser"] = u"Серёга"
    $ colors["ser"] = {
        "day": (255, 255, 0, 255),
        "sunset": (255, 255, 0, 255),
        "night": (255, 255, 0, 255),
        "prolog": (255, 255, 0, 255) }
    $ store.names_list.append("ser")

    # МУЗЫКА
    $ start_prolog = wks_music + "stalker.mp3"
    $ ludo = wks_music + "ludovico.mp3"
    $ gib = wks_music + "gib_plyaj.mp3"
    $ love_theme = wks_music + "RF_love_theme.mp3"
    $ kokoro = wks_music + "kokoro.mp3"
    $ faith = wks_music + "The Weeknd-Faith.mp3"
    $ omaewa = wks_music + "desu.mp3"
    $ eybog = wks_music + "Farewell To The Past.mp3"
    $ evl_soul = wks_music + "Evil In My Soul.mp3"
    $ spl_secrts = wks_music + "Spiral of Secrets.mp3"
    $ escape = wks_music + "Escape.mp3"
    $ hope = wks_music + "hope.mp3"
    $ negation = wks_music + "negation.mp3"
    $ going_home = wks_music + "going home.mp3"

    # ЗВУКИ
    $ steps = "mods/Workers_Council/sounds/steps.mp3"
    $ wc_run = "mods/Workers_Council/sounds/run.mp3"
    $ alarm = "mods/Workers_Council/sounds/alarm clock.mp3"
    $ step = "mods/Workers_Council/sounds/steps_home.mp3"
    $ street_noice = "mods/Workers_Council/sounds/sueta.mp3"
    $ shagi_padik = "mods/Workers_Council/sounds/padik_steps.mp3"
    $ hit_face_ladon = "mods/Workers_Council/sounds/ydar_sheka.mp3"
    $ gudok_car = "mods/Workers_Council/sounds/gudok.mp3"
    $ avar = "mods/Workers_Council/sounds/avariya.mp3"
    $ ear_noice = "mods/Workers_Council/sounds/zvon.mp3"

    # ПЕРЕХОДЫ
    define pushright = PushMove(2.0, "pushright")
    $ flash_red = Fade(.25, 0, .75, color="#f00")


label hope_prologue:
    show blink
    play music start_prolog fadein 3
    "Тук-Тук.Стук.Постоянный нескончаемый стук, от которого я уже начал сходить с ума."
    hide blink
    scene bg mirror
    show unblink
    $ persistent.sprite_time = 'day'
    "Тук-тук. Капли, соприкасаясь со стеклом, быстро летят вниз, освобождая место для новых. Уже конец весны, но на улице очень темно. Огромные тучи, клубнями налетевшие на мой родной город, несут лишь мрак."
    "Почему-то мне казалось, что окончание 10 класса будет выглядеть по-иному."
    $ set_mode_nvl()
    "С самого детского садика мои родители прививали мне какую-то слишком навязчивую мысль, что я никому ничего не должен, но если уж хочу быть примерным и уважаемым человеком в обществе, то придётся трудиться до изнеможения."
    "Все 9 лет учебы в школе, я с сильным желанием верил в это, что вот, осталось ещё немного и все. Вступлю в КПСС, добьюсь там высоких чинов, и жизнь моя будет прекрасна. Мало того моя жизнь, я буду и жизнь других людей делать более комфортной."
    "Сейчас, подытоживая все мои желания из прошлого, можно сказать, что у меня было неоспоримое желание стать политиком. В мечтах у меня идеализировались образы Тэтчер, Ленина, Сталина, Линкольна и прочих довольно известных политических деятелей."
    "Однако, к 10 классу я начал сомневаться в своих желаниях. Стал меньше читать книг, меньше общаться с людьми. Чаще стал замыкаться в себе, и не осознавать того, что происходит вокруг меня. Казалось, будто все нормально, но мне не было комфортно ни в одной компании. Мне надоело корчить из себя человека, которому всё нравится, которого устраивает всё, чем он живет."
    $ set_mode_adv()
    scene bg coridor with flash

    "До этого времени я познакомился с одной девочкой, которая, можно сказать, запала мне в душу.. Она была словно глоток свежего воздуха, в котором я так нуждался. Ее звали Аня."
    "В день нашего знакомства, 2 сентября, будучи ещё в восьмом классе, я устало блуждал по коридорам школы, ожидая начала дополнительного по иностранному языку. Из раздумий меня вывела девушка, в которую, я, судя по всему, врезался."
    show anya shy school close with dspr
    "Бац, мы оглянулись, глядя друг другу в глаза."
    th "Вот ведь судьба сама подталкивает людей друг к другу."
    "Я никак не ожидал увидеть там такое милое личико. За несколько секунд я изучил внешние параметры девушки. Ее глаза, темно-голубого цвета, виновато глядели на меня. Поправив локон красных волос, за считанные секунды, она, все же, решила заговорить, взяв на себя инициативу."
    anya "Извини, я тут просто задумалась немного."
    "Тихо проговорила она, все так же продолжая смотреть мне в глаза."
    ilya "Да все в порядке, не каждый день мне выдаются случаи врезаться в таких девушек"
    "Она мне улыбнулась."
    show anya smeh school close with dspr
    extend "Затем, моя новая знакомая одарила меня вопросительным взглядом, который я расценил, как фразу: «Чего стоишь? Вали давай»."
    ilya "Ладно мне пора, я… должен идти на дополнительный."
    show anya neitrall school close with dspr
    "Признался я."
    anya "Ой, а ты тоже идешь на дополнительный? Я просто поступила сюда с другой школы, и пока плохо ориентируюсь по зданию, и кажется немного заплутала. Мне бы на дополнительный по…{nw}"
    ilya "На английский шёл, вот."
    "Перебил я девушку."
    show anya smeh school close with dspr
    anya "Ой, какое совпадение, мне казалось, что такое бывает только в фильмах. Мне тоже надо туда."
    ilya "Ну, раз уж так, то давай помогу тебе добраться."
    hide anya with dissolve
    "Наш путь не был таким уж долгим и захватывающим… Надо было дойти до второго этажа, как сейчас помню… К слову, она перестала смотреть на меня, да и в принципе потеряла интерес ко мне в тот промежуток времени."
    scene bg class_room_day with dissolve
    $ renpy.pause(1.0)
    scene bg class_room with pushright
    "Дополнительные выдались достаточно скучными. Ничего нового нам в начале учебного года рассказать не могли. Мы потратили время только на определение наших целей."
    "После них, уже ничего не ожидая, я пошёл домой, не выпуская из головы образ той самой девушки, в которую я так неосторожно врезался…"
    stop music fadeout 3
    scene bg room with flash
    play music ludo fadein 3
    "Сейчас, вспоминая школу, понимаешь, что не хочется ничего этого терять. Не хочется осознавать, что до конца моих отношений со всеми этими ребятами остался всего какой-то жалкий год."
    "Множество знакомых, всего два друга. Вот и весь результат моего пребывания в школе. Знания? Ну да, был, да и являюсь отличником, только какой от них прок, если людей, с которыми можно ими поделиться, нет?"
    "Не буду же я подходить к неизвестным на улице и говорить, мол: «хочешь узнать третий закон Ньютона»?"
    th "26 мая 1989 год."
    "Заключил я про себя, поглядев на календарь возле окна."
    "Десятый класс пронёсся быстрее, чем все девять вместе взятых, а вот воспоминаний… Воспоминаний о нем вообще нет. Создаётся ощущение, что десятый класс – это просто пустота, заполняемая лишь моим нытьем и попытками осознать произошедшее."
    "Мог ли я что-то изменить, мог ли не допустить чего-то?"
    "При таких размышлениях, вспоминается один случай, произошедший в моей жизни, когда мне было 16. Я иду по улице и вижу, как двое старшеклассников зажали какого-то паренька, которому на вид и 15 не было."
    play music faith
    "Пройти мимо я не мог, поэтому вступился за него."
    scene bg ghetto with flash
    play sound steps
    ilya "Чего к парню пристали? Отстаньте от него."
    stop sound
    "В ответ мне лишь послышались оскорбления."
    "Я сразу же постарался отгородить парня, и начал атаковать неприятелей, отвлекая их от мальчика, и желая вывести из строя хотя бы одного из них."
    play sound sfx_punch_medium
    "Удар, блок. Пытаюсь своими быстрыми движениями дезориентировать их, что даже немного получается. Выскакиваю рядом с одним из обидчиков и сразу отправляю его на отдых.{nw}"
    play sound sfx_punch_washstand
    show black with flash_red
    play sound wc_run
    "Пропустив удар, я упал, перевернулся, и закрыл лицо руками. На фоне слышал звуки, как те парни убегают."
    stop sound
    th "Слава Богу."
    scene bg room with flash
    stop music fadeout 3
    "Помощь неизвестному пареньку в обмен на долгие разбирательства с родителями. Думаю, что это стоило того."
    play sound alarm
    th "Пора завтракать."
    stop sound
    play music gib fadein 3
    "По факту, сегодня был учебный день, но учиться в последний день учебного года, разумеется, никто не собирался."
    "Я быстро натянул на себя шорты, чтобы не бегать по дому в одних трусах и футболке."
    th "Модные у меня однако шорты…"
    "Шорты относительно широкие, в клеточку красно-зелёного цвета. Сказать, что на фоне моей белой футболки они пестрили – ничего не сказать."
    "Далее, по плану, у меня бытовые дела: для начала я схожу умыться, далее быстренько перекушу что-нибудь, и потом в школу."
    "Из комнаты родителей все ещё доносился храп. Удачное выдалось совпадение, что и у матери, и у отца сегодня не их смена на работе. Буду искренне надеяться, что у них сегодня выдастся отличный денёк."
    scene bg bathroom with dissolve
    "И так, водные процедуры."
    "Наберём в ручки воды, затем плеснём ее в лицо."
    play sound sfx_open_water_sink
    $ renpy.pause(0.5)
    play sound sfx_water_sink_stream
    $ renpy.pause(1.0)
    $ renpy.pause(0.7)
    play sound sfx_head_heartbeat
    show blink
    $ renpy.pause(1.0)
    th "##@!!!???"
    show unblink
    hide blink
    "Вода была не холодной, она была подобна кусочку льда в -30°."
    play sound sfx_open_water_sink
    play sound sfx_water_sink_stream
    "Оставив эмоции, я выкрутил кран на более тёплый поток воды. По-скорому умылся и вытерся."
    th "Хорошо, первая цель моего сегодняшнего дня, с горем пополам, выполнена."
    "Быстрыми шагами я направился в сторону кухни."
    play sound step
    "Топ-топ-топ…"
    th "Надо бы шуметь поменьше."
    stop sound
    scene bg kitchen with dissolve
    "Стараясь ходить по кухне на цыпочках, я тихонечко сварганил себе три бутерброда, состоящих из белого хлеба и докторской колбасы. Запивать все это я должен был зелёным чаем."
    "Не люблю наедаться по утрам,поэтому чаще всего завтракаю только бутербродами, или какой-то сладостью."
    "То ли у меня с настроением что-то, из-за чего привычный завтрак перестал казаться вкусным, то ли колбаса какая-то не та."
    $ renpy.pause(1.0)
    "Приём пищи окончен, моем за собой посуду и двигаем одеваться. Каким-то я сегодня проснулся совершенно неважным… Ладно, уверен, что в школе мне помогут и исправят не особо хорошее настроение на положительное."
    scene bg room with dissolve
    "Одеваться надо как-то попроще,  но так, чтобы было видно кто тут самый четкий на районе."
    th "Кажись, сегодня я буду самым размытым."
    "Из одежды я надел узкие брюки и белую рубашку, поверх накинул на себя пиджак, дабы придать себе статусный вид."
    th "Так, лицо умыл, еду съел, ширинку застегнул."
    "Со счастливыми мыслями, что мне удалось ничего не забыть, я выдвинулся в школу, прихватив с собой для вида, рюкзак чёрного цвета."
    stop music fadeout 3
    stop sound fadeout 1
    scene bg sssr with fade
    play sound street_noice fadein 3
    play music omaewa fadein 3
    th "М-да, денёк не распогодился."
    "Я шёл по серой улице Москвы, восхищаясь прекрасными видами весны. По разным сторонам улицы росли деревья, а из парка, рядом с которым находился мой дом, выехал трамвай."
    "Любовь к природе мне привита с самого детства не была, поэтому я не видел ничего особенного в обычных пейзажах природы или видах на неё."
    "Скорее, мое восхищение заключалось в том, что природа до сих пор способна выживать, как независимый организм, в мире, который почти полностью подчинен жестоким людям, при этом, в некоторых случаях, даже давая достойный отпор человечеству."
    "Что-то начало пронзительной щиплющей болью отдаваться в голени, я тихонько остановился, поглядев."
    th "Отлично..."
    th "Ладно, вперёд, за товарища Сталина."
    "С новой силой я зашагал вперёд, пытаясь забыть о том, что с моей ногой вообще что-то случилось. Наконец, перед моим взором показалась школа."
    scene bg schl with dissolve
    stop music fadeout 3
    "Зайдя на территорию школы, я сразу же заприметил, что во дворе столпилась огромная толпа, рядом с которой мне явно и требовалось находиться. Буквально прождав минут пять, люди начали двигаться вперёд – в школу, после выкрика директора."
    play music hope fadein 3
    ser "Эй, Илья!"
    "От этого голоса я немного испугался, но быстро взял себя в руки и оглянулся. Позади меня стоял мой друг – Серёга!"
    show el smile pioneer far with dspr
    ser "Привет, как тебе там живётся в давке?"
    show el smile pioneer close with dspr
    ilya "Не лучше, чем тебе."
    "Он протянул мне руку, и я, с горем пополам пожал её, затем мы встали примерно на одном уровне и двинули в зал уже вместе."
    hide el
    stop sound fadeout 1
    stop music fadeout 3
    hide el with dspr
    $ set_mode_nvl()
    "Сергей Сыроежкин. Как много боли и радости для меня заключено в этих словах. С этим человеком мы знакомы достаточно давно: с первого класса. Нами было пройдено множество проблем и принято много важных для нас решений. Почему-то до класса третьего наши взаимоотношения были решительно плохие. Мы часто дрались, ссорились, да и вообще были идеальным примером личной вражды."
    "К четвёртому классу все пошло на улучшение: были найдены совместные точки соприкосновения наших интересов, что помогло нам наладить контакт, и начать движение к дружбе."
    "Он всегда помогал мне, никогда не предавал. В общем, друг, что надо. Именно из-за него, в моей жизни возникло четкое разделение между другом и товарищем, чему я беспредельно рад."
    "Мы сидели весь год обучения за одной партой и наши результаты одни из самых лучших в школе, потому сегодня на церемонии закрытия учебного года, я полагаю, нас как-либо вознаградят, да и мы будем являться почетными гостями."
    $ set_mode_adv()
    scene bg act_zal with dissolve
    play sound street_noice
    "Минуты наслаждения тёплыми воспоминаниями кончились и вот, мы уже оказываемся в зале."
    "Людей, казалось бы, была целая толпа, но место в актовом зале хватило на всех. Более того, множество мест ещё и осталось свободными. В такой обстановке мы с Сергеем сели на последний ряд."
    "Перед нами открывался прекрасный вид на десятки, а то и сотню людей, которые продолжали толпиться и никак не могли сесть."
    stop music fadeout 3
    play music eybog fadein 3
    "Во всей этой суматохе, я увидел взгляд красноволосой девочки, сидящей вместе с местным мачо – Николаем, спереди от нас. Никогда не знал чем он привлекает девушек, однако иногда казалось, что он может угодить попросту всем дамам на свете."
    "Взгляд Ани, брошенный на меня, был холодным, я бы даже сказал, что каким-то укоризненным. Мой спутник, заметивший это, с улыбкой на лице повернулся ко мне и, не теряя ни секунды, сказал:"
    show el smile pioneer close with dspr
    ser "По-любому она втюхалась в тебя!"
    th "Всё было бы не так грустно, если бы это “по-любому” не длилось бы почти 2 года."
    ilya "Да ладно тебе, ты серьёзно? Посмотри в её бесчувственные глаза, они одним взглядом говорят, что я ей вообще уже не нужен."
    "Я отвёл взгляд, немного погрустнев. Приятное настроение от встречи с другом и торжественной церемонии быстро испарилось."
    ser "Боже мой, Илья, ты слишком идиот. Вот смотри, я сейчас подойду к ней и всё расскажу."
    ilya "Ты уверен, что в тысячный раз у тебя получится достичь успеха, пытаясь достичь его одними и теми же методами?"
    ilya "Конечно, спрашиваешь ещё, проверяй!"
    hide el with dspr
    stop music fadeout 3
    "Серёга аккуратно пошёл вдоль рядов, продвигаясь к Ане с Николаем, в то время как я остался совсем один на своём ряду."
    "Пока он находился в ссылке, ко мне, как бы невзначай, подсела моя одноклассница Полина, подошедшая ко мне так тихо, что я её даже и не заметил."
    play music kokoro fadein 3
    $ renpy.sound.set_volume(0.4)
    $ set_mode_nvl()
    "Полина… Достаточно добрая и милая девушка, которая пришла к нам в класс только на третьем году нашего обучения. Учитель сразу же подсадил её ко мне, как к доброму и достаточно интеллигентному мальчику."
    "Вскоре, её начали задирать мальчики, из-за того, что она нравилась одному из них, ну, а как я знаю, лучший метод привлечения к себе внимание в таком малом возрасте - это создание для человека, привлекаемого тобою, максимально нехорошего положения."
    "Мы всегда были добры друг к другу и наши отношения для большинства людей запоминаются больше как дружеские, чем как отношения любовничков. Она любит “подкармливать” меня, принося в школу всякого рода печенья и булочки. Помню, как мы в 7 классе, сидя вместе на скамейке возле школы, уминали вместе печенья. Я принёс сока из какого-то ларька недалеко от нашего учебного заведения, потому трапеза сделалась лишь приятнее."
    "Я бы мог даже сказать так, что если бы мой глаз не был положен на Анну, то я с превеликим удовольствием завёл бы отношения именно с Полиной."
    $ set_mode_adv()
    $ renpy.sound.set_volume(1)
    show polya smile school close with dspr
    #спрайт Полины, радость, ближняя позиция
    "Девочка сразу же полезла обниматься со мной, таково у нас было приветствие друг друга в хорошее настроение."
    polina "Ну как ты?"
    "Спросила она с ласковой интонацией, будто хочет пожалеть меня. Полина достаточно хорошо знала моё состояние, являясь одним человеком из тех, кому я мог довериться и на кого я мог положиться."
    ilya "Не знаю, в последнее время совершенно ничего не хочу делать, хоть верь, хоть нет. Могу с уверенностью заявить, что между чтением книги или любой другой деятельности, которая могла бы принести мне удовольствие, я бы выбрал апатичное состояние с последующим очень увлекательным разглядыванием стены."
    show polya surp school close with dspr
    "Девочка положила на мою руку свою и чуть более тихо пролепетала:"
    polina "Я тебя понимаю, Илья, у меня есть идея, как вывести тебя из этого ужасного состояния."
    show polya smile school close with dspr
    ilya "Ну… Валяй давай свою идею."
    "Я вальяжно развалился на стуле. Ну, настолько вальяжно, насколько позволял мне стул."
    $renpy.pause(0.2)
    show polya neitrall school close with dspr
    polina "Смотри, я испекла пирог, можешь прийти ко мне…"
    "Пирог. От Полины. Звучит достаточно аппетитно."
    ilya "М, а ты знаешь, как завлечь мальчиков в свою квартиру…"
    polina "Скорее знаю, как завлечь в свою квартиру Илью Раевского."
    "От этой фразы сделалось одновременно и приятно, и боязно, однако я не сбавлял темпа."
    ilya "Что ж, Илья Раевский с немалым удовольствием принимает ваше щедрое предложение и готов прийти сегодня после столь торжественной церемонии к вам домой."
    polina "Вместе пойдём."
    ilya "Вместе, так вместе…"
    "Я склонил голову ей на плечо, чувствуя, что ко мне возвращается сон."
    th "М-да, всё-таки просыпаться на час ранее положенного мне срока было плохой идеей, которая сегодня сведёт меня в гроб."
    show polya surp school close with dspr
    polina "Ты чего?"
    play sound street_noice
    "Тревожным голосом спросила девочка."
    ilya "Приустал немножко… Я не совсем выспался."
    polina "Ладно…"
    show polya neitrall school close with dspr
    "Полина приобняла меня, поглаживая по спине. Моё лицо непроизвольно выдавило улыбку."
    ilya "Полин, а с чем пирог будет?"
    show polya shy school close with dspr
    polina "С… С клюквой."
    ilya "М, замечательно."
    stop music fadeout 3
    "Последнее мной сказанное было сказано очень сонно."
    show blink
    $ renpy.pause(0.2)
    show unblink
    hide blink
    "Неожиданно даже для самого меня начали объявлять отличников и лучших учеников среди старших классов."
    polina "Илья, подъём!"
    show polya neitrall school close with dspr
    "Резкий голос Полины повышенным тоном смог разбить мои сонные грёзы и пробудить."
    ilya "О, да, что такое!?"
    polina "Вас объявляют…"
    play music eybog fadein 3
    "Я, встретив взявшегося из ниоткуда Серёгу, двинулся, попутно беседуя о чём-то. За нами поспешили многие другие ученики нашей школы."
    hide polya with dspr
    show el smile pioneer close at left with dspr
    ilya "Ты откуда взялся-то, Ксеркс доморощенный?"
    ser "Да я вот с Аней болтал…"
    ilya "И что? Стоило потраченного времени?"
    "Пока мы беседовали, наши ножки уже донесли нас на сцену, куда мы торжественно и взобрались."
    scene bg int_zal_izn with dissolve
    ser "Я тебе потом расскажу."
    hide el with dspr
    "Прямо перед нами стояли и Полина, и Аня, и множество других девочек. Как самые высокие, мы стояли в задних рядах, наблюдая за всем сверху."
    "Я немного наклонился к Серёге и шепнул ему на ушко."
    show el normal pioneer close at left with dspr
    ser "Рассказывай давай, интригант из тебя вообще никакой."
    ilya "С меня шоколадка."
    ser "- Аня встречается с Николаем, но по-моему они оба не уверены в своей позиции…"
    ilya "В позиции че… {nw}"
    hide el with dspr
    "Наш диалог прервал учитель, материализовавшийся по левый борт от меня. Перечить старшим, я конечно же не стал, поэтому всё дальнейшее мероприятие прошло в относительной тишине."
    th "Никогда не понимал одного. Вот девочки, они же стоят даже ближе к залу, чем мы. Почему же тогда им можно говорить, а нам нет? У нас что шепот другой что ли?"
    "Ладно, это был скорее риторический вопрос. В своих фантазиях я уже давно находился с Полиной в одной квартире, поедая вкуснейшие пироги."
    "Хотя нет, почему же с Полиной… Вот, к примеру, если бы я сейчас был с Аней, мы бы пошли на детскую площадку в парке, который поблизости от моей квартиры, и хорошенько бы отдохнули там…"
    "Из фантазий меня вывел голос моего многоуважаемого друга - Сергея, который без конца тормошил меня за плечо."
    th "Ну почему всегда надо прерывать меня на самом интересном?"
    ilya "Что ещё?"
    show el normal pioneer close at left with dspr
    "Не хотя ответил я."
    ser "Двинули, подробнее расскажу, держи свою грамоту."
    ilya "Оу…"
    "Слезая со сцены, я получил подробное описание моих действий на церемонии, а точнее моего сна. Теперь я знаю, что я - идиот, подставляющий лично Серёгу, чтоб он брал мои грамоты в такие моменты."
    ser "Вот объясни мне, я ведь живу не меньше тебя, объясни мне чёрт побери, как тебе удается засыпать в общественных местах?"
    ilya "Знаешь, есть просто предчувствие, будто бы я скоро стану бомжом без ничего и мне придется делать это на регулярной основе."
    "Я постучал его по плечу и посмеялся. Сергей ответил каким-то странным смехом, который был похож больше на какое-то кряхтение."
    ser "Так вот, слушай, Аня с Николаем - это факт да, но это достаточно некрепкие отношения, я так полагаю…{nw}"
    "Мне пришлось перебить рассказчика, дабы немного прояснить некоторые детали."
    ilya "То есть, ты хочешь сказать, что у них отношения просто для вида?"
    play sound street_noice
    ser "Я не знаю, возможно это звучит глупо, но я почему-то именно так и считаю!"
    ilya "Мда, Серёж, какой-то ты слишком наивный что ли."
    $ set_mode_nvl()
    $ renpy.sound.set_volume(0.3)
    "Я бы предпочёл считать Николая моим главным антагонистом, которому я противостою всю свою школьную жизнь."
    "Иногда у меня даже появляется полноценное чувство, будто он родился таким. Задирчивым, навязчивым и очень… глупым?"
    "Я бы мог описать его несколькими словами: человек с завышенной самооценкой, ненаходящий ничего гениальнее, чем пустые угрозы людям, неприятных ему или угрожающих его статусному положению."
    $ set_mode_adv()
    $ renpy.sound.set_volume(1)
    "Мои воспоминания о Николае почему-то решили испариться именно в тот момент, когда обладатель “крутого” причесона решил “подрулить” ко мне."
    play music evl_soul fadein 3
    #спрайт Николая, ухмылка по центру
    nik "Слушай, Раевский, пойдём отойдём. Поговорим."
    ilya "Николай, я искренне понимаю ваше желание остаться со мной наедине, в более интимной обстановке, но я пожалуй откажусь. Настроение не то."
    #с ухмылки на злость
    "Пожалуй из всех людей в школе как-то бороться с его напором в действительности мог лишь один я."
    nik "Ты, Раевский, давно по лицу не получал?"
    "Мой друг, прибывающий в полуоцепенении от действий моего собеседника, наконец-то очухался и выдавил:"
    show el serious pioneer close at left with dspr
    ser "Чего тебе надо?"
    nik "Я вообще не с тобой разговариваю, понял, да? А ты, Илья, если ещё раз так много будешь смотреть на Аню – буду говорить с тобой по-другому, уяснил?"
    ilya "Будь повежливее с людьми, возможно они будут слушать тебя."
    "Николай видимо сам оказался в шоке от моей ответной наглости и уже был готов завязать драку, как вдруг…"
    show anya surprise school close at right with dspr
    anya "Не деритесь мальчики, чего вы?"
    "Вовремя подошедшая пассия этого осла, смогла успешно разрешить конфликт."
    #эмоции Николая – серьёзность
    "Коля сразу же утихомирился, стал вести себя более сдержанно."
    ilya "Ничего, мы пожалуй пойдём."
    "Я улыбнулся, стрельнув колким взглядом в глаза Ани."
    stop music fadeout 3
    "Мы с Серёгой без промедления двинулись дальше, продолжая беседовать о своём."
    hide anya with dspr
    #убрать спрайт коли
    show el normal pioneer close at left with dspr
    ilya "Слушай, меня Полина к себе позвала, ты же не против, что один домой пойдёшь?"
    ser "Не понимаю я тебя, Илья, зачем Аня тогда? Полина, как по мне, в миллион раз лучше."
    "Мы переглянулись и в нашем диалоге возникло недолгое неловкое молчание."
    $ renpy.pause(0.5)
    ilya "Ну, раз уж тебе нравится, то полагаю, я могу немного побыть с ней. Верно, мой господин?"
    ser "Валяй, холоп."
    show el laugh pioneer close at left with dspr
    "Он усмехнулся и получил слабенький удар в плечо."
    play music spl_secrts fadein 3
    "За прошедшее время мы успели уже оказаться у выхода из школы, который был благополучно преодолен нами."
    show el normal pioneer close at left with dspr
    scene bg schl with dissolve
    $renpy.pause(0.3)
    scene bg sssr with dissolve
    play sound street_noice
    show polya neitrall school close with dspr
    play sound street_noice
    "Там меня уже встречала Полина. Она тихонько подошла ко мне и прижалась, взяв за руку."
    ilya "Ну, удачи тебе, не грусти и помни, что завтра в 12 на футбольном поле!"
    ser "Да, бывай, Илья, до завтра. Звони если что."
    "Он пожал мне руку на прощанье и удалился в противоположном относительно нашему направлению."
    hide el with dspr
    ilya "И снова здравствуйте."
    polina "Привет, сонный дурачок."
    ilya "Ну, и вовсе я не дурачок, у меня в аттестате пятерочек больше чем у тебя!"
    #просто нейтрал, без румянца
    "По мере диалога мы начали движения. Немного придерживая меня за руку, она вела нас. Начальное смущение вскоре сменилось на какое-то… удовольствие."
    scene bg sssr with dissolve
    polina "Дурачок, кто же знания по школьным оценкам смотрит?"
    ilya "Ну, я могу по иному доказать, что я не дурачок."
    polina "В школьной викторине почти по всем предметам моя команда выигрывала твою, Илья, не оправдывайся."
    ilya "Я не буду оправдываться, я лишь скажу одно, что мне просто подсунули каких-то бракованных людей в команду, вот мы и проиграли."
    "Она глянула на меня своими красивыми глазами, широко улыбнувшись."
    show polya smile school close with dspr
    polina "Не поверишь, но мне иногда казалось, что в моей команде абсолютно такие же!"
    ilya "Может и так, как по мне, активно отвечала лишь ты."
    polina "Илья, а что у вас там случилось с Николаем?"
    ilya "Ну, небольшая ссора… Просто хочется, чтобы его уже выперли из школы, но я очень сомневаюсь на активность школьной администрации в этом вопросе."
    polina "Но он же задирает ежедневно почти с десяток людей. Мне кажется…"
    show polya surp school close with dspr
    "Она сделала лицо более серьёзным и чуточку замедлила ход."
    polina "Что хотя бы ты должен разобраться с этим. Тебе же не всё равно, да?"
    ilya "Да, Полин, но если ты не обратила внимания, то на улице сейчас конец весны и школьный год закончится, а портить себе летние каникулы у меня нет сильного желания."
    polina "Как дела с Аней?"
    "Этот вопрос был достаточно… Достаточно неожиданным для меня. Она конечно же знала, что я влюблен в Аню и знала о наших непростых отношениях. Вопросы на эту тему были под табу, но видимо не сегодня. Что ж. Сыграю по её правилам."
    ilya "Никак, а что?"
    polina "Никак - это как?"
    ilya "А вот никак. Нет ничего. Пустота."
    polina "М… Странно. Ты обычно так вокруг неё крутился…"
    ilya "Ничего я не крутился!"
    show polya smile school close with dspr
    "Полина улыбнулась, хихикнув."
    hide polya with dspr
    scene bg ext_house_pol with dissolve
    stop music fadeout 3
    "Её дом был уже перед нами, остается всего-то перешагнуть дорогу и ву-аля."
    stop sound
    $ renpy.pause(1.0)
    scene bg entrance with dissolve
    play sound shagi_padik
    $ renpy.pause(4.5)
    scene bg lest_kletka with dissolve
    stop sound
    "Подъём по лестницам был для меня извечно тяжким трудом и неподъёмной ношей."
    show polya neitrall school close with dspr
    polina "Илья, ты всё ближе и ближе к цели…"
    ilya "Ну, Полиночка, я не могу так… "
    play music escape fadein 3
    "Я встал на колени на пыльную ступень."
    polina "Ты чего!?"
    show polya neitrall school with dspr:
        polya_sit
    "Она спустилась и присела передо мной на корточки."
    #нейтрал с румянцем
    polina "Илюш, я тебе твою любимую подушчеку дам…"
    "После этой фразы у меня появился сильнейший приток сил, из-за чего мои ноги сами понесли меня к двери её квартиры."
    "Подушечка… Я в доме Полины бывал, разумеется, ни один раз, и мне приглянулась одна подушка."
    "Она была какой-то особенно мягкой… Не знаю как описать. Вроде обычная подушка, но на ней так приятно лежать…"
    hide polya with dspr
    play sound shagi_padik
    $ renpy.pause(2.9)
    stop sound
    "Наконец Полина поднялась на свой этаж, а я как-то доковылял."
    "В конце концов она вставляет ключ в замочную скважину и открывает дверь."
    scene bg pr_koridor with dissolve
    "Заходя, я заприметил кота, лежащего на подушечке, которую мне обещали дать."
    polina "Видимо не полежишь."
    "С улыбкой сказала девушка."
    ilya "Абрикосик…"
    "Тихо вымолвили мои уста."
    "Я человек простой. Вижу котика - начинаю его интенсивно гладить, как это и было в прошлые разы."
    show cat_hands with dissolve
    with flash_red
    with hpunch
    hide cat_hands
    "Однако сегодня, видимо, действительно особенный день, поэтому, когда я потянулся к коту - он, вместо приятного урчания, укусил меня."
    ilya "Ай!"
    polina "Коты всё чувствуют…"
    ilya "Не знаю что чувствуют коты, но я почувствовал пока что только боль от укуса..."
    polina "Бедненький, почувствовал укус кота, оу-вау."
    stop music fadeout 3
    ilya "Просто я не ожидал, что он сильно укусит."
    play music love_theme fadein 3
    "Действительно, в этот раз Абрикос, так звали ее котика, укусил меня сильнее обычного. Каждый раз, когда я был дома у Полины, это было более слабо, будто он так со мной здоровался, а в этот раз... Будто прогоняет."
    "Ладно, смирюсь с тем, что сегодняшний день больше похож на кусочек черноты, заключающей в себе кучу зла, обид и агрессии. Меня ждал пирог и, пожалуй, это могло по-настоящему осчастливить меня."
    "Пока я стоял и размышлял, пытаясь снять со своей правой ноги ботинок, Полина уже успела разуться, добежать до кухни, достать откуда-то пирог и вернуться ко мне."
    polina "Ты похож на бабульку из сказки, сидящей у разбитого корыта..."
    "Она задумалась на пару секунд."
    polina "Только ты стоишь у башмака и пытаешься снять второй."
    "Заключила девушка."
    "Я выдавил из себя улыбку и наконец закончил процесс снятия ботинка."
    ilya "Пошли, Полин..."
    hide polya with dspr
    "Она приблизилась  ко мне сзади и обняла."
    polina "Тебе больно?"
    ilya "Честно говоря да, ты слишком сильно сдавливаешь в районе сонной артерии."
    polina "О Боже, Илья!"
    "Она отпустила меня и побежала на кухню, я последовал вслед за ней."
    scene bg polina_home with dissolve
    polina "Тебе какой кусочек?"
    ilya "Давай вот этот..."
    "Стоя над пирогом, я выбрал самый большой. Не сказать, что люблю максимализм, но между большим количеством еды и маленьким количеством еды, я выберу первое, хотя... Это смотря какая еда."
    polina "Жлоб, опять себе большой забираешь."
    "Обиженно сказала Полина."
    ilya "Ладно, давай тот, что выбрал я достанется тебе, ну, как бы в подарок за окончание учебного года, а я возьму вот этот."
    "Мой палец показал на кусочек чуть поменьше."
    polina "Знаешь..."
    "Она развернулась."
    polina "Ты похож на моего дядю еврея, который постоянно проделывал примерно такие же махинации."
    ilya "Ну,если только немножко."
    "С улыбкой ответил я."
    "Наконец, мы приступили к трапезе, сев за круглый стол рядом друг с другом. Отломив один кусочек и попробовав его, я почувствовал мягкость ягод, их свежесть и слабоватый кисло-сладкий вкус..."
    ilya "Это восхитительно."
    "Каждый раз оказываясь в её квартире, я чувствую какое-то тепло в душе. Она такая домовитая хозяюшка... Я взял новый кусочек пирога в рот."
    polina "Илюш..."
    show polya shy school close with dspr
    "Она пододвинулась ближе так, что её плечо коснулась моего, а талия была буквально в 10 сантиметрах."
    stop music fadeout 3
    play music negation fadein 2
    polina "Я вот хочу тебя спросить тебя о кое-чем..."
    "Полина проглотила слюну, улыбнулась и посмотрела наконец мне в глаза."
    polina "Если бы я сказала, что ты мне, ну, нравишься не как друг, а как любовник скорее."
    "Я поперхнулся, но быстро пришёл в себя."
    ilya "Прости, что?"
    polina "Ну, ты говорил..."
    "Она приобняла меня за спину."
    polina "Что с Аней у тебя ничего нет, а я будучи с тобой так долго рядом свыклась с тем, что ты всегда близко и так тепло ко мне относишься. Теплее, чем к кому-либо другому."
    "Она прижалась сильнее, в то время, как в голове у меня проносилась лишь одна мысль."
    th "Так, я имею два друга: Серёжу и Полину. Мне к Серёже что ли теплее относиться или что?"
    "На самом деле такое стечение обстоятельств для меня было совсем удивительным. Мы были знакомы уже чуть больше, чем 7 лет, но о наших любовных отношениях речи ещё никогда не заходило. Мою душу начали терзать смутные сомнения. Сомнения, которые душили меня, будто взяли за горло, и раздирали изнутри."
    ilya "Полин, я хочу сказать тебе кое-что..."
    "Не надо..."
    "Она с улыбкой, коснулась моей щеки незанятой рукой."
    ilya "Нет, я настаиваю..."
    polina "Не стоит."
    ilya "Да стоит! То есть, не стоит, а стоит..."
    th "Неудобно вышло..."
    show polya angry school close with dspr
    ilya "Полина, я не могу представить наши отношения выше, чем просто дружеские, я не могу ответить тебе взаимностью, прости."
    "Её рука на моей щеке резко сжалась, а со спины убралась."
    play sound hit_face_ladon 
    with flash_red
    hide polya with dspr
    extend "Резким движением, я получил смачную пощечину, от которой у меня даже немного потемнело в глазах. После чего вскочила из-за стола и отошла к раковине."
    ilya "Ты... Ты... Чего?"
    polina "Идиот. Всю жизнь так и провозишься с девушкой, которой на тебя совершенно плевать, вот и пробуй завести с ней отношения дальше, осёл."
    ilya "Чего ты так завелась, успокойся...{nw}"
    show polya angryteers school close with dspr
    polina "Тебе лучше уйти, Илья..."
    "Всхлипывая пробурчала девушка, после чего развернулась ко мне от раковины. Её глаза были наполнены слезами, а взгляд был мучительным."
    ilya "Нет, давай мы поговорим, пожалуйста."
    polina "Уйди. Пожалуйста."
    play music going_home fadein 3
    "Коротко и холодно сказала Полина, не отводя взгляд от меня. Все, что мне оставалось сделать в этой ситуации – это только уйти, дабы избежать бòльшего кровопролития. Не просто так у меня это предчувствие было сегодня утром, что день сложится погано. Натянув на себя ботинки и взяв рюкзак, я вышел из её квартиры, бросив на неё свой взгляд."
    th "Что же я натворил..."
    hide polya with dspr
    scene bg lest_kletka with dissolve
    "Спускаясь по лестнице вниз, я лишь думал о произошедшем внутри себя... Она ведь абсолютно права, я попросту заложник своих симпатий к Ане и ничего более, в то время, как Полина всегда была рядом, иногда оберегала меня... Зачем же я так с ней."
    scene bg entrance with dissolve
    $renpy.pause(0.5)
    scene bg ext_ser_house_pol with dissolve
    "Наконец я вышел из душного и мрачного помещения на не менее душную и мрачную улицу. Облака вновь напали на городское небо и приглушили солнечный свет."
    th "Так даже более хорошо для моего нынешнего состояния."
    th "Так, ладно. Я был не прав, абсолютно не прав. Полина мне тоже нравится, к тому же нравится ни разу не меньше этой красноволосой бестии. Жаль, что поняла она это быстрее меня. Ладно, ничего плохого в этом нет. Вот прямо завтра пойду к ней, взяв цветы в местном ларьке и все будет хорошо. Мы помиримся с ней, отдохнём."
    th "Доем пирог тот..."
    scene bg ser_sssr with dissolve
    "А, черт, встреча с Серегой же завтра, точно. Да уж, как все закрутилось. У меня иногда чувство возникает, что в этом мире все борются против меня, но только сейчас пришло осознание, что это я сам всех настраиваю против себя."
    th "Вот, к примеру, Николай. Он чувствует конкуренцию по отношению ко мне, вот и проявляет агрессию, дабы отпугнуть от своей девушки, а девушка-то мне его и не нужна по факту... Ладно, ничего. Все наладится. Вот приду домой, лягу в ванне с книжкой. Почитаю, отдохну, за ночь обмыслю на чистую голову как извиниться и все будет...{nw}"
    play sound gudok_car
    stop music
    "Резкий гудок автомобиля вывел меня из моих мыслей."
    scene bg razm
    play sound sfx_punch_washstand
    play sound ear_noice
    with hpunch
    with vpunch
    with flash_red
    show red_corn
    play ambience sfx_bones_breaking
    play sound ear_noice
    "Последовал сильный удар... Я почувствовал, как мое бедро хочет выскочить с другой стороны. Все мысли казались какими-то пустыми, а боль распространялась по всему телу."
    "От удара я подлетел вверх, подобно футбольному мячу, и, развернувшись вокруг своей оси, упал на асфальт головой. Где-то послышался хруст. Сильнейшая боль по всему телу, я чувствовал, что мое лицо и вся часть тела, подвергшаяся удару была всмятку."
    "Я не чувствовал ни ног, ни вообще нижней части своего тела, будто бы его вообще нет. Глаза постепенно начали закрываться, а последнее, что я услышал был крик людей и топот ног, направляющихся ко мне."
    show blink
    "Всё сознание перевернулось и мои веки закрылись..."
    stop sound