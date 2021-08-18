
init python:

    wks_prefix_images  = "mods/Workers_Council/images/"
    wks_prefix_name_bg = wks_prefix_images  + "bg/"
    wks_prefix_name_cg = wks_prefix_images  + "cg/"
    wks_prefix_sprites = wks_prefix_images  + "sprites/"
    wks_sprites_anya   = wks_prefix_sprites + "anya/"
    wks_music = "mods/Workers_Council/music/"
    wks_sprites_polya = wks_prefix_sprites + "polya/"
    wks_sprites_nikol = wks_prefix_sprites + 'nikol/'
    ## Автоматическое объявление БГ.

    def wks_define_images():
        for file in renpy.list_files():
            if file.startswith(wks_prefix_name_bg) and file.endswith((".png", ".jpg", ".jpeg")):
                name, _ = file.split(".")
                renpy.image("bg " + name[len(wks_prefix_name_bg):], file)

    wks_define_images()
    
init:
    image cat_hands = "mods/Workers_Council/images/sprites/cat.png"
    image red_corn = "mods/Workers_Council/images/ef/red.png"

    transform polya_sit:
        parallel:
            ease 1.0 ypos 1.1
        parallel:
            ease 0.75 zoom 1.05
            ease 0.5 zoom 1.0

    #АНЯ В ШКОЛЬНОЙ ФОРМЕ ДАЛЕКО И БЛИЗКО.
    image anya neitrall school close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_anya + "school/close/an_smile_school.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_anya + "school/close/an_smile_school.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_anya + "school/close/an_smile_school.png"
    )

    image anya neitrall school far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_anya + "school/far/an_smile_school.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_anya + "school/far/an_smile_school.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_anya + "school/far/an_smile_school.png"
    )

    image anya smeh school close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_anya + "school/close/an_laugh_school.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_anya + "school/close/an_laugh_school.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_anya + "school/close/an_laugh_school.png"
    )

    image anya smeh school far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_anya + "school/far/an_laugh_school.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_anya + "school/far/an_laugh_school.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_anya + "school/far/an_laugh_school.png"
    )

    image anya shy school close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_anya + "school/close/an_shy_school.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_anya + "school/close/an_shy_school.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_anya + "school/close/an_shy_school.png"
    )

    image anya shy school far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_anya + "school/far/an_shy_school.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_anya + "school/far/an_shy_school.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_anya + "school/far/an_shy_school.png"
    )


    image anya surprise school close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_anya + "school/close/an_surp_school.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_anya + "school/close/an_surp_school.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_anya + "school/close/an_surp_school.png"
    )

    image anya surprise school far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_anya + "school/far/an_surp_school.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_anya + "school/far/an_surp_school.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_anya + "school/far/an_surp_school.png"
    )
    #ПИОНЕРСКИЕ СПРАЙТЫ АНИ!
    image anya shy pioneer close =  ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_anya + "pioneer/close/an_shy.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_anya + "pioneer/close/an_shy.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_anya + "pioneer/close/an_shy.png"
    )

    image anya shy pioneer far =  ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_anya + "pioneer/far/an_shy_pion.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_anya + "pioneer/far/an_shy_pion.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_anya + "pioneer/far/an_shy_pion.png"
    )

    image anya neitrall pioneer close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_anya + "pioneer/close/an_sm.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_anya + "pioneer/close/an_sm.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_anya + "pioneer/close/an_sm.png"
    )
    image anya neitrall pioneer far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_anya + "pioneer/far/an_smile_pion.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_anya + "pioneer/far/an_smile_pion.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_anya + "pioneer/far/an_smile_pion.png"
    )
    image anya smeh pioneer close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_anya + "pioneer/close/an_smile_pion.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_anya + "pioneer/close/an_smile_pion.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_anya + "pioneer/close/an_smile_pion.png"
    )
    image anya smeh pioneer far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_anya + "pioneer/far/an_smeh.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_anya + "pioneer/far/an_smeh.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_anya + "pioneer/far/an_smeh.png"
    )

    image anya surprise pioneer close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_anya + "pioneer/close/an_surp.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_anya + "pioneer/close/an_surp.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_anya + "pioneer/close/an_surp.png"
    )

    image anya surprise pioneer far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_anya + "pioneer/far/an_surp_pion.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_anya + "pioneer/far/an_surp_pion.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_anya + "pioneer/far/an_surp_pion.png"
    )


    #ГОЛЫЕ СПРАЙТЫ АНИ(РУКИ ВВЕРХ СУКА)
    image anya smeh naked close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_anya + "naked/close/an_laugh.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_anya + "naked/close/an_laugh.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_anya + "naked/close/an_laugh.png"
    )

    image anya smeh naked far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_anya + "naked/far/an_laugh_naked.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_anya + "naked/far/an_laugh_naked.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_anya + "naked/far/an_laugh_naked.png"
    )
    
    image anya shy naked close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_anya + "naked/close/an_shy.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_anya + "naked/close/an_shy.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_anya + "naked/close/an_shy.png"
    )

    image anya shy naked far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_anya + "naked/far/an_shy_naked.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_anya + "naked/far/an_shy_naked.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_anya + "naked/far/an_shy_naked.png"
    )


    image anya neitrall naked close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_anya + "naked/close/an_smile.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_anya + "naked/close/an_smile.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_anya + "naked/close/an_smile.png"
    )

    image anya neitrall naked far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_anya + "naked/far/an_smile_naked.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_anya + "naked/far/an_smile_naked.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_anya + "naked/far/an_smile_naked.png"
    )
    image anya surprise naked close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_anya + "naked/close/an_surp.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_anya + "naked/close/an_surp.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_anya + "naked/close/an_surp.png"
    )

    image anya surprise naked far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_anya + "naked/far/an_surp_naked.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_anya + "naked/far/an_surp_naked.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_anya + "naked/far/an_surp_naked.png"
    )

    image polya sad naked close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_polya + "naked/close/pol_sad.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_polya + "naked/close/pol_sad.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_polya + "naked/close/pol_sad.png",
    )

    image polya sad naked far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_polya + "naked/far/pol_sad.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_polya + "naked/far/pol_sad.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_polya + "naked/far/pol_sad.png",
    )

    image polya sad school far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_polya + "school/far/pol_fsad.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_polya + "school/far/pol_fsad.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_polya + "school/far/pol_fsad.png",
    )

    image polya sad school close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_polya + "school/close/pol_sad.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_polya + "school/close/pol_sad.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_polya + "school/close/pol_sad.png",
    )

    
    image polya neitrall school far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_polya + "school/far/pol_fneitrall.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_polya + "school/far/pol_fneitrall.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_polya + "school/far/pol_fneitrall.png",
    )

    image polya neitrall school close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_polya + "school/close/pol_neitrall.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_polya + "school/close/pol_neitrall.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_polya + "school/close/pol_neitrall.png",
    )

    image polya smile school far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_polya + "school/far/pol_fsmile.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_polya + "school/far/pol_fsmile.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_polya + "school/far/pol_fsmile.png",
    )
    image polya smile school close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_polya + "school/close/pol_smile.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_polya + "school/close/pol_smile.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_polya + "school/close/pol_smile.png",
    )

    image polya shy school far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_polya + "school/far/pol_fshy.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_polya + "school/far/pol_fshy.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_polya + "school/far/pol_fshy.png",
    )

    image polya shy school close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_polya + "school/close/pol_shy.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_polya + "school/close/pol_shy.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_polya + "school/close/pol_shy.png",
    )
    
    image polya surp school far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_polya + "school/far/pol_fsurp.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_polya + "school/far/pol_fsurp.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_polya + "school/far/pol_fsurp.png",
    )

    image polya surp school close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_polya + "school/close/pol_surp.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_polya + "school/close/pol_surp.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_polya + "school/close/pol_surp.png",
    )


    image polya angry school far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_polya + "school/far/pol_fangry.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_polya + "school/far/pol_fangry.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_polya + "school/far/pol_fangry.png",
    )

    image polya angry school close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_polya + "school/close/pol_angry.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_polya + "school/close/pol_angry.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_polya + "school/close/pol_angry.png",
    )

    image polya angryteers school far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_polya + "school/far/pol_fangryters.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_polya + "school/far/pol_fangryters.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_polya + "school/far/pol_fangryters.png",
    )

    image polya angryteers school close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_polya + "school/close/pol_angryters.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_polya + "school/close/pol_angryters.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_polya + "school/close/pol_angryters.png",
    )

    #СПРАЙТЫ НИКОЛАЯ
    image nikol serius school far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_nikol + "far/serius.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_nikol + "far/serius.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_nikol + "far/serius.png",
    )

    image nikol serius pioneer far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_nikol + "far/serius_pioneer.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_nikol + "far/serius_pioneer.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_nikol + "far/serius_pioneer.png",
    )

    image nikol smile school far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_nikol + "far/smile.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_nikol + "far/smile.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_nikol + "far/smile.png",
    )

    image nikol smile pioneer far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_nikol + "far/smile_pioneer.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_nikol + "far/smile_pioneer.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_nikol + "far/smile_pioneer.png",
    )

    image nikol angry school far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_nikol + "far/angry.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_nikol + "far/angry.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_nikol + "far/angry.png",
    )

    image nikol angry pioneer far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_nikol + "far/angry_pioneer.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_nikol + "far/angry_pioneer.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_nikol + "far/angry_pioneer.png",
    )

    image nikol normal school far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_nikol + "far/normal.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_nikol + "far/normal.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_nikol + "far/normal.png",
    )

    image nikol normal pioneer far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_nikol + "far/normal_pioneer.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_nikol + "far/normal_pioneer.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_nikol + "far/normal_pioneer.png",
    )

    image nikol normal school close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_nikol + "close/normal.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_nikol + "close/normal.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_nikol + "close/normal.png",
    )
    
    image nikol normal pioneer close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_nikol + "close/normal_pioneer.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_nikol + "close/normal_pioneer.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_nikol + "close/normal_pioneer.png",
    )

    image nikol angry pioneer close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_nikol + "close/angry_pioneer.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_nikol + "close/angry_pioneer.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_nikol + "close/angry_pioneer.png",
    )

    image nikol angry school close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_nikol + "close/angry.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_nikol + "close/angry.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_nikol + "close/angry.png",
    )


    image nikol serius pioneer close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_nikol + "close/serius_pioneer.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_nikol + "close/serius_pioneer.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_nikol + "close/serius_pioneer.png",
    )

    image nikol serius school close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_nikol + "close/serius.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_nikol + "close/serius.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_nikol + "close/serius.png",
    )

    image nikol smile pioneer close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_nikol + "close/smile_pioneer.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_nikol + "close/smile_pioneer.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_nikol + "close/smile_pioneer.png",
    )

    image nikol smile school close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(
            wks_sprites_nikol + "close/smile.png",
            im.matrix.tint(0.94, 0.82, 1.0)
        ),
        "persistent.sprite_time == 'night'", im.MatrixColor(
            wks_sprites_nikol + "close/smile.png",
            im.matrix.tint(0.63, 0.78, 0.82)
        ),
        True, wks_sprites_nikol + "close/smile.png",
    )