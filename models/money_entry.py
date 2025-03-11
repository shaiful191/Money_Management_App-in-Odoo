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

  balance = fields.Float(compute = '_compute_balance', string='Balance',readonly=True)

  @api.depends('type','amount')
  def _compute_balance(self): 
      
      all_records = self.env['money.entry'].search([])

      total_income = sum(all_records.filtered(lambda r: r.type == 'income').mapped('amount'))
      total_expenses = sum(all_records.filtered(lambda r: r.type == 'expense').mapped('amount'))
 
      for record in self:
          record.balance = total_income - total_expenses

  def get_balance2(self):
     
     all_records = self.env['money.entry'].search([])

     total_income = sum(all_records.filtered(lambda r: r.type == 'income').mapped('amount'))
     total_expenses = sum(all_records.filtered(lambda r: r.type == 'expense').mapped('amount'))
     balance = total_income - total_expenses
     return {
        'type': 'ir.actions.client',
        'tag':'display_notification',
        'params': {
            'title': 'Current Balance',
            'message': f'Your current balance is {balance}',
            'sticky': False
        }
     } 