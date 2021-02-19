# rock_scissors_lizard_spock_back

Backend for rock, scissors, lizard,spock game. The game was originally created by [Sam Kass with Karen Bryla](https://bigbangtheory.fandom.com/wiki/Rock,_Paper,_Scissors,_Lizard,_Spock).  


## Rules
Scissors cuts Paper  
Paper covers Rock  
Rock crushes Lizard  
Lizard poisons Spock  
Spock smashes Scissors  
Scissors decapitates Lizard  
Lizard eats Paper  
Paper disproves Spock  
Spock vaporizes Rock  
(and as it always has) Rock crushes Scissors  


# To run locally  
**pre requirements Python 3.+ and Virtualenv**  
1. Create virtual environment and activate environment  
`python3 -m venv venv`  
`source venv/bin/activate`

2. Clone repository   
`git clone https://github.com/andreayully/rock_scissors_lizard_spock_back.git`

3. Install requirements   
`pip install -r requirements.txt`

4. Runserver   
` python manage.py runserver`

# Frontend in React  
https://github.com/andreayully/rock_scissors_lizard_spock_front  

### Swagger generator  
For documentation  
http://localhost:8000/swagger/  
http://localhost:8000/redoc/

### Postman collection  
https://www.getpostman.com/collections/e906d12b4a8b920615f7  

### Feature
* Django 3.1.5
* Django Rest-Framework 3.12.2
