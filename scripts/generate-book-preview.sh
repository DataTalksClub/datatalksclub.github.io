
# else nvm won't load
. ~/.nvm/nvm.sh
nvm use v10.17.0

cd previews

BOOK=$1

echo "book: ${BOOK}"

node render_book.js \
    ../_books/${BOOK}.md \
    ../images/books/${BOOK}/preview.jpg