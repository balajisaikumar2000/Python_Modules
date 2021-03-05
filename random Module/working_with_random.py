import random

#numbers between 0-1
value = random.random()           #we will get the value betweeen 0-1 excluding 1,and result will have only floating points
print(value)

#floating values between certain  range
value1 = random.uniform(1,10)         #result will be between 1-10 excluding 10
print(value1)

#random integers:
value = random.randint(1,6)     #in this method result will between 1-6 ,with 6 including
print(value)

#choice:
greetings = ["hello","hi","hey","howdy","hola"]
value = random.choice(greetings)     #choice doesn't take between values it needs a list ,or tuple
print(value+ " " + "balaji!")

#choices:

#choice will return only one value from a set
#if we want more than one  we have to use choices over choice and k here is how many we want to retrive
colors = ["Red","Black","Green"]
results = random.choices(colors,k=5)
print(results)

colors = ["Red","Black","Green"]
#weights will tell the probability
#here red is assigned to 18 ,and total sum of numbers in that list is 42,i.e probability of red to come is 20/42 and black is 20/42 and greeen is 2/42 ,so green will have leass chances to come
results = random.choices(colors,weights=[20,20,2],k=10)
print(results)

deck = list(range(1,53))     #we have 52 numbers here
print(deck)
random.shuffle(deck)            #numbers
print(deck)

#shuffling is ok ,but when we want to pick some random numbers out of it(say 10 numbers out of 52)
res = random.choices(deck,k=10)
print(res)
#there is a chance of getting similar values with choices method
hand = random.sample(deck,k=10)                  #sample() will return only unique values
print(hand)

#practical usage
#here we are using our random module into use case
#we are creating address for 100 members with this information below

first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria']

last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']

street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park', 'Oak', 'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill']

fake_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnydale', 'Bedrock', 'South Park', 'Atlantis', 'Mordor', 'Olympus', 'Dawnstar', 'Balmora', 'Gotham', 'Springfield', 'Quahog', 'Smalltown', 'Epicburg', 'Pythonville', 'Faketown', 'Westworld', 'Thundera', 'Vice City', 'Blackwater', 'Oldtown', 'Valyria', 'Winterfell', 'Braavos', 'Lakeview']

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

for num in range(100):    #starts with 0-99
    first = random.choice(first_names)
    last = random.choice(last_names)
    phone = f'{random.randint(100,999)}-555-{random.randint(1000,9999)}'
    street_num =random.randint(100,999)
    street = random.choice(street_names)
    city = random.choice(fake_cities)
    state = random.choice(states)
    zip_code =random.randint(10000,99999)
    address = f'{street_num} {street} St., {city} {state} {zip_code}'
    email =first.lower() + last.lower() + '@bogusemail.com'
    print(f'{first} {last}\n{phone}\n{address}\n{email}\n')

