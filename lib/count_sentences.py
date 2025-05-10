#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self.value = value  # Uses the property setter
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if not isinstance(value, str):
            print("The value must be a string.")
            self._value = ""
        else:
            self._value = value
    
    def is_sentence(self):
        return self._value.endswith(".") if self._value else False
    
    def is_question(self):
        return self._value.endswith("?") if self._value else False
    
    def is_exclamation(self):
        return self._value.endswith("!") if self._value else False
    
    def count_sentences(self):
        if not self._value:
            return 0
        # Split on sentence-ending punctuation, keeping delimiters
        sentences = [s for s in self._value.replace("!", ".").replace("?", ".").split(".") if s.strip()]
        return len(sentences)