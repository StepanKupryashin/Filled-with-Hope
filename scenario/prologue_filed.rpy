init:

    $ mods["wks_index"]=u"modTest"
    $ voj = Character(u'Вожатая',color="#32CD32")
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
        "day": (240, 230, 140, 255),
        "sunset": (240, 230, 140, 255),
        "night": (240, 230, 140, 255),
        "prolog": (240, 230, 140, 255) }
    $ store.names_list.append("nik")

    $ names["ilya"] = u"Илья"
    $ colors["ilya"] = {
        "day": (245, 245, 245, 255),
        "sunset": (245, 245, 245, 255),
        "night": (245, 245, 245, 255),
        "prolog": (245, 245, 245, 255) }
    $ store.names_list.append("ilya")
label VN_prolog:
    $ persistent.sprite_time = "day"
    $ day_time()
    play sound sfx_bus_idle
    play music downby
#шум мотора автобуса и голоса как пионеры пиздят fadein 2# 
    scene bg int_bus_people_day
    "Здравствуй жаркий июль." 
    "После месяца откровенного тунеядства родители решили справить меня в один интересный лагерь."  
    "Я пару раз бывал в лагерях, но место, в которое я еду, обещает быть чуть более необычным." 
    "Вроде как нас вырядят в пионеров и заставят вернуть атмосферу давно несуществующего Советского Союза.{w} А это значит, что никакого интернета, только живое общение.{w} Но это не по мне." 
    "В общении с людьми я был полным профаном.{w} Уж не знаю как так вышло, но с детства не получалось спокойно вести диалог с кем-либо." 
    "Я сильно волновался и не мог найти общий язык.{w} Тогда что же я забыл в лагере?" 
    "Мне никогда не нравились мои социальные навыки.{w} Не раз слышал, что помогает выход из зоны комфорта.{w} Так что поездка — это, своего рода, эксперимент." 
    "Новая жизнь или попытка наладить старую.{w} До конца еще не разобрался." 
    "Только пока что результат нулевой."  
    "Ребята общаются друг с другом, хотя знакомы от силы час." 
    "А я сижу один и пялюсь в окно.{w} В наушниках играет что-то меланхолично спокойное, почти заглушая чужие разговоры и шум двигателя." 
    "Не знаю сколько осталось ехать.{w} Надеюсь недолго." 
    "От духоты в салоне слегка кружилась голова, да и обилие различных женских духов создавало неповторимый аромат, от которого хотелось задушить себя ремнем, лишь бы не терпеть этот ужас." 
    "Зато пейзажи за окном крайне живописные." 
    "Бескрайние поля с посевами, небольшие огороженные избушки и все это тонуло в ярко зеленых зарослях, среди которых иногда встречались немногочисленные деревья." 
    "Лето во всей его красе." 
    th "Пока есть возможность, надо ловить момент." 
    "С этими мыслями я разблокировал телефон, нашел приложение камеры и сделал пару неплохих фотографий." 
    "Хотелось бы, чтобы они напоминали мне о чем-то приятном." 
    "Мои мысли прервал беспощадный зевок.{w} Видимо, разморило." 
    "Судя по всему, ехать еще около часа, так что могу позволить себе вздремнуть." 
    th "Надеюсь меня не забудут разбудить..." 
    "Я прикрыл глаза и растворился в солнечном свете."
#(SkaR - Down by the Riverside)(stop)#
    stop music fadeout 2
    stop ambience fadeout 2
    show blink
    "..."
    scene bg int_bus_people_day
    show unblink
    $renpy.pause(3)
#тут небольшая пауза типа спит#
    play music Reflection  
#(Денис Баклин) - (Reflections(play)#
#просто шум детей#
    stop sound
    "Удивительно, но я проснулся сам." 
    "Наушники выпали из ушей и шумные переговоры людей разбудили меня." 
    "Немногочисленные мальчики помогали девочкам достать чемоданы, а значит мы на месте." 
    "Я встал с сидения, размялся и закинул на плечо спортивную сумку со своими скромными пожитками." 
    "Дабы не помереть в толкучке, я подождал пока основная масса людей выползет из автобуса и вышел сам."
    scene bg ext_bus with dissolve2 
    "Вожатые суетились, сверяя своих новоиспеченных пионеров по спискам." 
    "Я стоял в сторонке и оглядывался." 
    th "Совенок... Кстати, неплохое название." 
    "Ворота выглядели старыми и скрипучими, но не вызывали отторжения.{w} Скорее наоборот, манили зайти и окунуться в местную густую атмосферу." 
    "Воздух здесь разительно отличался от городского.{w} Он был свежим, чистым." 
    "Казалось, что никогда не дышал всей грудью, а сейчас как вздохнул..."
    play sound sfx_inhale
