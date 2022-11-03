#TODO Export to text file
#TODO More sliders

import random
import info
import os

class Character:
    def __init__(self, appearance, hair_style, hair_color, eye_color, race, gender, birthsign, c_class, attackStyle, quests, c_challenges):
        self.appearance = appearance
        self.hair_style = hair_style
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.race = race
        self.gender = gender
        self.birthsign = birthsign
        self.c_class = c_class
        self.attackStyle = attackStyle
        self.quests = quests
        self.c_challenges = c_challenges

    def setRace(self, raceChosen):
        self.race = raceChosen

    def getRace(self):
        return self.race

    def setAppearance(self, appearanceChosen):
        self.appearance = appearanceChosen

    def setHairStyle(self, hairStyleChosen):
        self.hair_style = hairStyleChosen

    def setHairColor(self, hairColorChosen):
        self.hair_color = hairColorChosen

    def setEyeColor(self, eyeColorChosen):
        self.eye_color = eyeColorChosen

    def setGender(self, genderChosen):
        self.gender = genderChosen

    def setBirthsign(self, birthsignChosen):
        self.birthsign = birthsignChosen

    def setClass(self, c_classChosen):
        self.c_class = c_classChosen

    def setAttackStyle(self, attackStyleSet):
        self.attackStyle = attackStyleSet

        if self.c_class == "Custom Class":
            # A function within a function is known as a closure
            # If the custom class option is chosen within the class list, then it will go here and choose a specialization, two attributes and seven skills.
            print("\n=======CLASS DETAILS===========")
            def chooseSpecialization():
                # Specialization. i.e. Magic, Combat or Stealh
                special = random.choice(info.specializations)
                oneHandedWeapons = info.one_handed_weapons
                randomOneHandedWeapon = random.choice(oneHandedWeapons)
                
                twoHandedWeapons = info.two_handed_weapons
                randomTwoHandedWeapon = random.choice(twoHandedWeapons)
                global lines2
                global lines4
                global lines5
                print("- - - - - ", "\nSPECIALIZATION:", special, "\n- - - - - ")
                
                # If specialization is equal to magic, then set the attack style that the user will use to one of the three options located in the attack_styles dictionairy and then randomly select an option from one of those chosen dictionaries, i.e. combat attack style and within that the weapon and shield attack style
                if special == "Magic":

                    # Selects this list from the dictionairy located in info
                    magicAtk = info.attack_style["Magic Attack Style"]
                    randMagicAtk = random.choice(magicAtk)
                    lineTest1 = ""
                    lineTest2 = ""
                    lineTest3 = ""
                    lineTest4 = ""
                    lineTest5 = ""

                    print("METHOD OF ATTACK:", randMagicAtk, "\n- - - - - ")
                    if randMagicAtk == "One-Handed Weapon + Magic":
                        print("WEAPON:", "{} and Magic".format(randomOneHandedWeapon), "\n- - - - - ")
                        lineTest1 = "\nWEAPON: "
                        lineTest2 = "{} and Magic".format(randomOneHandedWeapon)
                        lineTest3 = "\n- - - - - "
                        lineTest4 = lineTest1 + lineTest2 + lineTest3
                        lineTest5 = lineTest4

                    randArmour = random.choice(info.armour)
                    print("ARMOUR:", randArmour, "\n- - - - - ")

                    newLine1 = str("\n=======CLASS DETAILS===========\n")
                    newLine2 = str("METHOD OF ATTACK: ")
                    newLine3 = str(randMagicAtk)
                    newLine4 = str("\n- - - - - ")
                    newLine5 = str(lineTest5)
                    newLine6 = str("\nARMOUR: ")
                    newLine7 = str(randArmour)
                    newLine8 = str("\n- - - - - ")
                    newLines = newLine1 + newLine2 + newLine3 + newLine4 + newLine5 + newLine6 + newLine7 + newLine8
                    newLinesSpaced = newLines

                    lines2 = newLinesSpaced

                elif special == "Combat":

                    combatAtk = info.attack_style["Combat Attack Style"]
                    randCombatAtk = random.choice(combatAtk)
                    lineTest1 = ""
                    lineTest2 = ""
                    lineTest3 = ""
                    lineTest4 = ""
                    lineTest5 = ""
                    print("METHOD OF ATTACK:", randCombatAtk, "\n- - - - - ")
                    
                    if randCombatAtk == "One-Handed Weapon" or randCombatAtk == "Weapon and Shield":
                        print("WEAPON:", "{0}".format(randomOneHandedWeapon), "\n- - - - - ")
                        lineTest1 = "\nWEAPON: "
                        lineTest2 = "{0}".format(randomOneHandedWeapon)
                        lineTest3 = "\n- - - - - "
                        lineTest4 = lineTest1 + lineTest2 + lineTest3
                        lineTest5 = lineTest4

                    elif randCombatAtk == "Two-Handed Weapon":
                        print("WEAPON:", "{0}".format(randomTwoHandedWeapon), "\n- - - - - ")
                        lineTest1 = "\nWEAPON: "
                        lineTest2 = "{0}".format(randomTwoHandedWeapon)
                        lineTest3 = "\n- - - - - "
                        lineTest4 = lineTest1 + lineTest2 + lineTest3
                        lineTest5 = lineTest4

                    randArmour = random.choice(info.armour)
                    print("ARMOUR:", randArmour, "\n- - - - - ")

                    newLine1 = str("\n=======CLASS DETAILS===========\n")
                    newLine2 = str("METHOD OF ATTACK: ")
                    newLine3 = str(randCombatAtk)
                    newLine4 = str("\n- - - - - ")
                    newLine5 = str(lineTest5)
                    newLine6 = str("\nARMOUR: ")
                    newLine7 = str(randArmour)
                    newLine8 = str("\n- - - - - ")

                    newLines = newLine1 + newLine2 + newLine3 + newLine4 + newLine5 + newLine6 + newLine7 + newLine8
                    newLinesSpaced = newLines

                    lines2 = newLinesSpaced

                elif special == "Stealth":

                    stealthAtk = info.attack_style["Stealth Attack Style"]
                    randStealthAtk = random.choice(stealthAtk)
                    lineTest1 = ""
                    lineTest2 = ""
                    lineTest3 = ""
                    lineTest4 = ""
                    lineTest5 = ""
                    print("METHOD OF ATTACK:", randStealthAtk, "\n- - - - - ")

                    if randStealthAtk == "One-Handed Weapon":
                        print("WEAPON:", "{0}".format(randomOneHandedWeapon), "\n- - - - - ")
                        lineTest1 = "\nWEAPON: "
                        lineTest2 = "{0}".format(randomOneHandedWeapon)
                        lineTest3 = "\n- - - - - "
                        lineTest4 = lineTest1 + lineTest2 + lineTest3
                        lineTest5 = lineTest4

                    randArmour = random.choice(info.armour)
                    print("ARMOUR:", randArmour, "\n- - - - - ")

                    newLine1 = str("\n=======CLASS DETAILS===========\n")
                    newLine2 = str("METHOD OF ATTACK: ")
                    newLine3 = str(randStealthAtk)
                    newLine4 = str("\n- - - - - ")
                    newLine5 = str(lineTest5)
                    newLine6 = str("\nARMOUR: ")
                    newLine7 = str(randArmour)
                    newLine8 = str("\n- - - - - ")
                    newLines = newLine1 + newLine2 + newLine3 + newLine4 + newLine5 + newLine6 + newLine7 + newLine8
                    newLinesSpaced = newLines

                    lines2 = newLinesSpaced
                
                else:
                    print("Nope")

            def chooseTwoAttributes():
                global lines4
                global lines5
                two_attr = random.sample(info.attributes, 2)
                two_attr_join = ',\n '.join(two_attr)
                print("TWO MAIN ATTRIBUTES:\n[", two_attr_join, "]", "\n- - - - - ")
                newLine1 = "\nTWO MAIN ATTRIBUTES:\n["
                newLine2 = two_attr_join
                newLine3 = "]"
                newLine4 = "\n- - - - - \n"
                newLines = newLine1 + newLine2 + newLine3 + newLine4

                lines4 = newLines
                

            def chooseSevenSkills():
                global lines4
                global lines5
                seven_skills = random.sample(info.skills, 7)
                seven_skills_join = ',\n '.join(seven_skills)
                print("SEVEN SKILLS:\n[", seven_skills_join, "]", "\n- - - - - ", "\n===============================")
                newLine1 = "SEVEN SKILLS:\n["
                newLine2 = seven_skills_join
                newLine3 = "]"
                newLine4 = "\n- - - - - "
                newLine5 = "\n===============================\n"
                newLines = newLine1 + newLine2 + newLine3 + newLine4 + newLine5

                lines5 = newLines

            chooseSpecialization()
            chooseTwoAttributes()
            chooseSevenSkills()

        else:
            None

    def setQuests(self, questsSet):
        self.quests = questsSet

    def setChallenges(self, challengesSet):
        self.c_challenges = challengesSet

