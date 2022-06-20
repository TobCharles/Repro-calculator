if __name__ == "__main__":
    print("=============== REPROCESSING CALCULATOR ===============\n")


def get_dock_type() -> bool:
    """Function to get type of docking."""

    print(
        """Select dockup option:\n
        1. NPC Station
        2. Structure
        """
    )

    while True:
        try:
            dock_type = int(input("Dockup option:"))
        except ValueError:
            print("Invalid, input must be integer:")
            continue
        while dock_type not in range(1, 3):
            print("Invalid, please pick options 1 or 2:")
            dock_type = int(input("Dockup option:"))
        if dock_type == 1:
            dock_mod = True
        else:
            dock_mod = False

        return dock_mod


def get_standing_level() -> float:
    """Function to get standings level."""

    print(
        """Do you have positive standings with station owners?
        1. Yes
        2. No
        """
    )

    while True:
        try:
            stnd_level = int(input("Option:"))
        except ValueError:
            print("Invalid, input must be integer.")
            continue
        while stnd_level not in range(1, 3):
            print("Invalid, please pick options 1 or 2:")
            stnd_level = int(input("Option:"))
        if stnd_level == 1:
            stnd_mod = 1.0
        else:
            stnd_mod = 0.95

        return stnd_mod


def get_rig_type() -> int:
    """Function to get rig type."""

    print(
        """Select structure rig type:\n
    1. Tech I Structure rig
    2. Tech II Structure rig
    9. Unsure (calculation assumes unrigged)
    0. No Structure rig
    """
    )
    while True:
        try:
            rig_type = int(input("Rig type:"))
        except ValueError:
            print("Invalid, input must be integer:")
            continue
        while rig_type not in [1, 2, 9, 0]:
            print("Invalid, please pick options 1, 2, 9 or 0:")
            rig_type = int(input("Rig type:"))
        if rig_type == 1:
            rig_mod = 1
        elif rig_type == 2:
            rig_mod = 3
        else:
            rig_mod = 0

        return rig_mod


def get_sec_type(rig_mod: int) -> float:
    """Function to get security modifier."""

    if rig_mod == 0:
        sec_mod = 0.0
        print("\nNOTICE: Structure is unrigged, skipping security modifier...")

        return sec_mod
    else:
        print(
            """Select system security level:\n
            1. High-Security
            2. Low-Security
            3. Null-Security/W-Space
            """
        )
        while True:
            try:
                sec_type = int(input("Security level:"))
            except ValueError:
                print("Invalid, input must be integer:")
                continue
            while sec_type not in range(0, 4):
                print("Invalid, please pick options 1-3:")
                sec_type = int(input("Security level:"))
            if sec_type == 2:
                sec_mod = 0.06
            elif sec_type == 3:
                sec_mod = 0.12
            else:
                sec_mod = 0.0

            return sec_mod


def get_strc_type() -> float:
    """Function to get structure type."""

    print(
        """Select structure type:\n
    1. Athanor structure
    2. Tatara structure
    9. Other structure types
    """
    )
    while True:
        try:
            strc_type = int(input("Structure type:"))
        except ValueError:
            print("Invalid, input must be integer:")
            continue
        while strc_type not in [1, 2, 9]:
            print("Invalid, please pick options 1,2 or 9:")
            strc_type = int(input("Structure type:"))
        if strc_type == 1:
            strc_mod = 0.02
        elif strc_type == 2:
            strc_mod = 0.055
        else:
            strc_mod = 0.0

        return strc_mod


def get_rep_skill() -> int:
    """Function to get reprocessing skill level."""

    print(
        """Select reprocessing skill level:
    1. Reprocessing I
    2. Reprocessing II
    3. Reprocessing III
    4. Reprocessing IV
    5. Reprocessing V
    0. No Reprocessing skill
    """
    )
    while True:
        try:
            rep_skill = int(input("Reprocessing skill:"))
        except ValueError:
            print("Invalid, input must be integer:")
            continue
        while rep_skill not in range(0, 6):
            print("Invalid, please pick options 1-5 or 0:")
            rep_skill = int(input("Reprocessing skill:"))
        else:
            rep_mod = rep_skill

        return rep_mod


