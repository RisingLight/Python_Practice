def formatting(sentence):
    sentence = list(sentence)
    for symbol in range(len(sentence) - 1):
        if sentence[symbol] == ' ':
            sentence[symbol] = ''
            sentence[symbol + 1] = sentence[symbol + 1].upper()

    sentence = ''.join(sentence)
    return sentence


def formatting_back(sentence):
    to_return = [sentence[0]]
    for symbol in sentence[1:]:
        if symbol == symbol.upper():
            to_return.append(' ')
            to_return.append(symbol.lower())
        else:
            to_return.append(symbol)
    to_return = ''.join(to_return)
    return to_return


def main():
    sentence = str(input('Enter yor string: '))
    formatted = formatting(sentence)
    print(f'Formatted: {formatted}')
    formatted_back = formatting_back(formatted)
    print(f'Formatted back: {formatted_back}')


if __name__ == '__main__':
    main()