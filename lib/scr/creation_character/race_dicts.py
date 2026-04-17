aasimar_dict = {
    "CreatureType": "Humanoid",
    "Small": "about 2-4 feet tall",
    "Medium": "about 4-7 feet tall",
    "Speed": "30 feet",

    "Celestial Resistance": "You have Resistance to Necrotic damage and Radiant damage.",

    "Darkvision": "You have Darkvision with a range of 60 feet.",

    "Healing Hands": "As a Magic action, you touch a creature and roll a number of d4s equal to your Proficiency Bonus. The creature regains a number of Hit Points equal to the total rolled. Once you use this trait, you can't use it again until you finish a Long Rest.",

    "Light Bearer": "You know the Light cantrip. Charisma is your spellcasting ability for it.",

    "Celestial Revelation": "At level 3, you can transform as a Bonus Action for 1 minute. Once per turn, you deal extra damage equal to your Proficiency Bonus (Necrotic or Radiant depending on form). Once used, you must finish a Long Rest before using it again.",

    "Heavenly Wings": "You gain a Fly Speed equal to your Speed for the duration.",

    "Inner Radiance": "You shed Bright Light in a 10-foot radius and Dim Light for 10 more feet. At the end of each of your turns, creatures within 10 feet take Radiant damage equal to your Proficiency Bonus.",

    "Necrotic Shroud": "Creatures within 10 feet must succeed on a Charisma saving throw or become Frightened until the end of your next turn."
}

dragonborn_dict = {
    "CreatureType": "Humanoid",
    "Medium": "about 5-7 feet tall",
    "Speed": "30 feet",

    "Draconic Ancestry": "Your lineage stems from a dragon progenitor. Your choice determines your Breath Weapon, Damage Resistance, and appearance.",

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

    "Breath Weapon": "You can replace one attack with a breath attack (15-foot cone or 30-foot line). Targets make a Dexterity save (DC = 8 + CON mod + Proficiency Bonus). Damage starts at 1d10 and increases at levels 5 (2d10), 11 (3d10), and 17 (4d10). Uses equal to Proficiency Bonus per Long Rest.",

    "Damage Resistance": "You have Resistance to the damage type determined by your Draconic Ancestry.",

    "Darkvision": "You have Darkvision with a range of 60 feet.",

    "Draconic Flight": "At level 5, you can sprout spectral wings as a Bonus Action, gaining a Fly Speed equal to your Speed for up to 10 minutes. Once used, you must finish a Long Rest before using it again."
}

dwarf_dict = {
    "CreatureType": "Humanoid",
    "Medium": "about 4-5 feet tall",
    "Speed": "30 feet",

    "Darkvision": "You have Darkvision with a range of 120 feet.",

    "Dwarven Resilience": "You have Resistance to Poison damage and Advantage on saving throws against being Poisoned.",

    "Dwarven Toughness": "Your Hit Point maximum increases by 1, and it increases by 1 again whenever you gain a level.",

    "Stonecunning": "As a Bonus Action, you gain Tremorsense (60 ft) for 10 minutes while touching stone. Uses equal to your Proficiency Bonus per Long Rest."
}

elf_dict = {
    "CreatureType": "Humanoid",
    "Medium": "about 5-6 feet tall",
    "Speed": "30 feet",

    "Darkvision": "You have Darkvision with a range of 60 feet.",

    "Elven Lineage": "Choose a lineage that grants magical abilities. You gain spells at levels 1, 3, and 5. You can cast each once per Long Rest without a spell slot, or with slots if available. Your spellcasting ability is Intelligence, Wisdom, or Charisma (chosen when selecting lineage).",

    "Elven Lineages": """Drow:
  Level 1: Darkvision increases to 120 ft + Dancing Lights
  Level 3: Faerie Fire
  Level 5: Darkness

High Elf:
  Level 1: Prestidigitation (can swap on Long Rest)
  Level 3: Detect Magic
  Level 5: Misty Step

Wood Elf:
  Level 1: Speed becomes 35 ft + Druidcraft
  Level 3: Longstrider
  Level 5: Pass without Trace""",

    "Fey Ancestry": "You have Advantage on saving throws against being Charmed.",

    "Keen Senses": "You gain proficiency in Insight, Perception, or Survival.",

    "Trance": "You don't need to sleep. You can complete a Long Rest in 4 hours while remaining conscious in meditation."
}

