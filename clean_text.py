def clean_up_text(file_name):
    with open(file_name) as f:

        # This line is from Zurich Okoren github
        punctuation_table = str.maketrans('\n-', '  ', '''1234567890~!@#$.,%^&*()_+?/`[];'":|♔''')

        mostly_filtered_text = f.read().translate(punctuation_table).replace('--', ' ')
        mostly_filtered_text = mostly_filtered_text.replace('\ufeff', '')
        text_list = mostly_filtered_text.lower().split()

        # This is how list comprehension work
        for index in range(len(text_list)):
            text_list[index] = text_list[index].strip()

        return text_list