
# Use darth to setup the third-party packages folder
import darth
darth.vendor('lib')

# Set the default logging level
import logging
logging.getLogger().setLevel(logging.INFO)