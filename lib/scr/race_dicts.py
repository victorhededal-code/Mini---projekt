racedict = {
    "aasimar": {
        "CreatureType": "Humanoid",
        "Small": "about 2-4 feet tall",
        "Medium": "about 4-7 feet tall",
        "Speed": "30 feet",

        "Celestial Resistance": "You have Resistance to Necrotic damage and Radiant damage.",
        "Darkvision": "You have Darkvision with a range of 60 feet.",
        "Healing Hands": "As a Magic action, you touch a creature and roll a number of d4s equal to your Proficiency Bonus. The creature regains Hit Points equal to the total rolled. Once per Long Rest.",
        "Light Bearer": "You know the Light cantrip. Charisma is your spellcasting ability.",
        "Celestial Revelation": "At level 3, transform as a Bonus Action for 1 minute. Once per turn deal extra damage equal to your Proficiency Bonus. Once per Long Rest.",
        "Heavenly Wings": "You gain a Fly Speed equal to your Speed for the duration.",
        "Inner Radiance": "Bright Light 10 ft, Dim Light 10 ft. Creatures within 10 ft take Radiant damage equal to your Proficiency Bonus at end of your turns.",
        "Necrotic Shroud": "Creatures within 10 ft must make a Charisma save or be Frightened until end of your next turn."
    },

    "dragonborn": {
        "CreatureType": "Humanoid",
        "Medium": "about 5-7 feet tall",
        "Speed": "30 feet",

        "Draconic Ancestry": "Determines Breath Weapon, Resistance, and appearance.",
        "Draconic Ancestors": """Black: Acid
Blue: Lightning
Brass: Fire
Bronze: Lightning
Copper: Acid
Gold: Fire
Green: Poison
Red: Fire
Silver: Cold
White: Cold""",

        "Breath Weapon": "Replace one attack with a 15-ft cone or 30-ft line. Dex save (DC = 8 + CON mod + PB). Damage scales 1d10 → 4d10. Uses = PB per Long Rest.",
        "Damage Resistance": "Resistance based on ancestry.",
        "Darkvision": "60 feet",
        "Draconic Flight": "At level 5, Bonus Action to gain Fly Speed for 10 minutes. Once per Long Rest."
    },

    "dwarf": {
        "CreatureType": "Humanoid",
        "Medium": "about 4-5 feet tall",
        "Speed": "30 feet",

        "Darkvision": "120 feet",
        "Dwarven Resilience": "Resistance to Poison damage and Advantage vs Poisoned.",
        "Dwarven Toughness": "+1 HP per level.",
        "Stonecunning": "Bonus Action: Tremorsense 60 ft for 10 minutes (PB uses per Long Rest)."
    },

    "elf": {
        "CreatureType": "Humanoid",
        "Medium": "about 5-6 feet tall",
        "Speed": "30 feet",

        "Darkvision": "60 feet",
        "Elven Lineage": "Gain spells at levels 1, 3, 5. Cast once per Long Rest or with slots.",
        "Elven Lineages": """Drow:
  Level 1: Darkvision 120 ft + Dancing Lights
  Level 3: Faerie Fire
  Level 5: Darkness

High Elf:
  Level 1: Prestidigitation
  Level 3: Detect Magic
  Level 5: Misty Step

Wood Elf:
  Level 1: Speed 35 ft + Druidcraft
  Level 3: Longstrider
  Level 5: Pass without Trace""",

        "Fey Ancestry": "Advantage vs Charmed.",
        "Keen Senses": "Proficiency in Insight, Perception, or Survival.",
        "Trance": "Long Rest in 4 hours."
    },

    "gnome": {
        "CreatureType": "Humanoid",
        "Small": "about 3-4 feet tall",
        "Speed": "30 feet",

        "Darkvision": "60 feet",
        "Gnomish Cunning": "Advantage on INT, WIS, CHA saves.",
        "Gnomish Lineage": "Choose lineage with magical abilities.",
        "Forest Gnome": "Minor Illusion + Speak with Animals (PB uses).",
        "Rock Gnome": "Mending + Prestidigitation + clockwork devices."
    },

    "goliath": {
        "CreatureType": "Humanoid",
        "Medium": "about 7-8 feet tall",
        "Speed": "35 feet",

        "Giant Ancestry": "Choose ability (PB uses per Long Rest).",
        "Cloud's Jaunt": "Teleport 30 ft.",
        "Fire's Burn": "Extra 1d10 Fire damage.",
        "Frost's Chill": "Extra 1d6 Cold + slow target.",
        "Hill's Tumble": "Knock creature Prone.",
        "Stone's Endurance": "Reduce damage (1d12 + CON).",
        "Storm's Thunder": "Reaction: deal 1d8 Thunder damage.",
        "Large Form": "At level 5, become Large for 10 min.",
        "Powerful Build": "Better carrying + escape Grapples."
    },

    "halfling": {
        "CreatureType": "Humanoid",
        "Small": "about 2-3 feet tall",
        "Speed": "30 feet",

        "Brave": "Advantage vs Frightened.",
        "Halfling Nimbleness": "Move through larger creatures.",
        "Luck": "Reroll natural 1s.",
        "Naturally Stealthy": "Hide behind larger creatures."
    },

    "human": {
        "CreatureType": "Humanoid",
        "Small": "about 2-4 feet tall",
        "Medium": "about 4-7 feet tall",
        "Speed": "30 feet",

        "Resourceful": "Gain Heroic Inspiration on Long Rest.",
        "Skillful": "One skill proficiency.",
        "Versatile": "One Origin feat."
    },

    "orc": {
        "CreatureType": "Humanoid",
        "Medium": "about 6-7 feet tall",
        "Speed": "30 feet",

        "Adrenaline Rush": "Bonus Action Dash + temp HP (PB uses).",
        "Darkvision": "120 feet",
        "Relentless Endurance": "Drop to 1 HP instead of 0 (once per Long Rest)."
    },

    "tiefling": {
        "CreatureType": "Humanoid",
        "Small": "about 3-4 feet tall",
        "Medium": "about 4-7 feet tall",
        "Speed": "30 feet",

        "Darkvision": "60 feet",
        "Fiendish Legacy": "Gain spells at levels 1, 3, 5.",
        "Fiendish Legacies": """Abyssal:
  Level 1: Poison Resistance + Poison Spray
  Level 3: Ray of Sickness
  Level 5: Hold Person

Chthonic:
  Level 1: Necrotic Resistance + Chill Touch
  Level 3: False Life
  Level 5: Ray of Enfeeblement

Infernal:
  Level 1: Fire Resistance + Fire Bolt
  Level 3: Hellish Rebuke
  Level 5: Darkness""",

        "Otherworldly Presence": "You know Thaumaturgy."
    }
}
"""for i in human_dict:
    print(i, ':', human_dict[i])"""