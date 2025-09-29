import random

foods = [
    "🍕 Pizza – because salad is just crunchy sadness.",
    "🍔 Burger – happiness between two buns.",
    "🍜 Noodles – the slurp of champions.",
    "🥗 Salad – just kidding, order fries.",
    "🍩 Donuts – because abs are overrated.",
    "🍦 Ice Cream – therapy but colder.",
    "🌮 Tacos – fold happiness in half.",
    "🍿 Popcorn – perfect for eating while doing absolutely nothing."
]

print("🤖 Welcome to the Food Suggestion Bot 🤖")
print("Thinking what you should eat today...\n")

print("👉 You should eat:")
print(random.choice(foods))
