def second_index(text: str, some_str: str) -> int or None:

  if text.count(some_str) <= 1:
    return None

  for_count_timer = 0
  result_second_index = -1

  while for_count_timer < 2:
    result_second_index = text.find(some_str,result_second_index+1)
    for_count_timer +=1

  return result_second_index

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'



