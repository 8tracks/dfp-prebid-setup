import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
GOOGLEADS_YAML_FILE = os.path.join(ROOT_DIR, 'googleads.yaml')


#########################################################################
# DFP SETTINGS
#########################################################################

# A string describing the order
DFP_ORDER_NAME = "Prebid Generated Setup Web 2017-07-19"

# The email of the DFP user who will be the trafficker for
# the created order
DFP_USER_EMAIL_ADDRESS = "matthew.cieplak@gmail.com"

# The exact name of the DFP advertiser for the created order
DFP_ADVERTISER_NAME = "AppNexus"
PREBID_BIDDER_CODE = 'appnexusAst'

# Names of placements the line items should target.
DFP_TARGETED_PLACEMENT_NAMES = ["Prebid_Web"]

# Sizes of placements. These are used to set line item and creative sizes.
DFP_PLACEMENT_SIZES = [
  {
    'width': '300',
    'height': '250'
  },
  {
    'width': '300',
    'height': '600'
  },
  {
    'width': '728',
    'height': '90'
  },
  {
    'width': '970',
    'height': '90'
  },
  {
    'width': '970',
    'height': '250'
  }
]

PREBID_PRICE_BUCKETS = 'PREBID_PRICE_BUCKETS'

# Whether we should create the advertiser in DFP if it does not exist.
# If False, the program will exit rather than create an advertiser.
DFP_CREATE_ADVERTISER_IF_DOES_NOT_EXIST = False

# If settings.DFP_ORDER_NAME is the same as an existing order, add the created 
# line items to that order. If False, the program will exit rather than
# modify an existing order.
DFP_USE_EXISTING_ORDER_IF_EXISTS = True

# Optional
# Each line item should have at least as many creatives as the number of 
# ad units you serve on a single page because DFP specifies:
#   "Each of a line item's assigned creatives can only serve once per page,
#    so if you want the same creative to appear more than once per page,
#    copy the creative to associate multiple instances of the same creative."
# https://support.google.com/dfp_sb/answer/82245?hl=en
#
# This will default to the number of placements specified in
# `DFP_TARGETED_PLACEMENT_NAMES`.
# DFP_NUM_CREATIVES_PER_LINE_ITEM = 2

# Optional
# The currency to use in DFP when setting line item CPMs. Defaults to 'USD'.
# DFP_CURRENCY_CODE = 'USD'

#########################################################################
# PREBID SETTINGS
#########################################################################

DFP_NUM_CREATIVES_PER_LINE_ITEM = 4

# Price buckets. This should match your Prebid settings for the partner. See:
# http://prebid.org/dev-docs/publisher-api-reference.html#module_pbjs.setPriceGranularity
# FIXME: this should be an array of buckets. See:
# https://github.com/prebid/Prebid.js/blob/8fed3d7aaa814e67ca3efc103d7d306cab8c692c/src/cpmBucketManager.js
# PREBID_PRICE_BUCKETS = {
#   'precision': 2,
#   'min' : 0.12,
#   'max' : 2.00,
#   'increment': 0.02,
# }

# PREBID_PRICE_BUCKETS = {
#   'precision': 2,
#   'min' : 2.10,
#   'max' : 10,
#   'increment': 0.10,
# }

PREBID_PRICE_BUCKETS = {
  'precision': 2,
  'min' : 10.25,
  'max' : 35,
  'increment': 0.25,
}




#########################################################################

# Try importing local settings, which will take precedence.
try:
    from local_settings import *
except ImportError:
    pass
