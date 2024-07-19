## Homework_7.1
Написати функцію say_hi, яка представить людину за переданими параметрами.

Вхідні дані: Два аргументи рядок(str) та позитивне число(int)

Функція має повернути рядок.

Замініть pass на Ваше рішення.

def say_hi(name, age):
  pass

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'

assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'


## Homework_7.2
На вхід функції correct_sentence передається два речення. Необхідно повернути їх виправлену копію так, щоб вони завжди починалися з великої літери та закінчувалися крапкою.

Зверніть увагу, що не всі виправлення необхідні. Якщо речення вже закінчується крапкою, додавати ще одну не потрібно, це буде помилкою

Вхідні аргументи: string.

Вихідні аргументи: string.

Замість pass необхідно написати Ваше рішення.

def correct_sentence(text):
     pass 

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'

assert correct_sentence("hello") == "Hello.", 'Test2' 

assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3' 

assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4' 

assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'

## Homework_7.3

Функція second_index приймає як параметри 2 рядки. Вам необхідно знайти індекс другого входження шуканого рядка у рядку для пошуку.

Розберемо перший приклад, де необхідно знайти друге входження "s" в слові "sims". Якби нам треба було знайти її перше входження, то тут все просто: за допомогою функції index або find ми можемо дізнатися, що "s" - це перший символ у слові "sims", а значить індекс першого входження дорівнює 0. Але нам Необхідно визначити другу "s", а вона четверта за рахунком. Значить індекс другого входження (і у відповідь питання) дорівнює 3.

Рядок, який потрібно знайти, може складатися з кількох символів.

Input: Два рядки (String).

Output: Int or None

Приклади:

def second_index(text, some_str): 
  pass 

assert second_index("sims", "s") == 3, 'Test1' 

assert second_index("find the river", "e") == 12, 'Test2' 

assert second_index("hi", "h") is None, 'Test3' 

assert second_index("Hello, hello", "lo") == 10, 'Test4'


## Homework_7.4

Напишіть функцію common_elements, яка згенерує два списки елементів з генераторного виразу (range) для 100 елементів, за наступними правилом:

Один список з числами кратними 3, інший з кратними числами 5.

За допомогою множин створіть набір з числами, які є в обох множинах (перетин).

Функція повинна повернути цю множину як результат своєї роботи.

Приклади

def common_elements():
    pass

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
