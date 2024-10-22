class Text():
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class Comment(Text):
    def __init__(self, text, comment):
        super().__init__(text)
        self.comment = comment

    def __str__(self):
        return f'{super().__str__()} - {self.comment}'

    def __repr__(self):
        return 'Служебная информация'


comment = Text('Привет')
comment_2 = Comment('Ола!', 'Учусь ООП')

print(comment_2)
print(repr(comment_2))
print(f'{comment_2!r}')