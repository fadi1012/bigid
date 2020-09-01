import random
import json
import names
import os
from datetime import datetime

allocated_id_list = []
cities_list = ['haifa', 'tlv', 'herzliya']
TASK_DIR = os.path.abspath(os.curdir)


class MockPersonalData:
    def __init__(self, email, first_name, last_name, city, country, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.country = country
        self.id = id


def generate_random_id():
    while True:
        id = str(random.randint(100000000, 900000000))
        if not id in allocated_id_list:
            allocated_id_list.append(id)
            break
    return id


def generate_mock_personal_data(num_of_identities_to_create=100, country="israel", city=None):
    num_of_identities_to_create = num_of_identities_to_create * 100
    random_full_name = names.get_full_name()
    email = 'user' + str(random.randint(0, num_of_identities_to_create)) + '@bigid.com'
    first_name = random_full_name.split(" ")[0].strip()
    last_name = random_full_name.split(" ")[1].strip()
    city = city or random.choice(cities_list)
    id = generate_random_id()
    return MockPersonalData(email=email, first_name=first_name, last_name=last_name, city=city, country=country,
                            id=id).__dict__


def main():
    identities_list = []
    num_of_identities_to_create = int(input("Please enter the requested number of identities"))
    for i in range(num_of_identities_to_create):
        mock_personal_data = generate_mock_personal_data(num_of_identities_to_create)
        identities_list.append(mock_personal_data)
    json_data = json.dumps(identities_list)
    print(json_data)
    json_file_path = TASK_DIR + f'/mock_users_data_{datetime.now().strftime("%H-%M-%S")}.json'
    open(json_file_path, 'w').write(json_data)
    print(f"Please see generated json file {json_file_path}")


if __name__ == "__main__":
    main()