#звук вдоха#    
    "Приятное тепло разбежалось по всему телу." 
    "Легкий ветерок помогал от палящего солнца.{w} Да и в целом впечатления пока очень приятные, но кто-то помешал мне наслаждаться видами." 
    show mt normal pioneer with dissolve
#до того, как од представится надо подписывать ее как Вожатая#    
    voj "Ты Семен, да?" 
    "Передо мной стояла молодая девушка.{w} Лет 25, не больше." 
    "К слову очень даже миловидная.{w} Я слегка напрягся, ведь, как известно, все проблемы начинаются из-за красивых женщин." 
    me "Да."
    show mt smile pioneer
    voj "Отлично, ты в моем отряде. Пойдем."
    hide mt with dissolve
    "Я послушно пошел за вожатой и оказался рядом с небольшой группой людей."
    scene ext_camp_entrance_day with dissolve2
    show polya neitrall school close at left with dspr
    show anya smeh school close at center with dspr
    show sl smile sport close at right with dspr
#спрайты полины ани лены слави с дефолт еблами#    
    "Мельком оглядев своих будущих товарищей, отметил, что в отряде преимущественно девочки."
    hide polya with dspr
    hide anya with dspr
    hide sl with dspr
#скрыть спрайты#
    show el normal pioneer at cleft with dissolve
    show sh normal pioneer at cright with dissolve
    "Из мальчиков я увидел только двух белобрысых.{w} Один в очках, другой с гнездом на голове."
    "Видимо, не суждено мне с ними подружиться.{w} Ну и плевать.{w} Кому нужны друзья, когда тут такой рассадник цветущих розочек."
    hide el with dissolve
    hide sh with dissolve
    show mt normal pioneer with dissolve
    "Вожатая пересчитала нас по головам, еще раз сверилась со списком и повела за ворота."
    "..."
    scene bg ext_square_day with dissolve2
    "Cпустя какое-то время мы дружным шумным балаганом оказались на площади" 
    "Она представляла собой бетонный плац, стройные ряды скамеек в тени густой листвы и, видимо, главная достопримечательность - памятник неизвестному мне гражданину." 
    th "Стоило меньше прогуливать историю..." 
    "Без пяти минут пионеры разбились по группкам и стояли в ожидании указаний." 
    "Я держался поближе к своему отряду, но все так же оставался этакой белой вороной." 
    "Бегло оглядев свой будущий коллектив, мне удалось заметить, что я не единственная одиночка в этом царстве любви и дружбы." 
#всех девочек надо разодеть хуй пойми во что, ибо пионерской формы у них еще нет, нврн из бкрр надо спрайты спиздить или сценарий переписывать.#    
    show un shy pioneer far with dissolve
    "Девочка со смешными хвостиками так же держалась на безопасном расстоянии.{w} По ее лицу понятно, что такое столпотворение людей действует ей на нервы." 
    hide un
    "Когда-то я тоже был таким, но позже социопатия превратилась в тотальное безразличие." 
    "По началу мой стеклянный взгляд напрягал одноклассников." 
    "Особо небезразличные даже предпринимали попытки как-то заговорить со мной, узнать кто такой у меня умер." 
    "В итоге я остался один и все разом сделали вид, будто меня не существует.{w} А я и не против." 
    "В воспоминаниях о прошлом я не заметил как к нам подошла вожатая."
    show mt normal pioneer with dissolve    
    mt "Здравствуйте ребята, меня зовут Ольга Дмитриевна, я ваша вожатая.{w} Пока не знаю кто из вас кто, но очень надеюсь, что мы с вами подружимся.{w} Сейчас нужно провести краткий инструктаж." 
    mt "Наш лагерь называется Совенок, но, думаю, вы уже в курсе. Лагерь у нас не обычный. Наша цель погрузить вас в атмосферу пионерских лагерей и дать вам отдохнуть от современной жизни." 
    mt "Так что теперь вы пионеры. А что это за пионеры без пионерской формы? Её вы получите завтра. Сегодня у нас ознакомительный день. Можете походить по лагерю, осмотреться, а ближе к вечеру распределим вас по домикам." 
    mt "Сейчас по расписанию обед, я вам покажу где столовая. Позже будете сами ориентироваться. Если слышите горн, значит нужно в столовую. Все понятно?" 
    "Пионеры выкрикнули радостное да!" 
    mt "Отлично, пойдемте."
    hide mt
    stop music
#    (Sergey Eybog - Reflection On Water)(stop)# 
    "..." 
