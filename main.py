import argparse
from book import Book

# Parse book_dir, description, and genre from command line
parser = argparse.ArgumentParser(description='Generate a book.')
parser.add_argument('--book_dir', type=str, help='The directory to store the book in')
parser.add_argument('--description', type=str, help='A description of the book')
parser.add_argument('--genre', type=str, help='The genre of the book')
args = parser.parse_args()

book = Book(args.book_dir, args.description, args.genre)
book_text = book.generate_book()
with open(os.path.join(args.book_dir, "book.txt"), "w") as f:
    f.write(book_text)

