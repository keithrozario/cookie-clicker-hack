def parse(spl):
    # Section 2: Run Details
    run_details_raw = spl[2]
    run_details_parts = run_details_raw.split(";")
    run_details = {
        "start_date": int(run_details_parts[0]),
        "full_date": int(run_details_parts[1]),
        "last_date": int(run_details_parts[2]),
        "bakery_name": run_details_parts[3],
        "seed": run_details_parts[4],
        "customizer_save": run_details_parts[5],
    }

    # Section 3: Preferences
    prefs_str = spl[3]
    prefs = {
        "particles": bool(int(prefs_str[0])),
        "numbers": bool(int(prefs_str[1])),
        "autosave": bool(int(prefs_str[2])),
        "autoupdate": bool(int(prefs_str[3])),
        "milk": bool(int(prefs_str[4])),
        "fancy": bool(int(prefs_str[5])),
        "warn": bool(int(prefs_str[6])),
        "cursors": bool(int(prefs_str[7])),
        "focus": bool(int(prefs_str[8])),
        "format": bool(int(prefs_str[9])),
        "notifs": bool(int(prefs_str[10])),
        "wobbly": bool(int(prefs_str[11])),
        "monospace": bool(int(prefs_str[12])),
        "filters": bool(int(prefs_str[13])),
        "cookiesound": bool(int(prefs_str[14])),
        "crates": bool(int(prefs_str[15])),
        "showBackupWarning": bool(int(prefs_str[16])),
        "extraButtons": bool(int(prefs_str[17])),
        "askLumps": bool(int(prefs_str[18])),
        "customGrandmas": bool(int(prefs_str[19])),
        "timeout": bool(int(prefs_str[20])),
        "cloudSave": bool(int(prefs_str[21])),
        "bgMusic": bool(int(prefs_str[22])),
        "notScary": bool(int(prefs_str[23])),
        "fullscreen": bool(int(prefs_str[24])),
        "screenreader": bool(int(prefs_str[25])),
        "discordPresence": bool(int(prefs_str[26])),
    }

    # Section 4: Main Game Stats
    stats_raw = spl[4].split(";")
    main_stats = {
        "cookies": float(stats_raw[0]),
        "cookies_earned": float(stats_raw[1]),
        "cookie_clicks": int(stats_raw[2]),
        "golden_clicks": int(stats_raw[3]),
        "handmade_cookies": float(stats_raw[4]),
        "missed_golden_clicks": int(stats_raw[5]),
        "bg_type": int(stats_raw[6]),
        "milk_type": int(stats_raw[7]),
        "cookies_reset": float(stats_raw[8]),
        "elder_wrath": int(stats_raw[9]),
        "pledges": int(stats_raw[10]),
        "pledge_t": int(stats_raw[11]),
        "next_research": int(stats_raw[12]),
        "research_t": int(stats_raw[13]),
        "resets": int(stats_raw[14]),
        "golden_clicks_local": int(stats_raw[15]),
        "cookies_sucked": float(stats_raw[16]),
        "wrinklers_popped": int(stats_raw[17]),
        "santa_level": int(stats_raw[18]),
        "reindeer_clicked": int(stats_raw[19]),
        "season_t": int(stats_raw[20]),
        "season_uses": int(stats_raw[21]),
        "season": stats_raw[22],
        "wrinkler_amount": float(stats_raw[23]),
        "wrinkler_number": int(stats_raw[24]),
        "prestige": float(stats_raw[25]),
        "heavenly_chips": float(stats_raw[26]),
        "heavenly_chips_spent": float(stats_raw[27]),
        "heavenly_cookies": float(stats_raw[28]),
        "ascension_mode": int(stats_raw[29]),
        "permanent_upgrades": [
            int(stats_raw[30]),
            int(stats_raw[31]),
            int(stats_raw[32]),
            int(stats_raw[33]),
            int(stats_raw[34]),
        ],
        "dragon_level": int(stats_raw[35]),
        "dragon_aura": int(stats_raw[36]),
        "dragon_aura2": int(stats_raw[37]),
        "chime_type": int(stats_raw[38]),
        "volume": int(stats_raw[39]),
        "shiny_wrinkler_amount": float(stats_raw[40]),
        "shiny_wrinkler_number": int(stats_raw[41]),
        "lumps": float(stats_raw[42]),
        "lumps_total": float(stats_raw[43]),
        "lump_t": int(stats_raw[44]),
        "lump_refill": int(stats_raw[45]),
        "lump_current_type": int(stats_raw[46]),
        "vault": [int(x) for x in stats_raw[47].split(",") if x],
        "heralds": int(stats_raw[48]),
        "fortune_gc": int(stats_raw[49]),
        "fortune_cps": int(stats_raw[50]),
        "cookies_ps_raw_highest": float(stats_raw[51]),
        "volume_music": int(stats_raw[52]),
        "cookies_sent": int(stats_raw[53]),
        "cookies_received": int(stats_raw[54]),
    }

    # Section 5: Buildings
    buildings_raw = spl[5].split(";")
    buildings = []
    for building_str in buildings_raw:
        if not building_str:
            continue
        parts = building_str.split(",")
        buildings.append(
            {
                "amount": int(parts[0]),
                "bought": int(parts[1]),
                "total_cookies": float(parts[2]),
                "level": int(parts[3]),
                "minigame_save": parts[4],
                "muted": int(parts[5]),
                "highest": int(parts[6] or parts[0]),
            }
        )

    # Section 6: Upgrades
    upgrades_str = spl[6]
    upgrades = {}
    for i in range(0, len(upgrades_str), 2):
        upgrades[i // 2] = {
            "unlocked": int(upgrades_str[i]),
            "bought": int(upgrades_str[i + 1]),
        }

    # Section 7: Achievements
    achievements_str = spl[7]
    achievements = {}
    for i in range(len(achievements_str)):
        achievements[i] = {"won": int(achievements_str[i])}

    # Section 8: Buffs
    buffs_raw = spl[8].split(";")
    buffs = []
    for buff_str in buffs_raw:
        if not buff_str:
            continue
        parts = buff_str.split(",")
        buffs.append(
            {
                "type_id": int(parts[0]),
                "time": float(parts[1]),
                "max_time": float(parts[2]),
                "arg1": float(parts[3] or 0),
                "arg2": float(parts[4] or 0),
                "arg3": float(parts[5] or 0),
            }
        )

    # Section 9: Mod Data
    mod_data_raw = spl[9].split(";")
    mod_data = {}
    for mod_str in mod_data_raw:
        if not mod_str:
            continue
        parts = mod_str.split(":")
        mod_id = parts[0]
        mod_save_data = ":".join(parts[1:])
        mod_data[mod_id] = mod_save_data

    return {
        "run_details": run_details,
        "prefs": prefs,
        "main_stats": main_stats,
        "buildings": buildings,
        "upgrades": upgrades,
        "achievements": achievements,
        "buffs": buffs,
        "mod_data": mod_data,
        "run_details_raw": run_details_raw,
    }