#    (Sergey Eybog - Your Bright Side)(play)#
    play music your_Bright
    scene bg ext_dining_hall_away_day with dissolve2
    "По пути к столовой, в толпе я приметил знакомое лицо."
    show anya smeh school  far with dspr
#спрайт ани#    
    th "Аня?{w} Серьезно?" 
    "Не понимаю, как я проглядел свою одноклассницу.{w} Видимо, стоит найти медпункт и проверить зрение.{w} Ну или голову."
    hide anya with dspr
#скрыть спрайт ани# 
    scene bg ext_dining_hall_near_day with dissolve2
    "У столовой была большая очередь.{w} Самыми первыми стояли младшие отряды.{w} Мы же, как самые старшие, заняли место в конце." 
    "Шум пионеров мне уже порядком надоел, так что я размотал запутавшиеся наушники и включил случайную песню из списка, но спокойно витать в облаках мне не дали."
    show sl normal sport close with dissolve
    sl "Привет!" 
    "Я вытащил один наушник." 
    me "Чего?{w} Не услышал." 
    "Девочка ласково улыбнулась и повторила." 
    sl "Привет!{w} Тебя как зовут?" 
    th "Ух ты, я теперь популярен у девушек или ей что-то от меня нужно" 
    me "Э...{w} Семен." 
    "Мой голос слегка дрогнул.{w} Кто же знал, что со мной попытается познакомиться девушка.{w} К слову, очень даже симпатичная." 
    th "Мда, мне бы писать мануалы о том, как создать ужасное первое впечатление."
    show sl smile sport close with dspr
    sl "Приятно познакомится.{w} А меня Славяна зовут, но это слишком официально, так что называй меня просто Славей, хорошо?" 
    "Девочка слегка смутилась и поправила непослушную прядку волос." 
    "Я же загляделся на нее.{w} Золотистые волосы, аккуратно собранные в две длинные косички, слегка красноватый румянец на щеках и очень красивые голубые глаза, которые будто затягивали в глубину вод, где потонет даже самое крепкое судно." 
    me "Хорошо, договорились." 
    "Славя улыбнулась еще шире, а я насторожился." 
    "Казалось бы, девочка просто хотела познакомится, но моя вечная паранойя воссоздает в мыслях кучу ситуаций, где меня обманут, предадут и убьют еще до кучи." 
    show sl serious sport close with dspr
    sl "Все хорошо?{w} Ты какой-то напряженный..." 
    "Славя действительно выглядела обеспокоенной.{w} Может все же остались в мире небезразличные люди?" 
    me "А...да...{w} Устал просто, не волнуйся."
    show sl sad sport close with dspr  
    sl "Точно?{w} А то тут медпункт недалеко." 
    me "Откуда ты это знаешь?" 
    "На лицо девочки вернулась улыбка."
    show sl smile sport close with dspr
    sl "Не первый раз тут.{w} Каждое лето приезжаю и все никак не надоест.{w} В этом лагере я будто дома." 
    "Меня настораживала такая открытость синеглазки.{w} Обычно люди держатся закрыто, не пускают в свой внутренний мир кого попало." 
    "И я прекрастно их понимаю!" 
    "Пускаешь в святая святых, а они заходят в грязной обуви, оставляя свои следы, которые так просто не отмоешь."
    show sl sad sport close with dspr
    sl "Ты опять замолчал...{w} Уверен, что не нужно к врачу?" 
    "Что же, видимо, Славя разительно отличается от всех, кого я знал раньше." 
    me "Да успокойся, я в порядке." 
    show mt normal pioneer at right with dissolve
    "Наш диалог прервала вожатая, которую я не услышал из-за шума пионеров."
    "Она что-то прошептала на ухо Славе и та, извинившись, оставила меня одного." 
    "А тем временем подошла и наша очередь." 
    hide mt
    hide sl
    
    scene bg int_dining_hall_people_day with dissolve2
    "Взяв поднос с едой, я начал осматривать столовую на наличие свободных мест."
    "На обед давали гороховое пюре и куриную котлету.{w} Метеоризм обеспечен."
    scene bg int_dining_hall_sunset with dissolve
    "Быстро управившись с едой, я довольно откинулся на спинку стула и положил руку на полный желудок."
    th "Мамина еда конечно самая лучшая, но это тоже ничего."
    "Пока я находился в раздумьях, к моему столику подошла девушка с тряпкой."
    show polya angry  school close with dspr
#Полина злость
    "Полина" "Ты же уже поел. Так чего сидишь?"
    "С нотками раздражения в голосе произнесла она."
    "Честно говоря, мне нечего было ответить, потому я уставился на девушку осуждающим взглядом."
    show polya neitrall school close with dspr
