def veteran_age_statistics(birth_years: list[int], current_year: int = 2025) -> tuple[dict[str, int], str, float, dict[str, float]]:
  ret_dic = {}
  dic_key = ['100+', '90-99', '80-89', '70-79', '60-69', '-59']
  for index in dic_key:
    ret_dic[index] = 0
  sumage = 0
  for index in birth_years:
    age = (current_year - index + 1)
    sumage += age
    if age < 60:
      ret_dic['-59'] += 1
    elif age < 70:
      ret_dic['60-69'] += 1
    elif age < 80:
      ret_dic['70-79'] += 1
    elif age < 90:
      ret_dic['80-89'] += 1
    elif age < 100:
      ret_dic['90-99'] += 1
    else:
      ret_dic['100+'] += 1
  percent_dic = {}
  for index in dic_key:
    percent_dic[index] = round((ret_dic[index] / len(birth_years)) * 100, 1)
  return (ret_dic, max(ret_dic, key=lambda x : ret_dic[x]), sumage / len(birth_years), percent_dic)

birth_years = [1930, 1935, 1940, 1945, 1955, 1965, 1975, 1985, 1923, 1919, 2000]
stats, most_common_group, average, percent = veteran_age_statistics(birth_years)
print(stats)
print("가장 많은 연령대:", most_common_group)
print("평균 연령:", average)
print("비율:", percent)