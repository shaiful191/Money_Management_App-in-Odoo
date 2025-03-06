from odoo import models,fields,api 

class MoneyEntry(models.Model):
  _name = 'money.entry'
  _description='Money Entry'


  name = fields.Char(string='Description',required=True)
  date = fields.Char(string='Date',default=fields.Date.today)
  amount = fields.Float(string='Amount',required=True)
  type = fields.Selection(
          [
            ('income','Income'),
            ('expense','Expense')
          ],
          string='Type',
          required=True
  )