#Полина нейтрал
    "Полина" "Фьюх, устала я. Присяду на пару минуток. Заставляют работать прямо с первых дней."
    "Она бросила на меня быстрый взгляд, видимо ожидая каких-либо слов."
    "Ну а что я?{w} Я все ещё был оскорблен таким поведением."
    show polya shy school close with dspr
#Полина смущение
    "Полина" "Ты извини, что я так резко наехала."
    th "Мысли читаешь?"
    me "Да ничего. Всё в порядке."
    show polya smile school close with dspr
#Полина улыбка
    "Полина" "Ты забавно выглядишь. Откатился на стуле, руку на пузо положил, довольный сидишь."
    "Она улыбнулась, и я был просто обескуражен изяществом её улыбки.{w} Такая светлая и добрая.{w} От неё веет теплом."
    th "Она производит приятное впечатление, игривое настроение появилось и у меня."
    me "Да вот думаю, через сколько начнёт действовать горох."
    "Она снова улыбнулась. С ней рядом я не чувствую скованности и неловкости, что удивляет, но не может не радовать."
    th "Улыбка такая же ослепительная, как и у Слави. Она у всех тут такая?"
    "Полина" "Меня Полиной звать. А тебя?"  
    me "Семён Петрович. Приятно познакомиться."
    "Полина" "Тебя Семёном называть, или Петровичем?"
    th "Какой запал и дерзость в улыбке.{w} Ух."
    me "Можно просто Сема."
    "Полина" "Договорились, Сема. Пойду я, дел невпроворот. Ещё увидимся."
    me "Всего доброго."
    hide polya with dspr
#убирай спрайт    
    "Она взяла в руки тряпку, поднос, и удалилась в сторону раздачи."
    "Только сейчас я приметил её чудную фигурку и внешность."
    "Волосы весьма необычного цвета, в прочем, в наше время это нормально."
    "Стоит к ней присмотреться.{w} Уж очень легко я чувствую себя рядом с ней."
    th "Чертовщина какая-то..."
    show blink
#тут переход через затемнение, я просто не помню как его делать
    
    scene bg ext_dining_hall_near_sunset
    hide blink
    show unblink
    
    "Когда я вышел из столовой солнце начало алеть.{w} Близился закат, а с ним и конец дня." 
    "Было удивительно тихо." 
    "Никогда не думал, что такая тишина бывает в лагере на сотни человек." 
    th "Ну и чем тут можно заняться?" 
    "Вожатая сказала осматривать окрестности, так что я пошел куда глаза глядят." 
    "..." 

    play music SkaR_PeacefulForest
#(SkaR - Peaceful Forest)(play)
#снова через затемнение    
    scene bg ext_boathouse_sunset 
    "В итоге вышел на пристань." 
    "Небольшая будка, где, видимо, обитает сторож.{w} Привязанные лодки.{w} Успокаивающий звук воды." 
    "Я медленным шагом шел по скрипучим доскам, смакуя каждую секунду спокойствия." 
    "Как и любого интроверта, меня утомляло длительное присутствие людей.{w} Даже если стоишь в сторонке, все равно ощущаешь давление и скованность."   
    "Сейчас же у меня получилось вдохнуть всей грудью и расслабится." 
    "Под вечер у меня всегда появляется мрачная меланхолия.{w} В такие моменты нужно забиться в самый дальний угол, где никто тебя не тронет." 
    "Но мне в очередной раз не повезло." 
    "Сзади меня скрипнула доска и я обернулся." 
    th "Вот только ее сейчас не хватало."
    show anya neitrall school close with dspr
#Аня нейтрал    
    anya "Приветик." 

#убирай спрайт 
    hide anya with dspr
    "Она первая заговорила со мной..."
    "За столько лет совместного обучения и парой слов не перекинулись, а тут девушка сама проявляет инициативу.{w} И вот как мне на это реагировать?"  
    "Несмотря на то, что я и глазом не повел, внутри меня было все вверх дном."
    "Чего-чего, а того, что Аня проявит инициативу в мою сторону я не ожидал."  
    th "Ненавижу это чувство." 
    "Дико ненавижу то, в чем по уши.{w} Сомнения, нерешительность, страх."
    "Встань и возьми, но нет."
    "Куча оправданий, чтобы остаться на месте.{w} Ничего не теряешь, ничего не получаешь."
    "Стабильность."
    "Да только в долгосрочной перспективе куда вымощена эта тропинка?"  
    "Я согласился на поездку в лагерь ради движения вперед, но даже на новом месте я остался старым собой."
    "А видимость изменений лишь кормили мою уверенность, что я делаю все правильно.{w} Только теперь вопрос встал куда более сложный.{w} Чего конкретно я хочу?"
    "Вот когда пойму, тогда уже можно подумать о возможностях и путях.{w} А пока что остается тонуть в старых незатянувшихся ранах."
    "Когда-нибудь я поведаю о них кому-то достойному моих откровений."
    "Когда-нибудь, но не сейчас."
    "Не готов пока выйти на эшафот со свой гильотиной." 
    "Аня" "Ты чего встал столбом? Присаживайся." 
    "Ее голос звучал одновременно и тепло и холодно."
    "Еще в школе я заметил, что она...носит маску?"
    "Вроде приветливая и дружелюбная девочка, душа компании и вся такая милая, но чувствовалась в ней эта неискренность. " 
    th "Ладно, черт с ним." 
    "Я послушно присел рядом и продолжил молчать, не в силах найти слова."
    show anya neitrall school close with dspr
