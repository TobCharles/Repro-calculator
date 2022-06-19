"""
TODO: File DocString. Fill this in with a description of what this file is/does.

"""
# CHANGES:
# No need to use time.sleep -> No need for time
# AVOID single letter variables.


def command_line_calculator():
    rig_type = input("please select a rig type:")
    while rig_type not in ["1", "2", "9", "0"]:
        rig_type = input("Invalid, please pick options 1,2,9 or 0:")
    if rig_type == "1":
        # a 1 or 2 without anything else around them is assumed to be an integer
        rig_mod = 1
    elif rig_type == "2":
        rig_mod = 3
    else:
        rig_mod = 0
    print("Selected option:", rig_type)

    print(
        """Step 2: Select security modifier:\n
    1. High-Security
    2. Low-Security
    3. Null-Security/W-Space
    """
    )
    if rig_type in ("9", "0"):
        sec_mod = 0
        print("\nNOTICE: Structure is unrigged, skipping security modifier...\n")

    else:
        sec_type = input("please select a security type:")
        while sec_type not in ["1", "2", "3"]:
            sec_type = input("Invalid, please pick options 1-3:")
        if sec_type == "2":
            # Anything with a decimal place is assumed to be a floating-point number
            sec_mod = 0.06
        elif sec_type == "3":
            sec_mod = 0.12
        else:
            sec_mod = 0
        print("Selected option:", sec_type)

    print(
        """Step 3: Select structure type:\n
    1. Athanor structure
    2. Tatara structure
    9. Other structure types
    """
    )

    strc_type = input("please select a structure type:")
    while strc_type not in ["1", "2", "9"]:
        strc_type = input("Invalid, please pick options 1-2 or 9:")
    if strc_type == "1":
        strc_mod = 0.02
    elif strc_type == "2":
        strc_mod = 0.055
    else:
        strc_mod = 0

    print("Selected option:", strc_type)

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

    rep_skill = int(input("please select your reprocessing skill:"))
    while rep_skill not in range(0, 6):
        rep_skill = int(input("Invalid, please pick options 1-5 or 0:"))
    else:
        repr_mod = rep_skill

    print("Selected option:", rep_skill)

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

    eff_skill = int(input("please select your reprocessing efficiency skill:"))
    while eff_skill not in range(0, 6):
        eff_skill = int(input("Invalid, please pick options 1-5 or 0:"))

    print("Selected option:", eff_skill)

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

    ore_skill = int(input("please select your specific ore skill:"))
    while ore_skill not in range(0, 6):
        ore_skill = int(input("Invalid, please pick options 1-5 or 0:"))
    else:
        ore_skill = ore_skill

    print("Selected option:", ore_skill)

    print(
        """Step 7: Select Implants:
    1. RX-801 Implant
    2. RX-802 Implant
    3. RX-804 Implant
    0. No Implants"""
    )

    implants = input("please select implants:")
    while implants not in ["1", "2", "3", "0"]:
        implants = input("Invalid, please pick options 1-3 or 0:")
    if implants == "1":
        implant_mod = 0.01
    elif implants == "2":
        implant_mod = 0.02
    elif implants == "3":
        implant_mod = 0.04
    else:
        implant_mod = 0

    print("Selected option:", implants)

    print(
        "You have selected options:\nRig Option:",
        rig_mod,
        "\n" "Security Option:",
        sec_mod,
        "\n" "Structure Option:",
        strc_mod,
        "\n" "Reprocessing Skill:",
        repr_mod,
        "\n" "Efficiency Skill:",
        eff_skill,
        "\n" "Specific Skill:",
        ore_skill,
        "\n" "Implant Option:",
        implant_mod,
        "\n" ".....Calculating.....",
    )

    # These will automatically be floats, as they are calculated using floats
    repo_yield = (
        ((50 + rig_mod) * (1 + sec_mod))
        * (1 + strc_mod)
        * (1 + (0.03 * repr_mod))
        * (1 + (0.03 * eff_skill))
        * (1 + (0.02 * ore_skill))
        * (1 + implant_mod)
    )
    repo_unrig = (
        (50 + rig_mod)
        * (1 + strc_mod)
        * (1 + (0.03 * repr_mod))
        * (1 + (0.03 * eff_skill))
        * (1 + (0.02 * ore_skill))
        * (1 + implant_mod)
    )
    yield_round = round(repo_yield, 1)
    unrig_round = round(repo_unrig, 1)

    if rig_type in ("9", "0"):
        print(
            "Your reprocessing yield is roughly:",
            unrig_round,
            "%",
            "\nNOTE: structure is unrigged",
        )
    else:
        print("Your reprocessing yield is roughly:", yield_round, "%")


if __name__ == "__main__":
    # Put "main-line" code to be executed when the file is run here, so that this
    # file can be included in larger projects easily
    print("=============== REPROCESSING CALCULATOR ===============\n")
    command_line_calculator()
