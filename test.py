"""This is an attempt to make a mad lib. I am going to do it once here, then another time in atom, to really nail it down."""
print "The game has begun!"
name = raw_input("Enter a name: ")
adj1 = raw_input("Enter an adjective (1 of 3): ")
adj2 = raw_input("Enter an adjective (2 of 3): ")
adj3 = raw_input("Enter an adjective (3 of 3): ")
verb1 = raw_input("Enter a verb (1 of 3): ")
verb2 = raw_input("Enter a verb (2 of 3): ")
verb3 = raw_input("Enter a verb (3 of 3): ")
noun1 = raw_input("Enter a noun (1 of 4): ")
noun2 = raw_input("Enter a noun (2 of 4): ")
noun3 = raw_input("Enter a noun (3 of 4): ")
noun4 = raw_input("Enter a noun (4 of 4): ")
animal = raw_input("Enter an animal: ")
food = raw_input("Enter a food: ")
fruit = raw_input("Enter a fruit: ")
number = raw_input("Enter a number: ")
supername = raw_input("Enter a superhero name: ")
country = raw_input("Enter a country: ")
dessert = raw_input("Enter a dessert: ")
year = raw_input("Enter a year: ")



#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rhythm of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world."

print STORY % (adj1, name, verb1, adj2, noun1, noun2, animal, food, verb2, noun3, fruit, adj3, name, verb3, number, name, supername, supername, name, country, name, dessert, name, year, noun4)