class advancedCharacter(Character):
    def __init__(self, face, tone, hair, eye_color):
        self.face = face
        self.tone = tone
        self.hair = hair
        self.eye_color = eye_color

    def FACE(self):
        print("\n*******************************")
        print("       FACE DETAILS")
        
        print("\n=======FACE SLIDERS============")
        
        Face = [1, 2, 3, 4, 5]

        for i in Face:
            print("Move Face Slider #{}".format(i), end=" ")
            i = random.choice(info.slider_options)
            print("{}".format(i))

        print("===============================")

        print("\n=======BROW SLIDERS============")

        Brow = [1, 2, 3]

        for i in Brow:
            print("Move Brow Slider #{}".format(i), end=" ")
            i = random.choice(info.slider_options)
            print("{}".format(i))

        print("===============================")

        print("\n=======CHEEKS SLIDERS==========")

        Cheeks = [1, 2, 3, 4, 5]

        for i in Cheeks:
            print("Move Cheeks Slider #{}".format(i), end=" ")
            i = random.choice(info.slider_options)
            print("{}".format(i))

        print("===============================")

        print("\n=======CHIN SLIDERS============")

        Chin = [1, 2, 3, 4, 5, 6, 7]

        for i in Chin:
            print("Move Chin Slider #{}".format(i), end=" ")
            i = random.choice(info.slider_options)
            print("{}".format(i))

        print("===============================")

        print("\n=======EYES SLIDERS============")

        Eyes = [1, 2, 3, 4]

        for i in Eyes:
            print("Move Eyes Slider #{}".format(i), end=" ")
            i = random.choice(info.slider_options)
            print("{}".format(i))

        print("===============================")

        print("\n=======FOREHEAD SLIDERS========")

        Forehead = [1, 2, 3]

        for i in Forehead:
            print("Move Forehead Slider #{}".format(i), end=" ")
            i = random.choice(info.slider_options)
            print("{}".format(i))

        print("===============================")

        print("\n=======JAW SLIDERS=============")

        Jaw = [1, 2, 3, 4]

        for i in Jaw:
            print("Move Jaw Slider #{}".format(i), end=" ")
            i = random.choice(info.slider_options)
            print("{}".format(i))

        print("===============================")

        print("\n=======MOUTH SLIDERS===========")

        Mouth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        for i in Mouth:
            print("Move Mouth Slider #{}".format(i), end=" ")
            i = random.choice(info.slider_options)
            print("{}".format(i))

        print("===============================")

        print("\n=======NOSE SLIDERS============")

        Nose = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

        for i in Nose:
            print("Move Nose Slider #{}".format(i), end=" ")
            i = random.choice(info.slider_options)
            print("{}".format(i))

        print("\n===============================")

        print("\n*******************************")

    def TONE(self):
        print("\n*******************************")
        print("       TONE DETAILS")
        
        print("\n=======SKIN SLIDERS============")
        
        Skin = [1, 2, 3, 4, 5]

        for i in Skin:
            print("Move Skin Slider #{}".format(i), end=" ")
            i = random.choice(info.slider_options)
            print("{}".format(i))

        print("===============================")

        print("\n=======BEARD SLIDERS===========")

        Beard = [1, 2, 3, 4, 5, 6]

        for i in Beard:
            print("Move Beard Slider #{}".format(i), end=" ")
            i = random.choice(info.slider_options)
            print("{}".format(i))

        print("===============================")

        print("\n=======EYES SLIDERS============")

        Eyes = [1, 2, 3, 4, 5, 6]

        for i in Eyes:
            print("Move Eyes Slider #{}".format(i), end=" ")
            i = random.choice(info.slider_options)
            print("{}".format(i))

        print("===============================")

        print("\n=======EYEBROWS SLIDERS========")

        Eyebrows = [1, 2, 3, 4, 5, 6, 7]

        for i in Eyebrows:
            print("Move Eyebrows Slider #{}".format(i), end=" ")
            i = random.choice(info.slider_options)
            print("{}".format(i))

        print("===============================")

        print("\n=======LIPS SLIDERS==========")

        Lips = [1, 2, 3]

        for i in Lips:
            print("Move Lips Slider #{}".format(i), end=" ")
            i = random.choice(info.slider_options)
            print("{}".format(i))

        print("===============================")

        print("\n=======NOSE SLIDERS============")

        Nose = [1, 2]

        for i in Nose:
            print("Move Nose Slider #{}".format(i), end=" ")
            i = random.choice(info.slider_options)
            print("{}".format(i))

        print("\n===============================")

        print("*******************************")

