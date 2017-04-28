relay_pin = 2
frequency = 60 * 60 # 1 hour
time_active = 5 # seconds

user = "<your-user>"
token = "<your-token>" # Create a token on your settings page https://jenkins/user/<your-user>/configure
url = "https://{}:{}@jenkins/api/json".format(user, token)

headers ={ 
    'crumb':'97f665ab9b00d1e16ca25e3a8b9af', # Take this for any request (Js console)
    'jenkins-crumb':'97f665ab9b00d1e16ca25e3a8b9af', 
    'content-type': 'application/json;charset=UTF-8',
}