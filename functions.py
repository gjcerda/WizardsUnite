def levelFoe(Enemy):
    chambers = [i for i in range(1,21)]
    levels = [3, 8, 18, 29, 38, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 187]
    return levels[Enemy.chamber - 1]

def stats_multiplier(Enemy):
    return 1 + 0.0816 * Enemy.level

class Foe:
    base_stats_erkling = {"stamina": [76, 93, 107, 124, 139], "power": [7, 8, 10, 11, 13],
    "elite stamina": [141, 173, 200, 231, 258], "elite power": [13, 16, 18, 21, 24],
    "defense": [0, 0, 0, 0, 0], "defense breach": [0, 0, 0, 0, 0], "dodge": [0, 0.05, 0.25, 0.4, 0.6]}
    base_stats_acromantula = {"stamina": [72, 91, 109, 136, 166], "power": [8, 10, 13, 17, 22],
    "elite stamina": [135, 170, 203, 254, 310], "elite power": [16, 19, 24, 32, 41],
    "defense": [0, 0, 0, 0, 0], "defense breach": [0, 0, 0, 0, 0], "dodge": [0, 0, 0, 0, 0]}
    base_stats_dark_wizard = {"stamina:": [62, 76, 88, 101, 113], "power": [7, 9, 11, 12, 14],
    "elite stamina": [115, 141, 163, 189, 211], "elite power": [14, 18, 20, 24, 26],
    "defense": [0, 0.05,0.15, 0.3, 0.5], "defense breach": [0, 0, 0.1, 0.2, 0.4], "dodge": [0, 0, 0, 0, 0]}
    base_stats_death_eater = {"stamina": [83, 101, 122, 147, 177], "power": [6, 7, 9, 10, 11],
    "elite stamina": [154, 189, 227, 273, 328], "elite power": [12, 14, 17, 19, 22],
    "defense": [0, 0, 0, 0, 0], "defense breach": [0, 0, 0, 0, 0], "dodge": [0, 0, 0, 0, 0]}
    base_stats_pixie = {"stamina": [41, 50, 58, 67, 75], "power": [7, 9, 11, 14, 18],
    "elite stamina": [77, 94, 109, 126, 140], "elite power": [13, 17, 21, 27, 34],
    "defense": [0, 0, 0, 0, 0], "defense breach": [0, 0, 0, 0, 0], "dodge": [0, 0.05, 0.25, 0.4, 0.6]}
    base_stats_werewolf = {"stamina": [70, 88, 109, 133, 159], "power": [7 ,9 ,11, 13, 16],
    "elite stamina": [131, 163, 203, 247, 296], "elite power": [13, 17, 21, 25, 30],
    "defense": [0, 0.05, 0.25, 0.4, 0.6], "defense breach": [0, 0, 0, 0.1, 0.3], "dodge": [0, 0, 0, 0, 0]}
    base_stats = {"Erkling": base_stats_erkling, "Acromantula": base_stats_acromantula, "Dark Wizard": base_stats_dark_wizard,
    "Death Eater": base_stats_death_eater, "Pixie": base_stats_pixie, "Werewolf": base_stats_werewolf,
    "deficiency defense": [0, 0, 0.05, 0.07, 0.12], "proficiency power": [0.05, 0.1, 0.15, 0.2, 0.25],
    "elite deficiency defense": [0, 0, 0.1, 0.15, 0.25], "elite proficiency power": [0.1, 0.2, 0.3, 0.4, 0.5]}
    def __init__(self, Type, Stars, Elite = False, Chamber = 20):
        self.stars = Stars
        self.type = Type
        self.elite = Elite
        self.chamber = Chamber
        self.level = levelFoe(self)
        self.defense = Foe.base_stats[self.type]["defense"][self.stars - 1]
        self.defense_breach = Foe.base_stats[self.type]["defense breach"][self.stars - 1]
        self.dodge = Foe.base_stats[self.type]["dodge"][self.stars - 1]
        if not Elite:
            self.deficiency_defense = Foe.base_stats["deficiency defense"][self.stars - 1] * (1 + 0.01 * self.level)
            self.proficiency_power = Foe.base_stats["proficiency power"][self.stars - 1] * (1 + 0.01 * self.level)
            self.max_stamina = Foe.base_stats[self.type]["stamina"][self.stars - 1] * stats_multiplier(self)
            self.power = Foe.base_stats[self.type]["power"][self.stars - 1] * stats_multiplier(self)
        else:
            self.deficiency_defense = Foe.base_stats["elite deficiency defense"][self.stars - 1] * (1 + 0.01 * self.level)
            self.proficiency_power = Foe.base_stats["elite proficiency power"][self.stars - 1] * (1 + 0.01 * self.level)
            self.max_stamina = Foe.base_stats[self.type]["elite stamina"][self.stars - 1] * stats_multiplier(self)
            self.power = Foe.base_stats[self.type]["elite power"][self.stars - 1] * stats_multiplier(self)