oneHandedWeapons = info.one_handed_weapons
randomOneHandedWeapon = random.choice(oneHandedWeapons)             
twoHandedWeapons = info.two_handed_weapons
randomTwoHandedWeapon = random.choice(twoHandedWeapons)

randRace = random.choice(info.races)
randAppearance = random.randrange(1,11)

randHumanMaleHair = random.choice(info.male_human_hair_styles)
randHumanFemaleHair = random.choice(info.female_human_hair_styles)

randElfMaleHair = random.choice(info.male_elf_hair)
randElfFemaleHair = random.choice(info.female_elf_hair)

randKhajiitMaleHair = random.choice(info.male_khajiit_hair)
randKhajiitFemaleHair = random.choice(info.female_khajiit_hair)

randOrcMaleHair = random.choice(info.male_orc_hair)
randOrcFemaleHair = random.choice(info.female_orc_hair)

randRedguardMaleHair = random.choice(info.male_redguard_hair)
randRedguardFemaleHair = random.choice(info.female_redguard_hair)

randArgonianMaleHair = random.choice(info.male_argonian_hair)
randArgonianFemaleHair = random.choice(info.female_argonian_hair)

randHairColor = random.choice(info.hair_color)
randEyeColor = random.choice(info.eye_color)
randGender = random.choice(info.genders)
randBirthsign = random.choice(info.birthsigns)

