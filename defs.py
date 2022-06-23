def get_repro_type() -> bool:
    """Function to get type of reprocessing."""

    print(
        """Select type of reprocessing:\n
        1. Ores
        2. Modules, Ships (scrapmetal)
        """
    )

    while True:
        try:
            repro_type = int(input("Reprocess type:"))
        except ValueError:
            print("Invalid, input must be integer:")
            continue
        while repro_type not in range(1, 3):
            print("Invalid, please pick options 1 or 2:")
            repro_type = int(input("Reprocessing type:"))
        if repro_type == 1:
            rtype_mod = True
        else:
            rtype_mod = False

        return rtype_mod


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
        """Do you have positive standings with NPC station?\n
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

        return sec_mod

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
        """Select reprocessing skill level:\n
    1. Reprocessing I
    2. Reprocessing II
    3. Reprocessing III
    4. Reprocessing IV
    5. Reprocessing V
    0. No Reprocessing skill\n
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
                """Select reprocessing efficiency skill level:\n
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
                if eff_skill in range(1, 6):
                    rep_mod = 4
                    print("Reprocessing IV is prereq of Efficiency, adjusting...\n")

                    eff_mod = eff_skill
                else:
                    eff_mod = eff_skill

                return rep_mod, eff_mod


def get_ore_type() -> int:

    print(
        """Select specific ore type:
        1. Simple Ores
        2. Coherent Ores
        3. Variegated Ores
        4. Abyssal, Complex, Mercoxit Ores, Ice & Moon Ores
        0. Not Applicable"""
    )

    while True:
        try:
            ore_type = int(input("Ore type:"))
        except ValueError:
            print("Invalid, input must be integer:")
            continue
        while ore_type not in range(0, 5):
            print("Invalid, please pick options 1-4 or 0:")
            ore_type = int(input("Ore type:"))
        else:
            type_mod = ore_type

            return type_mod


def get_ore_skill() -> int:
    """Function to get specific ore skill level."""

    print(
        """Select specific ore skill level:
    1. <Ore> Reprocessing I
    2. <Ore> Reprocessing II
    3. <Ore> Reprocessing III
    4. <Ore> Reprocessing IV
    5. <Ore> Reprocessing V
    0. No <Ore> Reprocessing skill\n
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


def get_scrap_skill() -> int:
    """Function to get scrapmetal reprocessing skill level."""

    print(
        """Select scrapmetal reprocessing skill level:
        1. Scrapmetal Reprocessing I
        2. Scrapmetal Reprocessing II
        3. Scrapmetal Reprocessing III
        4. Scrapmetal Reprocessing IV
        5. Scrapmetal Reprocessing V
        0. No Scrapmetal Reprocessing Skill
        """
    )

    while True:
        try:
            scrap_skill = int(input("Scrap skill:"))
        except ValueError:
            print("Invalid, input must be integer:")
            continue
        while scrap_skill not in range(0, 6):
            print("Invalid, pick options 1-5 or 0:")
            scrap_skill = int(input("Scrap skill:"))
        else:
            scrap_mod = scrap_skill

        return scrap_mod


def get_impl_type() -> float:
    """Function to get implant type."""

    print(
        """Select Implants:\n
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
