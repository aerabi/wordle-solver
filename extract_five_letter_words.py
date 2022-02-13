with open('usa.txt') as input_file:
    with open('five_letter_words.txt', 'w') as output_file:
        for line in input_file:
            if len(line.strip()) == 5:
                output_file.write(line)