def get_eff_skill() -> int:
    """Function to get efficiency skill level."""

    print(
        """Select reprocessing efficiency skill level:
    1. Reprocessing Efficiency I
    2. Reprocessing Efficiency II
    3. Reprocessing Efficiency III
    4. Reprocessing Efficiency IV
    5. Reprocessing Efficiency V
    0. No Reprocessing Efficiency skill
    """
    )
    while True:
        try:
            eff_skill = int(input("Efficiency skill:"))
        except ValueError:
            print("Invalid, input must be integer:")
            continue
        while eff_skill not in range(0, 6):
            print("Invalid, please pick options 1-5 or 0:")
            eff_skill = int(input("Efficiency skill:"))
        else:
            eff_mod = eff_skill

        return eff_mod


def get_ore_skill() -> int:
    """Function to get specific ore skill level."""

    print(
        """Select specific ore skill level:
    1. <Ore> Reprocessing I
    2. <Ore> Reprocessing II
    3. <Ore> Reprocessing III
    4. <Ore> Reprocessing IV
    5. <Ore> Reprocessing V
    0. No <Ore> Reprocessing skill
    """
    )
    while True:
        try:
            ore_skill = int(input("Specific skill:"))
        except ValueError:
            print("Invalid, input must be integer:")
            continue
        while ore_skill not in range(0, 6):
            print("Invalid, please pick options 1-5 or 0:")
            ore_skill = int(input("Specific skill:"))
        else:
            ore_mod = ore_skill

        return ore_mod


def get_imp_type() -> float:
    """Function to get implant type."""

    print(
        """Select Implants:
    1. RX-801 Implant
    2. RX-802 Implant
    3. RX-804 Implant
    0. No Implants
    """
    )
    while True:
        try:
            imp_type = int(input("Implant type:"))
        except ValueError:
            print("Invalid, input must be integer:")
            continue
        while imp_type not in range(0, 4):
            print("Invalid, please pick options 1-3 or 0:")
            imp_type = int(input("Implant type:"))
        if imp_type == 1:
            imp_mod = 0.01
        elif imp_type == 2:
            imp_mod = 0.02
        elif imp_type == 3:
            imp_mod = 0.04
        else:
            imp_mod = 0.0

        return imp_mod


STNT = get_dock_type()
if STNT == True:
    STND = get_standing_level()
    REPR = get_rep_skill()
    EFFI = get_eff_skill()
    ORES = get_ore_skill()
    IMPL = get_imp_type()
    RIGS = 0
    SECU = 0.0
    STCT = 0.0
    print("Station selecteed, ignoring structure calculation...")
else:
    RIGS = get_rig_type()
    SECU = get_sec_type(RIGS)
    STCT = get_strc_type()
    REPR = get_rep_skill()
    EFFI = get_eff_skill()
    ORES = get_ore_skill()
    IMPL = get_imp_type()


def calc_repro_yield():
    """Calculates standard yield."""

    repro_yield = (
        ((50 + RIGS) * (1 + SECU))
        * (1 + STCT)
        * (1 + (0.03 * REPR))
        * (1 + (0.03 * EFFI))
        * (1 + (0.02 * ORES))
        * (1 + IMPL)
    )

    return repro_yield


def calc_repro_unrig_yield():
    """Calculates unrigged yield."""

    repro_unrig_yield = (
        (50 + RIGS)
        * (1 + STCT)
        * (1 + (0.03 * REPR))
        * (1 + (0.03 * EFFI))
        * (1 + (0.02 * ORES))
        * (1 + IMPL)
    )

    return repro_unrig_yield


def calc_stn_repo_yield():
    """Calculates station yield."""

    stn_yield = (
        50
        * (1 + (0.03 * REPR))
        * (1 + (0.03 * EFFI))
        * (1 + (0.02 * ORES))
        * (1 + IMPL)
        * STND
    )

    return stn_yield


if SECU == 0.0 and STNT == False:
    norm_unrig_yield = calc_repro_unrig_yield()
    yield_unrig_round = round(norm_unrig_yield, 2)
    print("\nApproximate Yield:", yield_unrig_round, "%, (Unrigged)")
elif STNT == False:
    norm_yield = calc_repro_yield()
    yield_round = round(norm_yield, 1)
    print("\nApproximate Yield:", yield_round, "%, (structure)")
elif STND == 0.95:
    norm_stn_yield = calc_stn_repo_yield()
    norm_stn_yield_round = round(norm_stn_yield, 2)
    print("\nApproximate Yield:", norm_stn_yield_round, "% (station, neutral)")
else:
    norm_stn_yield = calc_stn_repo_yield()
    norm_stn_yield_round = round(norm_stn_yield, 2)
    print("\nApproximate Yield:", norm_stn_yield_round, "% (station)")
