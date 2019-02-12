"""
string_util.py

Misc. string processing functions
"""

def title_case(sentence):
    """
    Convert a string to title case.

    Title case means that the first character of every word is capitalized.

    Parameters
    ----------
    sentence : string
        String to be converted to title case


    Returns
    -------
    output : string
        Input string in title case

    Examples
    --------
    >>> title_case(ThIs iS a StRingG tO be COnvERted.)
        'This Is a String To Be Converted.'
    """

    # Check input is string
    if not isinstance(sentence, str):
        raise TypeError("Invaid input %s - Input must be a string." % (sentence))

    # Error if empty string
    if not sentence:
        raise ValueError("Input should not be empty.")

    word_list = sentence.split(" ")

    output = [word_list[0].capitalize()]

    for word in word_list[1:]:
        output.append(word.capitalize())

    return " ".join(output)
