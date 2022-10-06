# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
    Problem: https://www.hackerrank.com/challenges/simple-text-editor/problem
"""


def append_text(source_text, new_text):
    return source_text + new_text


def handle_append_text(source_text, new_text, stack):
    stack.append((pop_text, len(new_text)))
    return append_text(source_text, new_text)


def print_text(source_text, index_str):
    index = int(index_str) - 1
    print(source_text[index])
    return source_text


def pop_text(source_text, size_str):
    size = int(size_str)
    return source_text[:len(source_text) - size]


def handle_pop_text(source_text, size_str, stack):
    size = int(size_str)
    removed_chars = source_text[len(source_text) - size:]
    stack.append((append_text, removed_chars))
    return pop_text(source_text, size_str)


def undo_operation(source_text, stack):
    last_op = stack.pop()
    func, args = last_op[0], (arg for arg in last_op[1:])

    text = func(source_text, *args)
    return text


operations_map = {
    '1': handle_append_text,
    '2': handle_pop_text,
    '3': print_text,
    '4': undo_operation,
}

undo_operations = ('1', '2', '4')


def is_undo_allowed(op_text):
    return op_text in undo_operations


def parse_operation(operation_txt):
    operation = operation_txt.split()
    op, args = operation[0], (arg for arg in operation[1:])
    return op, args


def execute_editor(operations):
    text = ''
    stack = []
    for op_txt in operations:
        op, args = parse_operation(op_txt)
        func = operations_map[op]
        if is_undo_allowed(op):
            args = list(args)
            args.append(stack)

        text = func(text, *args)


def main():
    number_operations = int(input())
    operations = []
    for i in range(number_operations):
        operations.append(input())

    execute_editor(operations=operations)


if __name__ == "__main__":
    main()