#Аня нейтрал    
    "Аня" "Бывает же такое. Кого угодно ожидала лагере встретить, но только не тебя. Какими ветрами занесло?" 
    "Я удивлением услышал свой голос."
    me "Сам не знаю...{w}Так вышло.{w} А ты с какой цель приехала?"
    show anya smeh school close with dspr
#Аня улыбка    
    "Девочка улыбнулась своей фирменной натянутой улыбкой, которая могла означать что угодно, только не дружелюбие."  
    "Аня" "Отдыхать конечно! Зачем еще в летние лагеря ездят?"
    me "Извини за нескромный вопрос, а от чего ты устала?"
    show anya surprise school close with dspr
#Аня удивление    
    "Аня покрутила пальцем у виска." 
    "Аня" "Ты дурак что ли?"
    "Аня" "Учеба, общение, дополнительные занятия, подготовки к экзаменам - все это жутко выматывает. "
    "Девочка состроила недовольную рожицу." 
    me "Никогда бы не подумал, что такую как ты сможет вымотать общение."
    show anya shy school close with dspr
#Аня смущение     
    "Аня" "Знаешь, быть популярной не так легко, как тебе кажется." 
    me "О да, даже представить не могу как это купаться в лучах славы и постоянно видеть влюбленные взгляды." 
    "Аня" "Ты бы хотел такой жизни?" 
    "Вопрос поставил меня в тупик, и я задумался." 
    th "Хотел бы?" 
    me "Даже не знаю. Наверно нет." 
#Аня нейтрал
    show anya neitrall school close with dspr
    "Аня" "Я тоже не хотела, но быть изгоем - это ужасно!"
    "Аня" "Постоянные косые взгляды, перешептывания за твоей спиной. Натерпелась всего этого. Пришлось много трудится, чтобы стать хорошей для всех." 
    me "И что, оно того стоило?" 
    "Аня" "Стоило. Пусть люди вечно хотят моего внимания. Пусть каждый дурак в тайне мечтает, что именно он особенный. Пусть мне делают гадости из зависти. Все это лучше, чем считаться отбросом. "
    me "Неужели тебя так волнует чужое мнение?" 
    "Аня скорчила недовольную рожицу." 
    "Аня" "Тебе ли не знать, что люди бывают злыми."
    "Аня" "Разве не замечал, что тихих одиночек часто обижают, потому что они не могут за себя постоять?"
    "Аня" "Если бы все просто думали. Они свободно могут наговорить тебе гадостей или еще чего хуже сделать." 
    me "И поэтому ты решила, что лучший выход - это сделать себя идеальной в их глазах?" 
    "Аня" "Да." 
    me "Что же, тебя можно понять. Хотя я бы так не смог." 
    show anya smeh school close with dspr
#Аня улыбка     
    "Аня" "А ты и не должен. У каждого свои принципы и методы." 
    "…"
    scene bg ext_boathouse_night with dissolve
#тут затемнение
    $ renpy.pause(2.0)
    $ persistent.sprite_time = "night"
    $ night_time()
    "Мы так заболтались, что не заметили как стемнело." 
    "Аня" "Ладно, пора с жильем определится." 
    me "А, точно. Я уже и забыл."
    "Аня" "Спасибо за компанию."
    "Аня" "Никогда бы не подумала, что мы сможем так поговорить. Если бы не лагерь, так бы и слова друг другу не сказали до самого выпуска." 
    me "Да не за что. Было интересно тебя послушать." 
    "Аня" "Эх, кто знает какие еще сюрпризы приготовили нам эти каникулы…" 
#(SkaR - Peaceful Forest)(stop)
    stop music
    "…"
#тож через затемнение    
    scene bg ext_square_night with dissolve