randClass = random.choice(info.classes)
randAttackStyle = random.choice(info.attack_style["Magic Attack Style"])
randQuestsNum = random.randrange(1, 4)
randQuests = random.sample(info.questlines, randQuestsNum)
randChallenges = random.choice(info.challenges)
randCity = random.choice(info.cities)
randNum = random.randrange(1, 101)

randArmour = random.choice(info.armour)

classSpecialization = None

def combatSpec():
    print("\n=======CLASS DETAILS===========")
    combatAtk = info.attack_style["Combat Attack Style"]
    randCombatAtk = random.choice(combatAtk)
    lineTest1 = ""
    lineTest2 = ""
    lineTest3 = ""
    lineTest4 = ""
    lineTest5 = ""
    global lines2
    global lines4
    global lines5
    print("METHOD OF ATTACK:", randCombatAtk, "\n- - - - - ")
            
    if randCombatAtk == "One-Handed Weapon" or randCombatAtk == "Weapon and Shield":
        print("WEAPON:", "{0}".format(randomOneHandedWeapon), "\n- - - - - ")
        lineTest1 = "\nWEAPON: "
        lineTest2 = "{0}".format(randomOneHandedWeapon)
        lineTest3 = "\n- - - - - "
        lineTest4 = lineTest1 + lineTest2 + lineTest3
        lineTest5 = lineTest4
        

    elif randCombatAtk == "Two-Handed Weapon":
        print("WEAPON:", "{0}".format(randomTwoHandedWeapon), "\n- - - - - ")
        lineTest1 = "\nWEAPON: "
        lineTest2 = "{0}".format(randomTwoHandedWeapon)
        lineTest3 = "\n- - - - - "
        lineTest4 = lineTest1 + lineTest2 + lineTest3
        lineTest5 = lineTest4
        
    print("ARMOUR:", randArmour, "\n- - - - - ")
    print("===============================")
    newLine1 = str("\n=======CLASS DETAILS===========\n")
    newLine2 = str("METHOD OF ATTACK: ")
    newLine3 = str(randCombatAtk)
    newLine4 = str("\n- - - - - ")
    newLine5 = str(lineTest5)
    newLine6 = str("\nARMOUR: ")
    newLine7 = str(randArmour)
    newLine8 = str("\n- - - - - ")
    newLine9 = str("\n===============================\n")
    newLines = newLine1 + newLine2 + newLine3 + newLine4 + newLine5 + newLine6 + newLine7 + newLine8 + newLine9
    newLinesSpaced = newLines

    lines2 = newLinesSpaced
    lines4 = ""
    lines5 = ""

