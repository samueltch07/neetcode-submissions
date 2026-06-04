def concatenate(s1: str, s2: str) -> str:
    final_words = s1 + s2
    if(len(final_words) > 10):
        return "Too long!"
    return final_words   




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
