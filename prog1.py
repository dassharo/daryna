class Article:
    def __init__(self,
                 title,
                 descirption,
                 text):
        self.title = title
        self.description = descirption
        self.text = text

    def show(self):
        print(f"""Заголовок - {self.title}
Опис - {self.description}
Текст - {self.text}""")

article1 = Article("Стаття № 1",
                   "Опис статті № 1",
                   "Текст статті № 1")

article1.show()
