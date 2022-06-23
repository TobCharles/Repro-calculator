from defs import *

if __name__ == "__main__":
    print("=============== REPROCESSING CALCULATOR ===============\n")


# Determines whether to calculate station or structure yield,
# and what properties to include in calculations.
RTPE = get_repro_type()
if RTPE is True:
    DOCK = get_dock_type()
    SCRP = 0
    if DOCK is True:
        STDS = get_stds_level()
        STEF = get_stef_level()
        OTPE = get_ore_type()
        if OTPE == 1:
            REPR = int(4)
        elif OTPE == 2:
            REPR = 5
        elif OTPE == 3:
            REPR = 5
            EFFI = int(4)
        elif OTPE == 4:
            REPR = 5
            EFFI = 5
        else:
            REPR, EFFI = get_rep_and_eff_skill()
            ORES = get_ore_skill()
            IMPL = get_impl_type()
            RIGS = int(0)
            SECU, STCT = (0.0, 0.0)
            print(
                "\nStation selecteed, ignoring structure calculation..."
                "Reprocessing type: ores, adjusting calculations...\n"
            )
    else:
        RIGS = get_rig_type()
        SECU = get_sec_type(RIGS)
        STCT = get_strc_type()
        OTPE = get_ore_type()
        if OTPE == 1:
            REPR = int(4)
        elif OTPE == 2:
            REPR = 5
        elif OTPE == 3:
            REPR = 5
            EFFI = int(4)
        elif OTPE == 4:
            REPR = 5
            EFFI = 5
        else:
            REPR, EFFI = get_rep_and_eff_skill()
        ORES = get_ore_skill()
        IMPL = get_impl_type()
        STDS, STEF = (0.0, 0.0)
else:
    DOCK = get_dock_type()
    if DOCK is True:
        STDS = get_stds_level()
        STEF = get_stef_level()
        SCRP = get_scrap_skill()
        IMPL = get_impl_type()
        REPR, EFFI, OTPE, ORES, RIGS, SECU, STCT = int(0, 0, 0, 0, 0, 0, 0)
    else:
        RIGS = get_rig_type()
        SECU = get_sec_type(RIGS)
        STCT = get_strc_type()
        SCRP = get_scrap_skill()
        IMPL = get_impl_type()
        REPR, EFFI, OTPE, ORES = int(0, 0, 0, 0)


# Calculation formulae.
def calc_ore_strct_yield():
    """Calculates standard yield."""

    return (
        ((50 + RIGS) * (1 + SECU))
        * (1 + STCT)
        * (1 + (0.03 * REPR))
        * (1 + (0.03 * EFFI))
        * (1 + (0.02 * ORES))
        * (1 + IMPL)
    )


def calc_ore_unrig_yield():
    """Calculates unrigged yield."""

    return (
        (50 + RIGS)
        * (1 + STCT)
        * (1 + (0.03 * REPR))
        * (1 + (0.03 * EFFI))
        * (1 + (0.02 * ORES))
        * (1 + IMPL)
    )


def calc_ore_statn_yield():
    """Calculates station yield."""

    return (
        STEF
        * (1 + (0.03 * REPR))
        * (1 + (0.03 * EFFI))
        * (1 + (0.02 * ORES))
        * (1 + IMPL)
        * STDS
    )


def calc_scrap_strct_yield():
    """Calculates scrapmetal yield in structures."""

    return ((50 + RIGS) * (1 + SECU)) * (1 + STCT) * (1 + (0.02 * SCRP)) * (1 + IMPL)


def calc_scrap_unrig_yield():
    """Calculates scrapmetal yield in unrigged structures."""

    return (50 + RIGS) * (1 + STCT) * (1 + (0.02 * SCRP)) * (1 + IMPL)


def calc_scrap_statn_yield():
    """Calculates scrapmetal yield in station."""

    return STEF * (1 + (0.02 * SCRP)) * (1 + IMPL) * STDS


