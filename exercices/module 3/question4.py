from datetime import datetime, timedelta

maintenant = datetime.now()
plus_100_heures = maintenant + timedelta(hours=100)

print(plus_100_heures)