import logging

from googleads import dfp

from dfp.client import get_client

logger = logging.getLogger(__name__)

def activate_line_items(line_item_ids):
  """
  Activates line items in DFP.

  Args:
    line_item_ids (arr): an array of numbers, each a line item id
  Returns:
    an array: an array of approved line item IDs
  """
  dfp_client = get_client()
  line_item_service = dfp_client.GetService('LineItemService', version='v201702')

  line_items_activated = 0
  for line_item_id in line_item_ids:
    # APPROVE ORDER
    values = [{
        'key': 'id',
        'value': {
            'xsi_type': 'NumberValue',
            'value': line_item_id
            #'value': ', '.join([str(i) for i in line_item_ids])
        }
    }]
    query = 'WHERE id in (:id)'
    statement = dfp.FilterStatement(query, values)
    
    #Approve line items
    result = line_item_service.performLineItemAction(
        {'xsi_type': 'ActivateLineItems'}, statement.ToStatement())

    if result and int(result['numChanges']) > 0:
      line_items_activated += int(result['numChanges'])
  
  # Display results.
  if line_items_activated > 0:
    logger.info('Number of line items activated: %s' % line_items_activated)
  else:
    logger.info('No line items were activated.')


  return line_item_ids

