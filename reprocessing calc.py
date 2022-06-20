if __name__ == "__main__":
    print("=============== REPROCESSING CALCULATOR ===============\n")


def get_rig_type() -> int:
    """Function to get rig type."""

    print(
        """Step 1: Select Rig type:\n
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
            print("Invalid, please pick options 1,2,9 or 0:")
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
        print("\nStructure is unrigged, skipping security modifier...")

        return sec_mod
    else:
        print(
            """Step 2: Select Security Modifier:\n
            1. High-Security
            2. Low-Security
            3. Null-Security/W-Space
            """
        )
        while True:
            try:
                sec_type = int(input("Security Modifier:"))
            except ValueError:
                print("Invalid, input must be integer:")
                continue
            while sec_type not in range(0, 4):
                print("Invalid, please pick options 1-3:")
                sec_type = int(input("Security value:"))
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
        """Step 3: Select structure type:\n
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
        """Step 4: Select reprocessing skill level:
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
            rep_skill = int(input("Reprocessing Skill:"))
        except ValueError:
            print("Invalid, input must be integer:")
            continue
        while rep_skill not in range(0, 6):
            print("Invalid, please pick options 1-5 or 0:")
            rep_skill = int(input("Reprocessing Skill:"))
        else:
            rep_mod = rep_skill

        return rep_mod


def get_eff_skill() -> int:
    """Function to get efficiency skill level."""

    print(
        """Step 5: Select reprocessing efficiency skill level:
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
            eff_skill = int(input("Reprocessing Skill:"))
        except ValueError:
            print("Invalid, input must be integer:")
            continue
        while eff_skill not in range(0, 6):
            print("Invalid, please pick options 1-5 or 0:")
            eff_skill = int(input("Reprocessing Skill:"))
        else:
            eff_mod = eff_skill

        return eff_mod


def get_ore_skill() -> int:
    """Function to get specific ore skill level."""

    print(
        """Step 6: Select specific ore skill level:
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
            ore_skill = int(input("Specific Ore Skill:"))
        except ValueError:
            print("Invalid, input must be integer:")
            continue
        while ore_skill not in range(0, 6):
            print("Invalid, please pick options 1-5 or 0:")
            ore_skill = int(input("Specific Ore Skill:"))
        else:
            ore_mod = ore_skill

        return ore_mod


def get_imp_type() -> float:
    """Function to get implant type."""

    print(
        """Step 7: Select Implants:
    1. RX-801 Implant
    2. RX-802 Implant
    3. RX-804 Implant
    0. No Implants
    """
    )
    while True:
        try:
            imp_type = int(input("Implant Type:"))
        except ValueError:
            print("Invalid, input must be integer:")
            continue
        while imp_type not in range(0, 4):
            print("Invalid, please pick options 1-3 or 0:")
            imp_type = int(input("Implant Type:"))
        if imp_type == 1:
            imp_mod = 0.01
        elif imp_type == 2:
            imp_mod = 0.02
        elif imp_type == 3:
            imp_mod = 0.04
        else:
            imp_mod = 0.0

        return imp_mod


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


print(
    "You have selected options:\nRig Type:",
    RIGS,
    "\n" "Security Type:",
    SECU,
    "\n" "Structure Type:",
    STCT,
    "\n" "Reprocessing Skill:",
    REPR,
    "\n" "Efficiency Skill:",
    EFFI,
    "\n" "Specific Skill:",
    ORES,
    "\n" "Implant Type:",
    IMPL,
)

if SECU == 0.0:
    norm_unrig_yield = calc_repro_unrig_yield()
    yield_unrig_round = round(norm_unrig_yield, 1)
    print("\nApproximate Yield:", yield_unrig_round, "%, (Unrigged)")
else:
    norm_yield = calc_repro_yield()
    yield_round = round(norm_yield, 1)
    print("\nApproximate Yield:", yield_round, "%")
