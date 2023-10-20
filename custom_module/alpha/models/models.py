# -*- coding: utf-8 -*-

from odoo import models, fields, api


class User(models.Model):
     _name = 'alpha.user'
     _description = 'Model for users'

     name = fields.Char(string = 'Nombre', required = True)
     first_lastname = fields.Char(string = 'Apellido Paterno')
     second_lastname = fields.Char(string = 'Apellido Materno')
     phone = fields.Char(string = 'Teléfono')
     age = fields.Integer(string = 'Edad')
     gender = fields.Selection([
          ('masculine', 'Masculino'),
          ('femenine', 'Femenino')
     ], string = 'Género')
     groups = fields.Many2many('alpha.group', string = 'Grupos')

class Group(models.Model):
     _name = 'alpha.group'
     _description = 'Model for groups'

     group_id = fields.Char(string = 'Id del grupo', required = True)
     sport = fields.Selection([
          ('basket', 'Basketball'),
          ('futbol', 'Fútbol'),
          ('natation', 'Natación'),
          ('box', 'Box'),
          ('tenis', 'Tenis'),
          ('self_defense', 'Defensa personal')
     ], string = 'Deporte')
     date = fields.Date(string='Fecha')
     schedule = fields.Selection([
          ('6am', '6:00'),
          ('7am', '7:00'),
          ('8am', '8:00'),
          ('9am', '9:00'),
          ('10am', '10:00'),
          ('11am', '11:00'),
          ('12pm', '12:00'),
          ('13pm', '13:00'),
          ('14pm', '14:00'),
          ('15pm', '15:00'),
          ('16pm', '16:00'),
          ('17pm', '17:00'),
          ('18pm', '18:00'),
          ('19pm', '19:00'),
          ('20pm', '20:00'),
          ('21pm', '21:00'),
          ('22pm', '22:00'),
     ], string = 'Horario')
     campus = fields.Selection([
          ('alpha_uno', 'Alpha 1'),
          ('alpha_dos', 'Alpha 2'),
          ('alpha_tres', 'Alpha 3'),
          ('alpha_cuatro', 'Alpha 4')
     ], string = 'Sede')
     users = fields.Many2many('alpha.user', string = 'Usuarios')

     _sql_constraints = [
          ('group_id', 'unique(group_id)', "GroupId already exists with this value . GroupId must be unique!"),
     ]