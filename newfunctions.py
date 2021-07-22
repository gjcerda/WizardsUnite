def levelFoe(Foe):
    chambers = [i for i in range(1,21)]
    levels = [3, 8, 18, 29, 38, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 187]
    return levels[Foe._chamber - 1]

def stats_multiplier(Foe):
    return 1 + 0.0816 * Foe._level

class BaseFoe:
    _cls_deficiency_defense = ((0, 0), (0, 0), (0.05, 0.1), (0.07, 0.15), (0.12, 0.15))
    _cls_proficiency_power = ((0.05, 0.1), (0.1, 0.2), (0.15, 0.3), (0.2, 0.4), (0.25, 0.5))  
    _cls_defense = 0, 0, 0, 0, 0
    _cls_defense_breach = 0, 0, 0, 0, 0
    _cls_dodge = 0, 0, 0, 0, 0
    _cls_stamina = 0, 0, 0, 0, 0
    _cls_power = 0, 0, 0, 0, 0
    def __init__(self, stars, Elite = False, Chamber = 20):
        self._stars = stars
        self._elite = Elite
        self._chamber = Chamber
        self._level = levelFoe(self)
        self._deficiency_defense = BaseFoe._cls_deficiency_defense[self._stars - 1][self._elite] * (1 + 0.01 * self._level)
        self._proficiency_power = BaseFoe._cls_proficiency_power[self._stars - 1][self._elite] * (1 + 0.01 * self._level)

    @property
    def defense(self) -> float:
        return self._cls_defense[self._stars - 1]

    @property
    def defense_breach(self) -> float:
        return self._cls_defense_breach[self._stars - 1]

    @property
    def dodge(self) -> float:
        return self._cls_dodge[self._stars - 1]

    @property
    def max_stamina(self) -> int:
        return self._cls_stamina[self._stars - 1][self._elite] * stats_multiplier(self)

    @property 
    def power(self) -> int:
        return self._cls_power[self._stars - 1][self._elite] * stats_multiplier(self)

class Erkling(BaseFoe):
    _cls_dodge = 0, 0.05, 0.25, 0.4, 0.6
    _cls_stamina = ((76, 141), (93, 173), (107, 200), (124, 231), (139, 258))
    _cls_power = ((7, 13), (8, 16), (10, 18), (11, 21), (13, 24))

class Acromantula(BaseFoe):
    _cls_stamina = ((72, 135), (91, 170), (109, 203), (136, 254), (166, 310))
    _cls_power = ((8, 16), (10, 19), (13, 24), (17, 32), (22, 41))

class DarkWizard(BaseFoe):
    _cls_defense = 0, 0.05, 0.15, 0.3, 0.5
    _cls_defense_breach = 0, 0.1, 0.2, 0.4
    _cls_stamina = ((62, 115), (76, 141), (88, 163), (101, 189), (113, 211))
    _cls_power = ((7, 14), (9, 18), (11, 20), (12, 24), (14, 26))

Foe1 = DarkWizard(4)
print(f"Stars: {Foe1._stars}\nDefense: {Foe1.defense}\nDefense Breach: {Foe1.defense_breach}\nDodge: {Foe1.dodge}")