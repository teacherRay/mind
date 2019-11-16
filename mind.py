# https://github.com/teacherRay/mind.git
import random

#my dictionary of affirmations
affirmations={
'health':'All the organs, tissues, cells and atoms of my body are working together in harmony to create perfect health.', 
'mind':'I stay calm and relaxed by reqular meditation.',
'strength':'I enjoy exercises that strengthen my body and mind',
'life':'What would it look like to be living my ideal life?',
'inside':'I have everything I need inside me now.',
'abundant':'I am abundant.',
'forgiveness':'I forgive myself for what I have done, and I forgive all those who have harmed me.',
'teachers':'My teachers are everyone I encounter.',
'gratitude':'I am grateful for everything I have.'
}

#randomly choose from the dictionary of affirmations and print to console
choice=random.choice(list(affirmations.values()))
print(choice)
print(affirmations)

