units: dict = {
    "Algorithmiques et Programmation-2": {
        "Programmation JAVA": (
            (
                (20.00, 0.6),
                (18.50, 0.4),
            ),
            2,
        ),
        "Programmation Python": (
            (
                (18.25, 0.6),
                (20, 0.4),
            ),
            2,
        ),
        "Théorie des langages": (
            (
                (14.75, 0.6),
                (17, 0.4),
            ),
            1,
        ),
    },
    "Langues, Communication et Culture d'Entreprises-2": {
        "English communication - 2": (
            (
                (15.00, 0.6),
                (15.50, 0.4),
            ),
            1,
        ),
        "Techniques de communication - 2": (
            (
                (11.50, 0.6),
                (14.00, 0.4),
            ),
            1,
        ),
    },
    "Réseaux et Systèmes d'exploitation-2": {
        "Réseaux IP-2": (
            (
                (13.00, 0.6),
                (15.50, 0.4),
            ),
            2,
        ),
        "Systèmes d'exploitation Linux-2": (
            (
                (18.25, 0.6),
                (19.5, 0.4),
            ),
            2,
        ),
    },
    "Sciences Fondamentales-2": {
        "Probabilités, Statistique et Processus aléatoires": (
            (
                (06.00, 0.6),
                (15.00, 0.4),
            ),
            2,
        ),
        "Théorie des graphes": (
            (
                (14.50, 0.6),
                (15.00, 0.4),
            ),
            1,
        ),
    },
    "Système d'Information-2": {
        "Développement Web JavaScript EC6": (
            (
                (17.00, 0.6),
                (19.00, 0.4),
            ),
            2,
        ),
        "Gestion de versions décentralisé": (
            (
                (17.00, 0.6),
                (20.00, 0.4),
            ),
            1,
        ),
        "Modélisation UML": (
            (
                (11.75, 0.6),
                (11.00, 0.2),
                (8, 0.2),
            ),
            2,
        ),
    },
}

total: list[float] = []
maxi, mini = {"": float("-inf")}, {"": float("+inf")}
for unit in units:
    unit_avg = []
    for subject, notes in units[unit].items():
        avg = sum([note[0] * note[1] for note in notes[0]]) * notes[1]
        print(
            "\033[91m" + subject,
            ":\033[94m",
            "(\033[93m",
            "\033[92m + \033[93m".join(
                [f"{note[0]} \033[92m*\033[93m {note[1]}" for note in notes[0]]
            ),
            f"\033[94m) \033[92m*\033[93m {notes[1]} " f"= {avg:.2f}",
        )
        if list(maxi.values())[0] <= (avg / notes[1]):
            maxi = {subject: avg / notes[1]}

        if list(mini.values())[0] >= (avg / notes[1]):
            mini = {subject: avg / notes[1]}

        unit_avg.append((avg, notes[1]))
    tot = sum(x[0] for x in unit_avg)
    print(
        "\033[95m--------->\033[94m",
        unit,
        ":\033[92m",
        "\033[93m + \033[92m".join([f"{note[0]}" for note in unit_avg]),
        f"\033[93m= {tot:.2f}\033[0m",
    )
    total.append((tot, sum(x[1] for x in unit_avg)))

print(
    "\033[95m Average is :",
    "\033[94m(\033[93m",
    " \033[92m+\033[93m ".join([f"{note[0]:.2f}" for note in total]),
    f"\033[94m) \033[92m/\033[93m {sum(x[1] for x in total)} \033[92m=\033[93m {sum(x[0] for x in total) / sum(x[1] for x in total):.2f}\033[0m",
)

print(
    "\033[95m (MIN) :",
    "\033[94m(\033[93m",
    f" \033[92m {list(mini.keys())[0]} : {list(mini.values())[0]:.2f} \033[0m",
)

print(
    "\033[95m (MAX) :",
    f" \033[92m {list(maxi.keys())[0]} : {list(maxi.values())[0]:.2f} \033[0m",
)
