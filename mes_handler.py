import vkapi
from xlrd import open_workbook
from xlutils.copy import copy



def create_answer(data, token):
   white_list_users = [''] # employee vk id
   key_hello = ['п', 'привет', 'пр', 'hi']
   name_employee = [''] #employee
   user_id = data['user_id']
   vkapi.send_message(adm_id_id, token, 'То Что Пришло в первый раз!!!! - ' + str(user_id) +'  '+ str(data['body']))
   if(str(user_id) not in white_list_users):
       vkapi.send_message(user_id, token, 'Вас нет в списке сотрудников!')
       return 0
   else:
       if(data['body'].lower() in key_hello):
          for i in range(len(white_list_users)):
              if(str(user_id) == white_list_users[i]):
                  message = 'Привет, ' + str(name_employee[i])
                  vkapi.send_message(user_id, token, message)
                  vkapi.send_message(user_id, token, 'ввод,Саша,ninebot,200 - Привер ввода!')
                  return 0
                  break

   key_money = str(data['body']).split(',')
   if(key_money[0].lower() == 'ввод'):
      answ(token,user_id,key_money)
      return 0
   else:
       vkapi.send_message(adm_id, token, 'Из некорректного ввода - ' + str(user_id) +'  '+ str(data['body']))
       vkapi.send_message(user_id, token, 'Некорректный ввод')
       # TODO Вывод помощи!!!



def answ(token,user_id,key_money):
    name_xls = ''  # you xls tables
    rb = open_workbook(name_xls)
    wb = copy(rb)
    read = rb.sheet_by_index(0)
    sheet = wb.get_sheet(0) # work
    if(len(key_money) == 4):
        sheet.write(read.nrows, 4 , key_money[1])
        sheet.write(read.nrows, 1 , key_money[2])
        sheet.write(read.nrows, 3 , key_money[3])
    else:
        sheet.write(read.nrows, 0 , key_money)
    wb.save(name_xls)
    vkapi.send_message(user_id, token, 'Записано, молодец!')
    vkapi.send_message(adm_id, token,  str(user_id))
    vkapi.send_message(adm_id, token, key_money)