#(pathways_7dl [Micheal Ortega - Night of rain])(play)
    play music pathhh
    "Мы молча двинулись в сторону площади."
    "Каждый молчал о чем-то своем.{w} Слова казались излишними.{w} Уже достаточно сказано." 
    "Так же беззвучно разошлись в разные стороны, и только сейчас я задумался."
    th "Что это сейчас было?"
    "Воспоминания о нашем диалоги резко превратились в туман, будто это был скоротечный сон."
    "Не знаю зачем, но я ущипнул себя."
    th "Не сплю, живой."
    "Странное, однако, место.{w} Только приехал а уже столько эмоций."
    "Никогда столько не разговаривал, никогда не чувствовал такой подъем."
    "Дальше лучше, правда?"
    "Только вот что дальше?"
    "И как ответ, прозвучал сигнал, зовущий на ужин."
    th "Ужин, так ужин.{w} Как скажете."
    "Я неторопливо потопал к столовой.{w} Благо запомнил где она."
    "Скорее всего там опять длиннющая очередь, так что спешка ни к чему."
    "..."
#снова затемнение
    scene bg int_dining_hall_people_day
    "Как я и думал, очередь была, но в этот раз никто не мешал витать в облаках."
    "Мне удалось занять пустой столик в дальнем углу столовой."
    "Аппетита не было, потому я просто перемешивал содержимое тарелки, оглядывая местных пионеров."
    "Некоторые из них уже успели обзавесись формой с ярко красным галстуком.{w} А я вот до сих пор сижу в том, в чем приехал.{w} Так даже лучше, наверное."
    "Как-то не горел желанием одевать эти короткие шортики и жесткую рубашку, однако, что поделать раз уж тут такие правила."
    "Издали я приметил нашу молоденькую вожатую, которая моталась по всей столовой, видимо, собирая свой отряд.{w} И вот дошла до меня."
#фон ночного склада, который мы спиздим
    "Дальше мы пришли на склад, где уже знакомая мне Славя на глазок подбирала пионерам форму."
    "Все это дело протекало, на удивление, быстро."
    scene bg ext_square_night with dissolve
    "Позже на площади начался разговор о жилплощади."
    "Самое время, надо сказать."
    "Солнце почти полностью опустилось за горизонт, холодный ночной ветер заставлял ежиться от холода."
    "Когда незаселенным остался лишь я, вожатая подошла ближе."
    mt "Эх, Семен.{w} Проблема."
    mt "Свободных домиков, похоже не осталось.{w} Стало быть будешь жить со мной."
    th "..."
    me "Чего?"
    mt "Да, это не по правилам, а что поделать."
    "Ну а чего я ожидал со своей то удачей."
    menu:
        "Ладно":
            jump  od_rut_1day
        "Может поищем еще?":
            jump  polya_rut_1day
#ВЫБОР: Ладно/Может поищем еще?

#Ладно(рут ОД):
label od_rut_1day:
    show mt smile pioneer
    mt "Вот и отлично." 
    mt "Скоро уже отбой, так что пойдем покажу тебе где домик."
    "Я послушно поплелся за вожатой."
    hide mt
    scene bg night_houses with dissolve
#    scene bg ночная улица с домиками, проебал фон
    "По пути разглядывал других ребят, которые разбились по парам и отпирали двери своих берлог."
    "Видно, я один такой удачливый."
    "Хотя, с другой стороны, может это лучше, чем жить в паре с каким-то другим пионером?"
    "Ольга Дмитриевна производила на меня приятное впечатление.{w} Когда слышишь слово вожатая, представляет стараю злую тетку, которая вечно кричит."
    "Девушка, что сейчас идет чуть впереди меня не такая."
    "По крайней мере мне так казалось."
    scene bg ext_house_of_mt_night_without_light with dissolve
    "Вскоре мы остановились у домика, который буквально тонул в кустах сирени и больше походил на заброшенную деревенскую избу, которую время все-таки пощадило."
    show mt smile pioneer
    mt "Вот тут мы и будем жить.{w} Надеюсь на приятное сожительство."
    "Вожатая мило улыбнулась."
    hide mt with dspr
    "Да только сложно было верить ее улыбке."
    "Какой бы искренней она не казалась, я знал, что на курсах психологии ее учили как находить подход к каждому подопечному."
    "И судя по тому, у нее получилось расположить у меня к себе, она хорошая манипуляторша."
    "Или просто хорошая?"
    th "Ладно, не важно."
    scene bg int_house_of_mt_noitem_night with dissolve
    "Мы зашли в домик."
    "Вожатая показала мое койко-место, после чего велела отвернуться и переоделась в легкомысленный домашний халатик."
    "Я же просто стянул новоприобретенную форму, улегся в постель и отвернулся к стенке."
    show mt normal pioneer with dspr
    mt "Я тебя сильно смутила?"
    "Голос Ольги Дмитриевны звучал обеспокоенно."
    me "Нет, просто устал. Спать хочу."
    mt "Тогда спокойной ночи.{w} Завтра важный день."
    me "И вам того же."
    hide mt
    "Еле слышные шаги до выхода из домика и комната погрузилась во мрак."
    scene bg int_house_of_mt_night2 with dissolve
    "В этот момент я будто ощутил всю тяжесть планеты."
    "Не знаю где и когда умудрился так устать, но сон пришел очень быстро."
    "Пусть он будет длинным и приятным."
    
    
    
    