def magicSpec():
    print("\n=======CLASS DETAILS===========")
    magicAtk = info.attack_style["Magic Attack Style"]
    randMagicAtk = random.choice(magicAtk)
    lineTest1 = ""
    lineTest2 = ""
    lineTest3 = ""
    lineTest4 = ""
    lineTest5 = ""
    global lines2
    global lines4
    global lines5
    print("METHOD OF ATTACK:", randMagicAtk, "\n- - - - - ")
    if randMagicAtk == "One-Handed Weapon + Magic":
        print("WEAPON:", "{} and Magic".format(randomOneHandedWeapon), "\n- - - - - ")
        lineTest1 = "\nWEAPON: "
        lineTest2 = "{} and Magic".format(randomOneHandedWeapon)
        lineTest3 = "\n- - - - - "
        lineTest4 = lineTest1 + lineTest2 + lineTest3
        lineTest5 = lineTest4

    print("ARMOUR:", randArmour, "\n- - - - - ")
    print("===============================")
    newLine1 = str("\n=======CLASS DETAILS===========\n")
    newLine2 = str("METHOD OF ATTACK: ")
    newLine3 = str(randMagicAtk)
    newLine4 = str("\n- - - - - ")
    newLine5 = str(lineTest5)
    newLine6 = str("\nARMOUR: ")
    newLine7 = str(randArmour)
    newLine8 = str("\n- - - - - ")
    newLine9 = str("\n===============================\n")
    newLines = newLine1 + newLine2 + newLine3 + newLine4 + newLine5 + newLine6 + newLine7 + newLine8 + newLine9
    newLinesSpaced = newLines

    lines2 = newLinesSpaced
    lines4 = ""
    lines5 = ""

