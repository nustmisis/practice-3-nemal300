# -*- coding: utf-8 -*-
"""
Напишите функцию которая на вход получает строку с госномером автомибиля и
выводит к какому типу относится данный госномер, или возвращает Fail! если это
не госномер.

Типы гос.номеров:

Тип |    Пример
----+----------
 1А | с227на 69
 1Б |  ао365 78
  2 | ан7331 47
  3 | 3733мм 55

Для корректной работы автоматических тестов не переименовывайте функцию
get_plate_type!
"""

import re


def get_plate_type(plate):
  regex_type_1a = r"^\w\d{3}\w{2}\s\d{2}$"
  regex_type_1b = r"^\w{2}\d{3}\s\d{2}$"
  regex_type_2 = r"^\w{2}\d{4}\s\d{2}$"
  regex_type_3 = r"^\d{4}\w{2}\s\d{2}$"

  if re.match(regex_type_3, plate):
      return "3"
  elif re.match(regex_type_1b, plate):
      return "1Б"
  elif re.match(regex_type_2, plate):
      return "2"
  elif re.match(regex_type_1a, plate):
      return "1А"
  return "Fail!"

