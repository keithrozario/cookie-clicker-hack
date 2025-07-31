import serialize


def test_serialize_run_details():
    run_details = {
        "start_date": 1753188318209,
        "full_date": 1753188318209,
        "last_date": 1753753952776,
        "bakery_name": "basiloaf",
        "seed": "lkzao",
        "customizer_save": "0,1,0,0,0,0,0",
    }
    run_details_str = serialize.serialize_run_details(run_details)
    assert (
        run_details_str
        == "1753188318209;1753188318209;1753753952776;basiloaf;lkzao;0,1,0,0,0,0,0"
    )


def test_serialize_prefs():
    prefs = {
        "particles": True,
        "numbers": True,
        "autosave": True,
        "autoupdate": True,
        "milk": True,
        "fancy": True,
        "warn": False,
        "cursors": True,
        "focus": True,
        "format": False,
        "notifs": False,
        "wobbly": True,
        "monospace": False,
        "filters": True,
        "cookiesound": True,
        "crates": False,
        "showBackupWarning": False,
        "extraButtons": True,
        "askLumps": False,
        "customGrandmas": True,
        "timeout": False,
        "cloudSave": True,
        "bgMusic": True,
        "notScary": False,
        "fullscreen": False,
        "screenreader": False,
        "discordPresence": True,
    }
    prefs_str_new = serialize.serialize_prefs(prefs)
    assert prefs_str_new == "111111011001011001010110001"


def test_serialize_stats():
    stats = {
        "cookies": 12401719440.323624,
        "cookies_earned": 16716604460.189524,
        "cookie_clicks": 12425,
        "golden_clicks": 9,
        "handmade_cookies": 65391637.07692009,
        "missed_golden_clicks": 99,
        "bg_type": 0,
        "milk_type": 0,
        "cookies_reset": 0.0,
        "elder_wrath": 0,
        "pledges": 0,
        "pledge_t": 0,
        "next_research": 0,
        "research_t": 0,
        "resets": 0,
        "golden_clicks_local": 9,
        "cookies_sucked": 0.0,
        "wrinklers_popped": 0,
        "santa_level": 0,
        "reindeer_clicked": 0,
        "season_t": 0,
        "season_uses": 0,
        "season": "",
        "wrinkler_amount": 0.0,
        "wrinkler_number": 0,
        "prestige": 0.0,
        "heavenly_chips": 0.0,
        "heavenly_chips_spent": 0.0,
        "heavenly_cookies": 0.0,
        "ascension_mode": 0,
        "permanent_upgrades": [-1, -1, -1, -1, -1],
        "dragon_level": 0,
        "dragon_aura": 0,
        "dragon_aura2": 0,
        "chime_type": 0,
        "volume": 75,
        "shiny_wrinkler_amount": 0.0,
        "shiny_wrinkler_number": 0,
        "lumps": 4.0,
        "lumps_total": 5.0,
        "lump_t": 1753703678952,
        "lump_refill": 0,
        "lump_current_type": 0,
        "vault": [],
        "heralds": 41,
        "fortune_gc": 0,
        "fortune_cps": 0,
        "cookies_ps_raw_highest": 793163.0812128433,
        "volume_music": 50,
        "cookies_sent": 0,
        "cookies_received": 0,
    }
    stats_str_new = serialize.serialize_stats(stats)
    assert (
        stats_str_new
        == "12401719440.323624;16716604460.189524;12425;9;65391637.07692009;99;0;0;0;0;0;0;0;0;0;9;0;0;0;0;0;0;;0;0;0;0;0;0;0;-1;-1;-1;-1;-1;0;0;0;0;75;0;0;4;5;1753703678952;0;0;;41;0;0;793163.0812128433;50;0;0;"
    )