def stealthSpec():
    print("\n=======CLASS DETAILS===========")
    stealthAtk = info.attack_style["Stealth Attack Style"]
    randStealthAtk = random.choice(stealthAtk)
    lineTest1 = ""
    lineTest2 = ""
    lineTest3 = ""
    lineTest4 = ""
    lineTest5 = ""
    global lines2
    global lines4
    global lines5
    print("METHOD OF ATTACK:", randStealthAtk, "\n- - - - - ")

    if randStealthAtk == "One-Handed Weapon":
        print("WEAPON:", "{0}".format(randomOneHandedWeapon), "\n- - - - - ")
        lineTest1 = "\nWEAPON: "
        lineTest2 = "{0}".format(randomOneHandedWeapon)
        lineTest3 = "\n- - - - - "
        lineTest4 = lineTest1 + lineTest2 + lineTest3
        lineTest5 = lineTest4

    print("ARMOUR:", randArmour, "\n- - - - - ")
    print("===============================")
    newLine1 = str("\n=======CLASS DETAILS===========\n")
    newLine2 = str("METHOD OF ATTACK: ")
    newLine3 = str(randStealthAtk)
    newLine4 = str("\n- - - - - ")
    newLine5 = str(lineTest5)
    newLine6 = str("\nARMOUR: ")
    newLine7 = str(randArmour)
    newLine8 = str("\n- - - - - ")
    newLine9 = str("\n===============================\n")
    newLines = newLine1 + newLine2 + newLine3 + newLine4 + newLine5 + newLine6 + newLine7 + newLine8 + newLine9
    newLinesSpaced = newLines

    lines2 = newLinesSpaced
    lines4 = ""
    lines5 = ""

if randClass == "Combat":
    classSpecialization = "Combat"
    randClass = random.choice(info.combat_classes)
elif randClass == "Magic":
    classSpecialization = "Magic"
    randClass = random.choice(info.magic_classes)
elif randClass == "Stealth":
    classSpecialization = "Stealth"
    randClass = random.choice(info.stealth_classes)
elif randClass == "Custom Class":
    classSpecialization == "Custom Class"

if randChallenges == "Complete all the quests in a City":
    randChallenges = "Complete all the quests in a City({0})".format(randCity)

