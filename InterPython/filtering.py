from filter_data import DATA


def run():
    # Filtering using list comprehensions
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    old_people = [{**worker, 'old': worker['age'] >= 70} for worker in DATA]
    adults = [worker['name'] for worker in DATA if worker['age'] >= 18]

    # Filtering using high order fxs
    all_python_devs_hof = list(filter(lambda worker: worker['language'] == 'python', DATA))
    all_python_devs_hof = list(map(lambda worker: worker['name'], all_python_devs_hof))

    all_platzi_workers_hof = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    all_platzi_workers_hof = list(map(lambda worker: worker['name'], all_platzi_workers_hof))

    adults_hof = list(filter(lambda worker: worker['age'] >= 18, DATA))
    adults_hof = list(map(lambda worker: worker['name'], adults_hof))

    old_people_hof = list(map(lambda worker: {**worker, 'old': worker['age'] >= 70}, DATA))
    
    print(all_python_devs == all_python_devs_hof)
    print(all_platzi_workers == all_platzi_workers_hof)
    print(adults == adults_hof)
    print(old_people == old_people_hof)


if __name__ == '__main__':
    run()