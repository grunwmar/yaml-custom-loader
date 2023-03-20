from tag import Tag
from custom_loader import CustomLoader


@CustomLoader.set(alias="chapter")
class Chapter(Tag): 
    def string(self): return self.__repr__()


@CustomLoader.set(alias="label")
class Label(Tag): 
    def string(self): return self.__repr__()


@CustomLoader.set(alias="text")
class Text(Tag): 
    def string(self): return self.__repr__()


jd = CustomLoader.load_file("yaml_document.yaml")
print(jd)

"""
print:

    {
        'title': !Text(en='Book', cs='Kniha'), 
        'meta': {
            'languages': ['en', 'cs']
            }, 
    'content': [
        !Chapter(
                !Label('Label I.'), 
                !Text(en='English paragraph one.', cs='Český odstavec jedna.'), 
                !Text(en='English paragraph two.', cs='Český odstavec dva.')
            )
        ]
    }

"""