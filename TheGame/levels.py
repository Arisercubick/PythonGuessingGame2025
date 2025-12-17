

def levelSelect(level):
    levels = {
        'level1': {
            'array': ["New York", "Los Angeles", "Chicago", "Houston"],
            'question': "What is the largest city in the United States by population?",
            'answer': "New York"
        },
        'level2': {
            'array': ["Mercury", "Venus", "Earth", "Mars"],
            'question': "Which planet is known as the Red Planet?",
            'answer': "Mars"
        },
        'level3': {
            'array': ["Einstein", "Newton", "Galileo", "Curie"],
            'question': "Who developed the theory of relativity?",
            'answer': "Einstein"
        },
        'level4': {
            'array': ["Shakespeare", "Hemingway", "Fitzgerald", "Orwell"],
            'question': "Who wrote '1984'?",
            'answer': "Orwell"
        }
    }
    return levels[level]


def totalLevels():
    return 4
