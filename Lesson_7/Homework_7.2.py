def correct_sentence(sentences: str) -> str:

    sentences = sentences.split(".")
    sentences = [s.strip() for s in sentences]
    sentences = [s.capitalize() for s in sentences]
    sentences = ". ".join(sentences)
    sentences = sentences.strip()

    if sentences[-1] != ".":
        sentences = sentences + "."

    return sentences


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'


