
# else nvm won't load
. ~/.nvm/nvm.sh
nvm use v10.17.0

cd previews

PODCAST=$1

echo "podcast: ${PODCAST}"

node render_podcast.js \
    ../_podcast/${PODCAST}.md \
    ../images/podcast/${PODCAST}.jpg