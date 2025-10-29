"""
COMP 163 - Project 1: Character Creator & Chronicles

This solution sticks to concepts through the Files chapter:
- functions, dicts/lists, conditionals/loops, try/except, file I/O
(no classes, no advanced libraries).

AI-usage transparency:
- (AI-assisted) comments mark places where ChatGPT helped with phrasing/structure.
- Student reviewed, tested, and can explain each line during interview.
"""

# =============================
# Configuration & Data Tables
# =============================

# (AI-assisted) Class table chosen for test compatibility:
# README screenshots list Warrior, Mage, Rogue, Cleric with qualitative goals:
# Warrior: High STR, low MAG, high HP
# Mage:    Low STR, high MAG, medium HP
# Rogue:   Medium STR, medium MAG, low HP
# Cleric:  Medium STR, high MAG, high HP
#
# B1 Balanced Linear: base + level*growth f*
