import json
import os.path
import re
import shutil


class BookType:    

    def __init__(self, type, keywords, folder):
        self.type = type
        self.keywords = keywords
        self.folder = folder

    def __repr__(self):
        return "BookType({0.type!r}, {0.keywords!r}, {0.folder!r})".format(self)


NONE_KEYWORDS = ['pdf', 'to', 'the']
    
class Book:

    class UnknownType(exception):
        pass
    
    def __init__(self, path, type=None):
        self.path = path
        self.type = type

    @property
    def name(self):
        return os.path.basename(self.path)

    def keywords(self):
        words = re.findall('\w+', self.name)
        return [w.lower() for w in words if w not in NONE_KEYWORDS]
    
    def _move_to(self, folder):
        target = os.path.join(folder, self.name)
        shutil.move(self.path, target)
        self.path = target

    def move(self):
        if self.type is None:
            raise self.UnknownType
        self._move_to(self.type.folder)
        
        
class Classifier:

    class CannotClassify(exception):
        pass

    class UnknownType(exception):
        pass
    
    def __init__(self, jsonfile):
        self.booktypes = []
        self.keywords = {}
        self.jsonfile = jsonfile
        
    def classify(self, book):
        for w in book.keywords:
            if w in self.keywords:
                book.type = keywords[w]
                return
        raise self.CannotClassify(book.name)
                
    def remove_keyword(self, w):
        self.keywords[w].keywords.delete(w)
        self.keywords.delete(w)
    
    def remove_duplicate_keywords(self, book):
        for w in book.keywords:
            if w in self.keywords and self.keywords[w] != book.type:
                self.remove_keyword(w)
    
    def load_types(self):
        with open(self.jsonfile) as f:
            types = json.load(f)
            for type, info in types.items():
                keywords = info['keywords'].split(',')
                self.booktypes.append(cls(type, keywords, info['folder']))
                for w in keywords:
                    self.keywords[w] = self.booktypes[-1]

    def dump_types(self):
        """dump all types to JSON file"""
        pass

    def update_keywords(self, book):
        """update keywords by a book with known type"""
        if book.type not in self.booktypes:
            raise self.UnknownType(book.type)
