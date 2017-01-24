class Vaccum:
    def vaccuum_reflex(self, location,state):
        if state == 'dirty':
            return 'Suck'
        else:
            if location == 'a':
                return 'Go Right'
            else:
                return 'Go Left'

vaccum = Vaccum()

location = input("Enter the location")
state = input("Enter the state")

location = location.lower()
state = state.lower()


print(vaccum.vaccuum_reflex(location, state))
