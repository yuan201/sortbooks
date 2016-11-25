import parser


class BookSorter:
    """
    BookSorter main program.
    Call this program to sort ebooks based on keywords from
    book name.
    Subcommands:
    1. scan [target_folder]
        to scan a folder and all its subfolders with classified
        books. The closest folder name will be taken as type name
        and keywords from book names will be stored as keywords
        for the type. Some common keywords will be ignore such as
        'a', 'the', etc. Keywords found in multiple folders will
        also be ignored.
    2. sort [source_folder]
        sort unclassified books based on keywords found during 
        scanning. Books are not moved during sort. The result of
        sorting will be recorded in the report file specified.
        Books failed to be automatically sorted will be recorded
        too so it can be mannually edited.
    3. move [source_folder] [target_folder]
        actually move the books accoring to sorting reports.
        Successful moving will remove the record in the report file.
        Several iteration of edit and move can be repeated until all
        books are moved to proper folder.
    """
    def run(self):
        """main command"""
        pass

    def scan(self):
        """perform the scan command"""
        pass
        
    def sort(self):
        """perform the sort command"""
        pass
        
    def move(self):
        """perform the move command"""
        pass
    
    def __init__(self):
        # self.parse = parser.


if __name__ == "__main__":
    bs = BookSorter(*args)
    bs.run()
