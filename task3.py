# def is_balanced(expression):
#     """Перевіряє симетричність розділювачів у рядку"""
#     stack = []
#     brackets = {')': '(', '}': '{', ']': '['}

#     for char in expression:
#         if char in brackets.values():  # Якщо відкриваючий символ
#             stack.append(char)
#         elif char in brackets.keys():  # Якщо закриваючий символ
#             if not stack or stack[-1] != brackets[char]:  # Перевірка відповідності
#                 return "Несиметрично"
#             stack.pop()  # Видаляємо парний відкриваючий символ зі стеку

#     return "Симетрично" if not stack else "Несиметрично"

# # Тестові рядки
# test_expressions = [
#     "( ){[ 1 ]( 1 + 3 )( ){ }}",  # Симетрично
#     "( 23 ( 2 - 3);",  # Несиметрично
#     "( 11 }"  # Несиметрично
# ]

# # Перевірка результатів
# for expr in test_expressions:
#     print(f"{expr}: {is_balanced(expr)}")