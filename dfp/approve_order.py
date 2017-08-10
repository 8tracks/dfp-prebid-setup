#!/usr/bin/env python

import logging

from googleads import dfp

import settings

from dfp.client import get_client
from dfp.exceptions import BadSettingException, MissingSettingException


logger = logging.getLogger(__name__)


def approve_order(order_id):
  
  # APPROVE ORDER
  values = [{
      'key': 'orderId',
      'value': {
          'xsi_type': 'NumberValue',
          'value': order_id
      }
  }]
  query = 'WHERE orderId = :orderId'
  statement = dfp.FilterStatement(query, values)
  
  dfp_client = get_client()
  order_service = dfp_client.GetService('OrderService', version='v201702')
    

  result = order_service.performOrderAction(
        {'xsi_type': 'ApproveOrders'}, statement.ToStatement())
  logger.info('Approved an order with id "{id}"'.format(
         id=order_id))


  return order_id
