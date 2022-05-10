import sys
import utils

slug = sys.argv[1]
email = sys.argv[2]

utils.append_email_hash(slug, email)