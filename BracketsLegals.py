from Stack import Stack


class BracketsLegals:

    def __init__(self):
        self.curly_brackets_stak = Stack()
        self.round_brackets_stak = Stack()
        self.square_brackets_stak = Stack()

    def brackets_string_isLegal(self, brackets_string):
        the_string_isLegal = True
        for s in brackets_string:
            if s == '(':
                self.round_brackets_stak.push(s)
            elif s == '[':
                self.square_brackets_stak.push(s)
            elif s == '{':
                self.curly_brackets_stak.push(s)
            elif s == ')':
                if self.round_brackets_stak.isNotEmpty():
                    self.round_brackets_stak.pop()
                else:
                    the_string_isLegal = False
                    break
            elif s == ']':
                if self.square_brackets_stak.isNotEmpty():
                    self.square_brackets_stak.pop()
                else:
                    the_string_isLegal = False
                    break
            elif s == '}':
                if self.curly_brackets_stak.isNotEmpty():
                    self.curly_brackets_stak.pop()
                else:
                    the_string_isLegal = False
                    break
            if self.three_stacks_is_empty():
                the_string_isLegal = True
            return the_string_isLegal

    def check_list(self, brackets_list):
        all_string_is_legal = True

        for brackets_string in brackets_list:
            if not self.brackets_string_isLegal(brackets_string):
                all_string_is_legal = False
                break
        if all_string_is_legal:
            print(f"all string is LEGAL = {all_string_is_legal}")
        return all_string_is_legal

    def three_stacks_is_empty(self):
        return self.square_brackets_stak.isEmpty() and self.curly_brackets_stak.isEmpty() and self.round_brackets_stak.isEmpty()