#Может поищем еще?(рут Полины):
label polya_rut_1day:
    show mt normal pioneer close with dspr
    me "А может получше поищем?"
    "Ольга Дмитриевна задумчиво уставилась в список.{w} Забавно постукивая пальчиком по подбородку, она изучала каждую строчку."
    mt" Есть тут один домик..."
    mt "Правда, там кровати немного неустойчивые.{w} И замок заедает.{w} Ещё и дверца шкафа сломана."
    mt "Не знаю, кто там жил до этого. Думала не буду заселять туда никого.{w} Только если на крайний случай."
    me "Беру!"
    mt "Отлично.{w} Так…"
    "Она нашла ключ от моего будущего жилища и передала мне."
    mt "Вот.{w} Можешь заселяться."
    me "Спасибо большое, Ольга Дмитриевна."
    "Улыбнувшись мне, она направилась по своим делам.{w} А я же в свою очередь пошёл заселяться."
    hide mt with dspr
    scene bg gg_house with dissolve
#//домик гг// хз пока какой домик на фон, Юрий, решай
    "Повозившись с замком, я вошёл в свое жилище."
    me "Не так плачевно, как я думал."
    "Я стукнул ногой по ножке кровати, и та слегка затряслась."
    "Улегшись на неё, я закинул руки за голову, пытаясь уснуть."
    "Как бы я не старался заснуть, сон все никак не хотел идти.{w} То ли виной тому новое место, то ли духота."
    "Я решил не мучиться, перекатываясь с одного бока на другой."
    scene bg ext_beach_night with dissolve
    "Побродив по ночному лагерю, я вышел к пляжу."
    "Живописное место, особенно при свете луны."
    "Её мягкий свет отражался в воде, придавая этому месту загадочную атмосферу." 
    "Волны спокойно и небрежно бились об берег."
    "Сняв сандали, я ступил в воду по щиколотку."
    th "Прохладная...{w} купаться в такой сейчас не лучший вариант.{w} Хотя...{w} слягу с простудой и уеду домой."
    play sound sfx_fall_wood_floor
#//звук того, как что-то упало на деревянный пол//
    "Обернувшись в сторону звука, я заметил по правую сторону пляжа брандвахту."
    "Звук раздался снова."
    th "Стоило бы проверить."
    "Надев сандали обратно, я медленно поплелся в сторону этих звуков."
    scene bg ext_boathouse_night with dissolve
    th "Никого...{w} может стоит взойти и оглядеть с другой стороны?"
    "Сказано – сделано.{w} Я взошел на брандвахту, и стараясь не шуметь направился по ту сторону."
    scene bg night_water with dissolve
#//бг воды со стороны брандвахты// не ебу чо за бг
    "Девочка.{w} Лежит на скамейке, держа в руке телефон."
    "Видимо, так и не заметила меня. Либо просто не подаёт виду."
    show polya neitrall school close with dspr
#Полина нейтрал
    "Полина" "Тоже пришёл полюбоваться ночным небом, Сема?"
    "Раздался женский голос со стороны скамьи."
    me "Звуки странные услышал.{w} Из любопытства решил проверить."
    "Полина" "Вот оно как..."
    "Девушка выпрямилась, глянув в мою сторону."
    "Полина" "Присаживайся?"
    "И только сейчас я узнал в ней Полину."
    "Девушку, чья улыбка заставляла чему-то светлому в душе просыпаться."
    "Под светом луны её кожа выглядела бледной.{w} Будто призрак сошёл с картины."
    me "Да.{w} Сейчас."
    "Сев рядом с ней, я поднял голову, уставившись в небо.{w} Заметив это, Полина улыбнулась, последовав моему примеру."
    show polya smile school close with dspr
