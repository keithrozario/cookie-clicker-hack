from helper_functions import format_number

def serialize_run_details(run_details: dict) -> str:
    run_details_list = [
        str(run_details["start_date"]),
        str(run_details["full_date"]),
        str(run_details["last_date"]),
        run_details["bakery_name"],
        run_details["seed"],
        run_details["customizer_save"],
    ]
    run_details_str = ";".join(run_details_list)

    return run_details_str


def serialize_prefs(prefs: dict) -> str:

    prefs_list = [
        str(int(prefs["particles"])),
        str(int(prefs["numbers"])),
        str(int(prefs["autosave"])),
        str(int(prefs["autoupdate"])),
        str(int(prefs["milk"])),
        str(int(prefs["fancy"])),
        str(int(prefs["warn"])),
        str(int(prefs["cursors"])),
        str(int(prefs["focus"])),
        str(int(prefs["format"])),
        str(int(prefs["notifs"])),
        str(int(prefs["wobbly"])),
        str(int(prefs["monospace"])),
        str(int(prefs["filters"])),
        str(int(prefs["cookiesound"])),
        str(int(prefs["crates"])),
        str(int(prefs["showBackupWarning"])),
        str(int(prefs["extraButtons"])),
        str(int(prefs["askLumps"])),
        str(int(prefs["customGrandmas"])),
        str(int(prefs["timeout"])),
        str(int(prefs["cloudSave"])),
        str(int(prefs["bgMusic"])),
        str(int(prefs["notScary"])),
        str(int(prefs["fullscreen"])),
        str(int(prefs["screenreader"])),
        str(int(prefs["discordPresence"])),
    ]
    prefs_str_new = "".join(prefs_list)
    return prefs_str_new


def serialize_stats(main_stats: dict) -> str:

    stats_list = [
        format_number(main_stats["cookies"]),
        format_number(main_stats["cookies_earned"]),
        str(main_stats["cookie_clicks"]),
        str(main_stats["golden_clicks"]),
        format_number(main_stats["handmade_cookies"]),
        str(main_stats["missed_golden_clicks"]),
        str(main_stats["bg_type"]),
        str(main_stats["milk_type"]),
        format_number(main_stats["cookies_reset"]),
        str(main_stats["elder_wrath"]),
        str(main_stats["pledges"]),
        str(main_stats["pledge_t"]),
        str(main_stats["next_research"]),
        str(main_stats["research_t"]),
        str(main_stats["resets"]),
        str(main_stats["golden_clicks_local"]),
        format_number(main_stats["cookies_sucked"]),
        str(main_stats["wrinklers_popped"]),
        str(main_stats["santa_level"]),
        str(main_stats["reindeer_clicked"]),
        str(main_stats["season_t"]),
        str(main_stats["season_uses"]),
        main_stats["season"],
        format_number(main_stats["wrinkler_amount"]),
        str(main_stats["wrinkler_number"]),
        format_number(main_stats["prestige"]),
        format_number(main_stats["heavenly_chips"]),
        format_number(main_stats["heavenly_chips_spent"]),
        format_number(main_stats["heavenly_cookies"]),
        str(main_stats["ascension_mode"]),
        str(";".join([str(i) for i in main_stats["permanent_upgrades"]])),
        str(main_stats["dragon_level"]),
        str(main_stats["dragon_aura"]),
        str(main_stats["dragon_aura2"]),
        str(main_stats["chime_type"]),
        str(main_stats["volume"]),
        format_number(main_stats["shiny_wrinkler_amount"]),
        str(main_stats["shiny_wrinkler_number"]),
        format_number(main_stats["lumps"]),
        format_number(main_stats["lumps_total"]),
        str(main_stats["lump_t"]),
        str(main_stats["lump_refill"]),
        str(main_stats["lump_current_type"]),
        ",".join(map(str, main_stats["vault"])),
        str(main_stats["heralds"]),
        str(main_stats["fortune_gc"]),
        str(main_stats["fortune_cps"]),
        format_number(main_stats["cookies_ps_raw_highest"]),
        str(main_stats["volume_music"]),
        str(main_stats["cookies_sent"]),
        str(main_stats["cookies_received"]),
    ]
    stats_str_new = ";".join(stats_list) + ";"
    return stats_str_new


def serialize_buildings(buildings: list) -> str:
    buildings_list = []
    for b in buildings:
        buildings_list.append(
            ",".join(
                [
                    str(b["amount"]),
                    str(b["bought"]),
                    format_number(b["total_cookies"]),
                    str(b["level"]),
                    b["minigame_save"],
                    str(b["muted"]),
                    str(b["highest"]),
                ]
            )
        )
    buildings_str_new = ";".join(buildings_list) + ";"

    return buildings_str_new


def serialize_upgrades(upgrades: dict) -> str:
    upgrades_list = []
    for i in sorted(upgrades.keys()):
        upgrades_list.append(str(upgrades[i]["unlocked"]))
        upgrades_list.append(str(upgrades[i]["bought"]))
    upgrades_str_new = "".join(upgrades_list)

    return upgrades_str_new


def serialize_achievements(achievements: dict) -> str:
    achievements_list = []
    for i in sorted(achievements.keys()):
        achievements_list.append(str(achievements[i]["won"]))
    achievements_str_new = "".join(achievements_list)
    return achievements_str_new


def serialize_buffs(buffs: list) -> str:
    buffs_list = []
    for b in buffs:
        buffs_list.append(
            ",".join(
                [
                    str(b["type_id"]),
                    format_number(b["time"]),
                    format_number(b["max_time"]),
                    format_number(b["arg1"]),
                    format_number(b["arg2"]),
                    format_number(b["arg3"]),
                ]
            )
        )
    buffs_str_new = ";".join(buffs_list)
    return buffs_str_new


def serialize_mod_data(mod_data: dict) -> str:
    mod_data_list = []
    for mod_id, mod_save_data in mod_data.items():
        mod_data_list.append(f"{mod_id}:{mod_save_data}")
    mod_data_str_new = ";".join(mod_data_list)

    return mod_data_str_new


def gen_new_spl(
    version: str,
    placeholder: str,
    prefs_str_new: str,
    stats_str_new: str,
    buildings_str_new: str,
    upgrades_str_new: str,
    achievements_str_new: str,
    buffs_str_new: str,
    mod_data_str_new: str,
    run_details_str: str,
) -> str:

    new_spl = [
        version,
        placeholder,  # Empty
        run_details_str,
        prefs_str_new,
        stats_str_new,
        buildings_str_new,
        upgrades_str_new,
        achievements_str_new,
        buffs_str_new,
        mod_data_str_new,
    ]

    final_string = "|".join(new_spl)

    return final_string

def serialize_parsed_data(parsed_data: dict):

    run_details_str = serialize_run_details(parsed_data["run_details"])
    prefs_str_new = serialize_prefs(parsed_data["prefs"])
    stats_str_new = serialize_stats(parsed_data["main_stats"])
    buildings_str_new = serialize_buildings(parsed_data["buildings"])
    upgrades_str_new = serialize_upgrades(parsed_data["upgrades"])
    achievements_str_new = serialize_achievements(parsed_data["achievements"])
    buffs_str_new = serialize_buffs(parsed_data["buffs"])
    mod_data_str_new = serialize_mod_data(parsed_data["mod_data"])
    serialized_string = gen_new_spl(
        parsed_data["version"],
        parsed_data["placeholder"],
        prefs_str_new,
        stats_str_new,
        buildings_str_new,
        upgrades_str_new,
        achievements_str_new,
        buffs_str_new,
        mod_data_str_new,
        run_details_str,
    )

    return serialized_string