gnome_dict = {
    "CreatureType": "Humanoid",
    "Small": "about 3-4 feet tall",
    "Speed": "30 feet",

    "Darkvision": "You have Darkvision with a range of 60 feet.",

    "Gnomish Cunning": "You have Advantage on Intelligence, Wisdom, and Charisma saving throws.",

    "Gnomish Lineage": "Choose a lineage that grants magical abilities. Your spellcasting ability is Intelligence, Wisdom, or Charisma (chosen when selecting lineage).",

    "Forest Gnome": "You know Minor Illusion. You can cast Speak with Animals a number of times equal to your Proficiency Bonus per Long Rest, without a spell slot (or using spell slots).",

    "Rock Gnome": "You know Mending and Prestidigitation. You can spend 10 minutes to create a Tiny clockwork device (max 3 at a time, lasts 8 hours) that produces a chosen Prestidigitation effect when activated."
}

goliath_dict = {
    "CreatureType": "Humanoid",
    "Medium": "about 7-8 feet tall",
    "Speed": "35 feet",

    "Giant Ancestry": "Choose a giant ancestry boon. You can use the chosen ability a number of times equal to your Proficiency Bonus per Long Rest.",

    "Cloud's Jaunt": "Bonus Action: teleport up to 30 feet to a space you can see.",

    "Fire's Burn": "On hit, deal an extra 1d10 Fire damage.",

    "Frost's Chill": "On hit, deal an extra 1d6 Cold damage and reduce the target’s Speed by 10 feet until your next turn.",

    "Hill's Tumble": "On hit, you can knock a Large or smaller creature Prone.",

    "Stone's Endurance": "Reaction: reduce incoming damage by 1d12 + your Constitution modifier.",

    "Storm's Thunder": "Reaction: when a creature within 60 ft damages you, deal 1d8 Thunder damage to it.",

    "Large Form": "At level 5, you can become Large for 10 minutes (Bonus Action). You gain Advantage on Strength checks and +10 Speed. Once per Long Rest.",

    "Powerful Build": "You have Advantage on checks to escape Grappled and count as one size larger for carrying capacity."
}

halfling_dict = {
    "CreatureType": "Humanoid",
    "Small": "about 2-3 feet tall",
    "Speed": "30 feet",

    "Brave": "You have Advantage on saving throws against being Frightened.",

    "Halfling Nimbleness": "You can move through the space of any creature that is a size larger than you, but you can't stop in the same space.",

    "Luck": "When you roll a 1 on a d20 Test, you can reroll the die, and must use the new result.",

    "Naturally Stealthy": "You can take the Hide action even when only lightly obscured by a creature at least one size larger than you."
}

human_dict = {
    "CreatureType": "Humanoid",
    "Small": "about 2-4 feet tall",
    "Medium": "about 4-7 feet tall",
    "Speed": "30 feet",

    "Resourceful": "You gain Heroic Inspiration whenever you finish a Long Rest.",

    "Skillful": "You gain proficiency in one skill of your choice.",

    "Versatile": "You gain an Origin feat of your choice."
}

orc_dict = {
    "CreatureType": "Humanoid",
    "Medium": "about 6-7 feet tall",
    "Speed": "30 feet",

    "Adrenaline Rush": "You can take the Dash action as a Bonus Action. When you do so, you gain Temporary Hit Points equal to your Proficiency Bonus. Uses equal to your Proficiency Bonus per Long or Short Rest.",

    "Darkvision": "You have Darkvision with a range of 120 feet.",

    "Relentless Endurance": "When you are reduced to 0 Hit Points but not killed outright, you can drop to 1 Hit Point instead. Once used, you can't use it again until you finish a Long Rest."
}

tiefling_dict = {
    "CreatureType": "Humanoid",
    "Small": "about 3-4 feet tall",
    "Medium": "about 4-7 feet tall",
    "Speed": "30 feet",

    "Darkvision": "You have Darkvision with a range of 60 feet.",

    "Fiendish Legacy": "Choose a fiendish legacy that grants supernatural abilities. You gain spells at levels 1, 3, and 5. You can cast each once per Long Rest without a spell slot, or using spell slots if available. Your spellcasting ability is Intelligence, Wisdom, or Charisma (chosen when selecting the legacy).",

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

    "Otherworldly Presence": "You know Thaumaturgy. When you cast it, it uses your Fiendish Legacy spellcasting ability."
}

"""for i in human_dict:
    print(i, ':', human_dict[i])"""