#Полина улыбка
    "Полина" "Красиво, правда? Лунный свет падает на воду, раскачиваясь на волнах."
    "Полина" "А если привстать и подойти к ограждению, можно увидеть и отражение звёзд."
    "Мечтательно пролепетала она."
    me "Никогда не удавалось увидеть такого в городе.{w} А тут...{w} россыпь звёзд и такая яркая луна.{w} Очень завораживает."
    "Полина" "Да. Именно поэтому я и люблю ночь."
    "Полина" "В посёлке, котором я живу вид точно такой же.{w} Никакой городской свет не мешает."
    me "Я думал ты городская."
    "Полина" "К счастью, нет."
    show polya sad school close with dspr
#Полина грусть
    "Пояснила она, и в этот момент улыбка сошла с её лица."
    me "И откуда ты именно?"
    "Полина промолчала, не моргая смотря куда-то вдаль."
#Скрывай спрайт
    hide polya with dspr
    th "Видимо, не хочет говорить...{w} что ж, ладно, заставлять не буду."
    "Через пару минут послышалось милое сопение под ухом.{w} Я слабо ткнул девушку в бок."
    show polya shy school close with dspr
#Полина смущение
    "Полина" "А?{w} Кого?"
    "Она сонно заморгала глазами, рассматривая моё лицо."
    me "Чего спим?"
    "Полина" "Ой...{w} извини.{w} Я уже не первый раз засыпаю, пока сижу тут."
    "Полина" "Те звуки, которые ты слышал...{w} это телефон из рук падал.{w} Я его подниму, засыпаю, и он снова выпадает из рук."
    "Она смущённо улыбнулась, поправляя локон волос."
    me "Тогда может пойдём по домикам? Вдруг простудишься тут."
    th "Хотя сам недавно думал намеренно простудиться и уехать отсюда..."
#Полина улыбка
    show polya smile school close with dspr
    "Полина" "А ты переживаешь?"
    "В её голосе чувствовалась озорная нотка."
    me "Я этого не говорил."
    "Хихикнув, девушка закинула ноги на скамью, обняв их руками."
    "Полина" "Знаешь, мне кажется, что ночью я чувствую себя живой."
    "Полина" "Тишина, покой, никто не дёргает и не отвлекает. Благодать же."
    me "А тебя так часто отвлекают днем?"
    "Полина" "Есть такое."
    "Полина" "То мама, то бабушка, то отчим…{w} не дают спокойно ничем заняться."
    me "И чем ты обычно занимаешься?"
    "Не сказать, чтобы мне было сильно интересно, но хотелось бы знать хоть что-то о человеке, с которым я ночью провожу время."
    "Мысль меня позабавила."
    "Полина" "Читать люблю.{w} Романы особенно."
    "Полина" "Джоджо Мойес там, Анна Тодд.{w} Еще классическую русскую литературу."
    "Полина" "Ночью приходится включать лампу и заниматься любимым делом."
    me "Зрение ведь так посадишь себе."
    "Полина" "А что поделать?{w} Приходится чем-то жертвовать."
    "Полина" "А тебе что нравится?"
    "Вопрос поставил меня в тупик.{w} Как оно обычно бывает, не знаешь даже что ответить."
    me "Видео-играми увлекаюсь.{w} Почитываю иногда книги.{w} Но больше нравятся визуальные новеллы."
    "Полина" "Никогда не читала их..."
    me "Право, ты теряешь очень многое."
    "Мы вместе засмеялись."
    me "Как-нибудь покажу тебе пару визуальных новелл на телефоне.{w} Действительно интересная вещь."
    "Полина" "Договорились."
    "Глянув на время, я обратился к Полине."
    me "Уже без пятнадцати полночь.{w} Нас ведь не будут ругать, если поймают?"
    "Девушка заговорщически улыбнулась."
    "Полина" "Пусть сначала поймают."
    th "А мне нравится настрой этой дамы."
    "Полина" "Но судьбу мы конечно же испытывать не будем, и двинемся сейчас в кровати?"
    me "Или двинут нам, да."
    "Мы сошли с брандвахты, поднимаясь по песку к основным зданиям лагеря."
    "Полина" "Мне тут сворачивать надо. Так что прощаемся, Семён.{w} Доброй ночи."
    me "Доброй.{w} Не заблудись."
    "Полина" "Снова беспокоишься?"
    "Я хмыкнул, развернувшись в другую сторону, и услышал вслед."
    show polya shy school close with dspr
#Полина смущение
    "Полина" "Дагомыс.{w} Я живу там."
    th "Запомним."
    hide polya with dspr
#Скрывай спрайт
#дом бг через затемнение
    "Дойдя до дома, я улегся в кровать."
    "Сонливость тут же нахлынула, и я не стал ей сопротивляться."    





   