def mainCharGen():
    C2 = Character(None, None, None, None, None, None, None, None, None, None, None)
    C2.setRace(randRace)
    C2.setAppearance(randAppearance)

    if randGender == "Male" and randRace == "Nord" or randRace == "Imperial" or randRace == "Breton":
        C2.setHairStyle(randHumanMaleHair)
    elif randGender == "Female" and randRace == "Nord" or randRace == "Imperial" or randRace == "Breton":
        C2.setHairStyle(randHumanFemaleHair)

    elif randGender == "Male" and randRace == "Wood Elf(Bosmer)" or randRace == "High Elf(Altmer)" or randRace == "Dark Elf(Dunmer)":
        C2.setHairStyle(randElfMaleHair)
    elif randGender == "Female" and randRace == "Wood Elf(Bosmer)" or randRace == "High Elf(Altmer)" or randRace == "Dark Elf(Dunmer)":
        C2.setHairStyle(randElfFemaleHair)

    elif randGender == "Male" and randRace == "Khajiit":
        C2.setHairStyle(randKhajiitMaleHair)
    elif randGender == "Female" and randRace == "Khajiit":
        C2.setHairStyle(randKhajiitFemaleHair)

    elif randGender == "Male" and randRace == "Orc":
        C2.setHairStyle(randOrcMaleHair)
    elif randGender == "Female" and randRace == "Orc":
        C2.setHairStyle(randOrcFemaleHair)

    elif randGender == "Male" and randRace == "Redguard":
        C2.setHairStyle(randRedguardMaleHair)
    elif randGender == "Female" and randRace == "Redguard":
        C2.setHairStyle(randRedguardFemaleHair)

    elif randGender == "Male" and randRace == "Argonian":
        C2.setHairStyle(randArgonianMaleHair)
    elif randGender == "Female" and randRace == "Argonian":
        C2.setHairStyle(randArgonianFemaleHair)

    C2.setHairColor(randHairColor)
    C2.setEyeColor(randEyeColor)

    C2.setGender(randGender)
    C2.setBirthsign(randBirthsign)
    C2.setClass(randClass)


    print("\n=======CHARACTER DETAILS=======", "\n- - - - - ", "\nRACE:", C2.race, "\n- - - - - ", "\nGENDER:", C2.gender, "\n- - - - -", "\nAPPEARANCE: Press the random appearance button {0} times".format(C2.appearance), "\n- - - - -", "\nHAIR STYLE:", C2.hair_style, "\n- - - - -", "\nHAIR COLOR:", C2.hair_color, "\n- - - - -", "\nEYE COLOR:", C2.eye_color, "\n- - - - - ", "\nBIRTHSIGN:", C2.birthsign, "\n- - - - - ", "\nCLASS:", C2.c_class, "\n- - - - - ", "\n===============================")
    C2.setAttackStyle(randAttackStyle)
    C2.setQuests(randQuests)
    C2.setChallenges(randChallenges)


    if classSpecialization == "Combat":
        combatSpec()
         
    elif classSpecialization == "Magic":
        magicSpec()  
            
    elif classSpecialization == "Stealth":
        stealthSpec()

    else:
        None


    print("\n=======QUESTS & OTHER==========", "\n- - - - - ", "\nMANDATORY QUESTS:", C2.quests, "\n- - - - - ", "\nCHALLENGES(Optional):", C2.c_challenges, "\n- - - - - ", "\n===============================")

    print("Your character data has been saved to a text file.\n")
    input("Press any key to exit.")
    lines1 = ["\n=======CHARACTER DETAILS=======", "\n- - - - - ", "\nRACE: ", C2.race, "\n- - - - - ", "\nGENDER: ", C2.gender, "\n- - - - -", "\nAPPEARANCE: Press the random appearance button {0} times".format(C2.appearance), "\n- - - - -", "\nHAIR STYLE: ", C2.hair_style, "\n- - - - -", "\nHAIR COLOR: ", C2.hair_color, "\n- - - - -", "\nEYE COLOR: ", C2.eye_color, "\n- - - - - ", "\nBIRTHSIGN: ", C2.birthsign, "\n- - - - - ", "\nCLASS: ", C2.c_class, "\n- - - - - ", "\n===============================\n"]
    lines3 = ["\n=======QUESTS & OTHER==========", "\n- - - - - ", "\nMANDATORY QUESTS: ", str(C2.quests), "\n- - - - - ", "\nCHALLENGES(Optional): ", C2.c_challenges, "\n- - - - - ", "\n==============================="]
    tx = "{0} {1}.txt".format(randRace, randClass)
    textFile = open(tx, "w")
    textFile.writelines(lines1)
    textFile.writelines(lines2)
    textFile.writelines(lines4)
    textFile.writelines(lines5)
    textFile.writelines(lines3)
    textFile.close()

def advancedCharGen():
    C1 = advancedCharacter("Face", None, None, None)
    C1.FACE()
    C1.TONE()

menu = [
   "1. Normal Character Generator",
   "2. Advanded Appearance Generator",
]

selected = 0

def display_menu(menu, selected):
    for number, item in enumerate(menu, 1):
        if number == selected:
            print('(X)', item)
        else:
            print('( )', item)

while True:
    display_menu(menu, selected)

    try:
        # don't assign directly to `selected` because user may choose wrong number
        new_selection = int(input("Please choose one of the menu options.\n"))

        if new_selection in (1, 2):
            # assign to `selected` when user choose correct number
            selected = new_selection

            display_menu(menu, selected)
 
            new = input("Would you like to make another selection? [Y/n]").lower()

            if new_selection == 1 and new in ("n", "no"):
                mainCharGen()
                os.system('cls')
                break

            if new_selection == 2 and new in ("n", "no"):
                mainCharGen()
                advancedCharGen()
                os.system('cls')
                break
            
            else:
                print()

            
                
        else:
            print("Invalid Choice. Enter one of the menu numbers.")
    except ValueError:
        print("Invalid Choice. Enter one of the menu numbers.")