def test_serialize_buildings():
    buildings = [
        {
            "amount": 100,
            "bought": 100,
            "total_cookies": 430576710.0,
            "level": 0,
            "minigame_save": "",
            "muted": 0,
            "highest": 100,
        },
        {
            "amount": 87,
            "bought": 88,
            "total_cookies": 552822555.0,
            "level": 0,
            "minigame_save": "",
            "muted": 0,
            "highest": 87,
        },
        {
            "amount": 72,
            "bought": 72,
            "total_cookies": 483112390.0,
            "level": 0,
            "minigame_save": "",
            "muted": 0,
            "highest": 72,
        },
        {
            "amount": 60,
            "bought": 60,
            "total_cookies": 956167862.0,
            "level": 0,
            "minigame_save": "",
            "muted": 0,
            "highest": 60,
        },
        {
            "amount": 47,
            "bought": 47,
            "total_cookies": 3410644218.0,
            "level": 1,
            "minigame_save": "",
            "muted": 0,
            "highest": 47,
        },
        {
            "amount": 31,
            "bought": 31,
            "total_cookies": 5319130692.0,
            "level": 0,
            "minigame_save": "",
            "muted": 0,
            "highest": 31,
        },
        {
            "amount": 13,
            "bought": 13,
            "total_cookies": 2682169515.0,
            "level": 0,
            "minigame_save": "",
            "muted": 0,
            "highest": 13,
        },
        {
            "amount": 3,
            "bought": 3,
            "total_cookies": 2797343576.0,
            "level": 0,
            "minigame_save": "",
            "muted": 0,
            "highest": 3,
        },
        {
            "amount": 0,
            "bought": 0,
            "total_cookies": 0.0,
            "level": 0,
            "minigame_save": "",
            "muted": 0,
            "highest": 0,
        },
        {
            "amount": 0,
            "bought": 0,
            "total_cookies": 0.0,
            "level": 0,
            "minigame_save": "",
            "muted": 0,
            "highest": 0,
        },
        {
            "amount": 0,
            "bought": 0,
            "total_cookies": 0.0,
            "level": 0,
            "minigame_save": "",
            "muted": 0,
            "highest": 0,
        },
        {
            "amount": 0,
            "bought": 0,
            "total_cookies": 0.0,
            "level": 0,
            "minigame_save": "",
            "muted": 0,
            "highest": 0,
        },
        {
            "amount": 0,
            "bought": 0,
            "total_cookies": 0.0,
            "level": 0,
            "minigame_save": "",
            "muted": 0,
            "highest": 0,
        },
        {
            "amount": 0,
            "bought": 0,
            "total_cookies": 0.0,
            "level": 0,
            "minigame_save": "",
            "muted": 0,
            "highest": 0,
        },
        {
            "amount": 0,
            "bought": 0,
            "total_cookies": 0.0,
            "level": 0,
            "minigame_save": "",
            "muted": 0,
            "highest": 0,
        },
        {
            "amount": 0,
            "bought": 0,
            "total_cookies": 0.0,
            "level": 0,
            "minigame_save": "",
            "muted": 0,
            "highest": 0,
        },
        {
            "amount": 0,
            "bought": 0,
            "total_cookies": 0.0,
            "level": 0,
            "minigame_save": "",
            "muted": 0,
            "highest": 0,
        },
        {
            "amount": 0,
            "bought": 0,
            "total_cookies": 0.0,
            "level": 0,
            "minigame_save": "",
            "muted": 0,
            "highest": 0,
        },
        {
            "amount": 0,
            "bought": 0,
            "total_cookies": 0.0,
            "level": 0,
            "minigame_save": "",
            "muted": 0,
            "highest": 0,
        },
        {
            "amount": 0,
            "bought": 0,
            "total_cookies": 0.0,
            "level": 0,
            "minigame_save": "",
            "muted": 0,
            "highest": 0,
        },
    ]
    buildings_str_new = serialize.serialize_buildings(buildings)
    assert (
        buildings_str_new
        == "100,100,430576710,0,,0,100;87,88,552822555,0,,0,87;72,72,483112390,0,,0,72;60,60,956167862,0,,0,60;47,47,3410644218,1,,0,47;31,31,5319130692,0,,0,31;13,13,2682169515,0,,0,13;3,3,2797343576,0,,0,3;0,0,0,0,,0,0;0,0,0,0,,0,0;0,0,0,0,,0,0;0,0,0,0,,0,0;0,0,0,0,,0,0;0,0,0,0,,0,0;0,0,0,0,,0,0;0,0,0,0,,0,0;0,0,0,0,,0,0;0,0,0,0,,0,0;0,0,0,0,,0,0;0,0,0,0,,0,0;"
    )


def test_serialize_upgrades():
    """
    Test upgrade variable is too long
    """
    pass


def test_serialize_achievements():
    """
    Test achievement variable is too long
    """
    pass


def test_serialize_buffs():
    """
    No Buffs to test
    """
    pass


def test_serialize_mod_data():
    """
    No Mod Data to test
    """
    pass


def test_gen_spl():
    pass