# Prints out user selected options from above functions.
print(
    "=== Your Selected Options ===\n",
    "Reprocessing type:",
    RTPE,
    "\nDockup option:",
    DOCK,
    "\nStanding option:",
    STDS,
    "\nStation Efficiency option:",
    STEF,
    "\nRig option:",
    RIGS,
    "\nStructure option:",
    STCT,
    "\nEfficiency Skill option:",
    EFFI,
    "\nReprocessing Skill option:",
    REPR,
    "\nOre Type option:",
    OTPE,
    "\nSpecific Skill option:",
    ORES,
    "\nScrapmetal Skill option:",
    SCRP,
    "\nImplant option:",
    IMPL,
)


# selects what type of yield to display and any notices about calculations.
if RTPE is False:
    if DOCK is False and SECU == 0.0:
        scrap_unrig = round(calc_scrap_unrig_yield(), 2)
        print(
            "\nApprox yield:",
            scrap_unrig,
            "% (scrap / unrigged structure)\n",
        )
    elif DOCK is False:
        scrap_strct = round(calc_scrap_strct_yield(), 2)
        print("\nApprox yield:", scrap_strct, "% (structure)\n")
    elif STDS == 0.95:
        scrap_statn = round(calc_scrap_statn_yield(), 2)
        print("\nApprox yield:", scrap_statn, "% (neutral station)\n")
    elif STEF in [25, 30, 32]:
        scrap_statn = round(calc_scrap_statn_yield(), 2)
        print("\nApprox yield:", scrap_statn, "% (low-yield station)\n")
    else:
        scrap_statn = round(calc_scrap_statn_yield(), 2)
        print("\nApprox yield:", scrap_statn, "% (station)\n")
elif EFFI or REPR not in [5]:
    if DOCK is False and SECU == 0.0:
        ore_unrig = round(calc_ore_unrig_yield(), 2)
        print(
            "\nApprox yield:",
            ore_unrig,
            "% (scrapmetal / unrigged structure)\n"
            "NOTE: Confirm skill prereqs for specific ores are met.\n"
            "Yield calculation may be inaccurate otherwise.",
        )
    elif DOCK is False:
        ore_strct = round(calc_ore_strct_yield(), 2)
        print(
            "\nApprox yield:",
            ore_strct,
            "% (structure)\n"
            "NOTE: Confirm skill prereqs for specific ores are met.\n"
            "Yield calculation may be inaccurate otherwise.",
        )
    elif STDS == 0.95:
        ore_statn = round(calc_ore_statn_yield(), 2)
        print(
            "\nApprox yield:",
            ore_statn,
            "% (neutral station)\n"
            "NOTE: Confirm skill prereqs for specific ores are met.\n"
            "Yield calculation may be inaccurate otherwise.",
        )
    elif STEF in [25, 30, 32]:
        ore_statn = round(calc_ore_statn_yield(), 2)
        print(
            "\nApprox yield:",
            ore_statn,
            "% (low-yield station)\n"
            "NOTE: Confirm skill prereqs for specific ores are met.\n"
            "Yield calculation may be inaccurate otherwise.",
        )
    else:
        ore_statn = round(calc_ore_statn_yield(), 2)
        print(
            "\nApprox yield:",
            ore_statn,
            "% (station)\n"
            "NOTE: Confirm skill prereqs for specific ores are met.\n"
            "Yield calculation may be inaccurate otherwise.",
        )
else:
    if DOCK is False and SECU == 0.0:
        ore_unrig = round(calc_ore_unrig_yield(), 2)
        print(
            "\nApprox yield:",
            ore_unrig,
            "% (scrapmetal / unrigged structure)\n",
        )
    elif DOCK is False:
        ore_strct = round(calc_ore_strct_yield(), 2)
        print("\nApprox yield:", ore_strct, "% (structure)\n")
    elif STDS == 0.95:
        ore_statn = round(calc_ore_statn_yield(), 2)
        print("\nApprox yield:", ore_statn, "% (neutral station)\n")
    elif STEF in [25, 30, 32]:
        ore_statn = round(calc_ore_statn_yield(), 2)
        print("\nApprox yield:", ore_statn, "% (low-yield station)\n")
    else:
        ore_statn = round(calc_ore_statn_yield(), 2)
        print("\nApprox yield:", ore_statn, "% (station)\n")

input()
