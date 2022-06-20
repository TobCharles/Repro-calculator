import time

if __name__ == "__main__":
    print("=============== REPROCESSING CALCULATOR ===============\n")

# Returns the type of station where reprocessing will happen,
# and whether user has positive standings with station owners.


def get_dock_type() -> bool:
    """Function to get type of docking."""

    print(
        """Select dockup option:\n
        1. NPC Station
        2. Player Structure
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


def get_stds_level() -> float:
    """Function to get standings level."""

    print(
        """Do you have positive standings with NPC station?
        1. Yes
        2. No
        0. Unsure (calculation assumes no)
        """
    )

    while True:
        try:
            stds_type = int(input("Option:"))
        except ValueError:
            print("Invalid, input must be integer.")
            continue
        while stds_type not in range(0, 3):
            print("Invalid, please pick options 1, 2 or 0:")
            stds_type = int(input("Option:"))
        if stds_type == 1:
            stds_mod = 1.0
        else:
            stds_mod = 0.95

        return stds_mod


def get_stef_level() -> int:
    """Function to get station efficiency."""

    print(
        """Select NPC station efficiency:\n
        1. 25%
        2. 30%
        3. 32%
        4. 40%
        5. 45%
        6. 50%
        0. Unsure (calculation assumes efficiency 32%)"""
    )
    while True:
        try:
            stef_type = int(input("Station efficiency:"))
        except ValueError:
            print("Invalid, input must be integer:")
            continue
        while stef_type not in range(0, 7):
            print("Invalid, pick options 1-6 or 0:")
            stef_type = int(input("Station efficiency:"))
        if stef_type == 1:
            stef_mod = 25
        elif stef_type == 2:
            stef_mod = 30
        elif stef_type == 4:
            stef_mod = 40
        elif stef_type == 5:
            stef_mod = 45
        elif stef_type == 6:
            stef_mod = 50
        else:
            stef_mod = 32

        return stef_mod


# Returns parameters for structure reprocessing yield.
def get_rig_type() -> int:
    """Function to get rig type."""

    print(
        """Select structure rig type:\n
    1. Tech I Structure rig
    2. Tech II Structure rig
    9. No Structure rig
    0. Unsure (calculation assumes unrigged)
    """
    )
    while True:
        try:
            rig_type = int(input("Rig type:"))
        except ValueError:
            print("Invalid, input must be integer:")
            continue
        while rig_type not in [1, 2, 9, 0]:
            print("Invalid, pick options 1, 2, 9 or 0:")
            rig_type = int(input("Rig type:"))
        if rig_type == 1:
            rig_mod = 1
        elif rig_type == 2:
            rig_mod = 3
        else:
            rig_mod = 0

        return rig_mod


def get_sec_type(rig_val: int) -> float:
    """Function to get security modifier."""

    if rig_val == 0:
        sec_mod = 0.0
        print("\nNOTICE: Structure is unrigged, skipping security modifier...")
        time.sleep(1)

        return sec_mod
    else:
        print(
            """Select system security level:\n
            1. High-Security (0.5 - 1.0)
            2. Low-Security (0.1 - 0.4)
            3. Null-Security/W-Space (-1.0 - 0.0)
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
    9. Other structure types / Unsure
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


def get_rep_and_eff_skill() -> int:
    """Function to get reprocessing and efficiency skill level."""

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
                if eff_skill == 0:
                    rep_mod = 4
                    print("Reprocessing IV is prereq of Efficiency, adjusting...\n")
                    time.sleep(1)

                    eff_mod = eff_skill
                else:
                    eff_mod = eff_skill

                return eff_mod, rep_mod


def get_ore_skill() -> int:
    """Function to get specific ore skill level."""

    print(
        """Select specific ore skill level:\n(i.e. Simple/Varigated/Coherent Ore Reprocessing etc)
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


def get_impl_type() -> float:
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


# determines whether to calculate station or structure yield.
DOCK = get_dock_type()
if DOCK == True:
    STDS = get_stds_level()
    STEF = get_stef_level()
    EFFI, REPR = get_rep_and_eff_skill()
    ORES = get_ore_skill()
    IMPL = get_impl_type()
    RIGS = 0
    SECU = 0.0
    STCT = 0.0
    print("\nStation selecteed, ignoring structure calculation...\n")
    time.sleep(1)
else:
    RIGS = get_rig_type()
    SECU = get_sec_type(RIGS)
    STCT = get_strc_type()
    EFFI, REPR = get_rep_and_eff_skill()
    ORES = get_ore_skill()
    IMPL = get_impl_type()
    STDS = 0.0
    STEF = 0


# calculation formulae
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
        STEF
        * (1 + (0.03 * REPR))
        * (1 + (0.03 * EFFI))
        * (1 + (0.02 * ORES))
        * (1 + IMPL)
        * STDS
    )

    return stn_yield


print(
    "=== Your Selected Options ===\n",
    "Dockup option:",
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
    "\nSpecific Skill option:",
    ORES,
    "\nImplant option:",
    IMPL,
)
time.sleep(1)

if DOCK == False and SECU == 0.0:
    struct_unrig_yield = calc_repro_unrig_yield()
    struct_unrig_yield_round = round(struct_unrig_yield, 2)
    print("\nApproximate yield:", struct_unrig_yield_round, "% (unrigged structure)")
elif DOCK == False:
    struct_yield = calc_repro_yield()
    struct_yield_round = round(struct_yield, 2)
    print("\nApproximate yield:", struct_yield_round, "% (structure)")
elif DOCK == True and STDS == 0.95:
    statn_yield = calc_stn_repo_yield()
    statn_yield_round = round(statn_yield, 2)
    print("\nApproximate yield:", statn_yield_round, "% (neutral station)")
elif DOCK == True and STEF == 25:
    statn_yield = calc_stn_repo_yield()
    statn_yield_round = round(statn_yield, 2)
    print("\nApproximate yield:", statn_yield_round, "% (low-yield station)")
else:
    statn_yield = calc_stn_repo_yield()
    statn_yield_round = round(statn_yield, 2)
    print("\nApproximate yield:", statn_yield_round, "% (station)")


input()
