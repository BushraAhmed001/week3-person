from person import Superhero
batman = Superhero("Batman","Bruce Wayne", "Super Rich", "Joker","Home")
print(batman.name)
print(batman.identity)
print(batman.power)
print(batman.enemy)
batman.introduce()
batman.set_new_lair("Wayne Towers")
print(batman.new_lair)
print(f"Lair: {batman.get_lair()}.")