"""if userInput1 == "Heya":
    C2 = Character(None, None, None, None, None, None, None, None, None, None, None)
    C2.setRace(randRace)
    C2.setAppearance(randAppearance)

    if randGender == "Male" and randRace == "Nord" or randRace == "Imperial" or randRace == "Breton":
        C2.setHairStyle(randHumanMaleHair)
    elif randGender == "Female" and randRace == "Nord" or randRace == "Imperial" or randRace == "Breton":
        C2.setHairStyle(randHumanFemaleHair)

    elif randGender == "Male" and randRace == "Wood Elf(Bosmer)" or randRace == "High Elf(Altmer)" or randRace == "Dark Elf(Dunmer)":
        C2.setHairStyle(randElfMaleHair)
    elif randGender == "Female" and randRace == "Wood Elf(Bosmer)" or randRace == "High Elf(Altmer)" or randRace == "Dark Elf(Dunmer)":
        C2.setHairStyle(randElfFemaleHair)

    elif randGender == "Male" and randRace == "Khajiit":
        C2.setHairStyle(randKhajiitMaleHair)
    elif randGender == "Female" and randRace == "Khajiit":
        C2.setHairStyle(randKhajiitFemaleHair)

    elif randGender == "Male" and randRace == "Orc":
        C2.setHairStyle(randOrcMaleHair)
    elif randGender == "Female" and randRace == "Orc":
        C2.setHairStyle(randOrcFemaleHair)

    elif randGender == "Male" and randRace == "Redguard":
        C2.setHairStyle(randRedguardMaleHair)
    elif randGender == "Female" and randRace == "Redguard":
        C2.setHairStyle(randRedguardFemaleHair)

    elif randGender == "Male" and randRace == "Argonian":
        C2.setHairStyle(randArgonianMaleHair)
    elif randGender == "Female" and randRace == "Argonian":
        C2.setHairStyle(randArgonianFemaleHair)

    C2.setHairColor(randHairColor)
    C2.setEyeColor(randEyeColor)

    C2.setGender(randGender)
    C2.setBirthsign(randBirthsign)
    C2.setClass(randClass)


    print("\n=======CHARACTER DETAILS=======", "\n- - - - - ", "\nRACE:", C2.race, "\n- - - - - ", "\nGENDER:", C2.gender, "\n- - - - -", "\nAPPEARANCE: Press the random appearance button {0} times".format(C2.appearance), "\n- - - - -", "\nHAIR STYLE:", C2.hair_style, "\n- - - - -", "\nHAIR COLOR:", C2.hair_color, "\n- - - - -", "\nEYE COLOR:", C2.eye_color, "\n- - - - - ", "\nBIRTHSIGN:", C2.birthsign, "\n- - - - - ", "\nCLASS:", C2.c_class, "\n- - - - - ", "\n===============================")
    C2.setAttackStyle(randAttackStyle)
    C2.setQuests(randQuests)
    C2.setChallenges(randChallenges)


    if classSpecialization == "Combat":
        combatSpec()
         
    elif classSpecialization == "Magic":
        magicSpec()  
            
    elif classSpecialization == "Stealth":
        stealthSpec()

    else:
        None


    print("\n=======QUESTS & OTHER==========", "\n- - - - - ", "\nMANDATORY QUESTS:", C2.quests, "\n- - - - - ", "\nCHALLENGES(Optional):", C2.c_challenges, "\n- - - - - ", "\n===============================")
else:
    print()

test2 = input()
if test2 == "yes":
    C1 = advancedCharacter("Face", None, None, None)
    C1.FACE()
    C1.TONE()
"""
