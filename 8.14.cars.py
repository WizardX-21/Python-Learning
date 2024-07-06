def make_car(manufacturer,model,**other_info):
  car_detail = {}
  car_detail['Manufacturer-Name'] = manufacturer
  car_detail['Model-Name'] = model
  for key,value in other_info.items():
    car_detail[key] = value
  return car_detail
car = make_car('subaru','outback',color = 'blue', tow_package = 'True')
print(car)
  