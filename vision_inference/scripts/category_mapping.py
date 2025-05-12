CATEGORY_MAPPING = {
    'bottle': 'Trash',
    'cup': 'Trash',
    'can': 'Trash',
    'wrapper': 'Trash',
    'plastic bag': 'Trash',
    'paper': 'Trash',
    'aluminium foil': 'Trash',
    'paper ball': 'Trash',

    'cell phone': 'Personal',
    'laptop': 'Personal',
    'id card': 'Personal',
    'wallet': 'Personal',
    'watch': 'Personal',
    'earphones': 'Personal',

    'pen': 'Personal',
    'pencil': 'Personal',
    'notebook': 'Personal',
    'scale': 'Personal',
    'eraser': 'Personal',
    'sharpener': 'Personal',

    'knife': 'Dangerous',
    'scissors': 'Dangerous',
    'blade': 'Dangerous',
    'electrical wire': 'Dangerous',
    'broken glass': 'Dangerous',

    'unknown': 'Unknown'
}

def map_category(detected_label):
    return CATEGORY_MAPPING.get(detected_label.lower(), 'Unknown')
