import re
import operator
import collections

Token = collections.namedtuple("Token", ["type", "val"])
Op = collections.namedtuple("Op", ["fn", "prec"])

N, LP, RP, OP = ("N", "LP", "RP", "OP")


class Tokenizer:
    def __init__(self, expr):
        self.expr = expr
        self.re_token = re.compile(r"\s*(?:(\d+)|(.))")
        self.tokens = self._tokenize()
        self.current = None

    def eat(self):
        try:
            self.current = next(self.tokens)
        except StopIteration:
            self.current = None
        return self.current

    def _tokenize(self) -> iter:
        for n, op in self.re_token.findall(self.expr):
            if n:
                yield Token(N, n)
            elif op == "(":
                yield Token(LP, op)
            elif op == ")":
                yield Token(RP, op)
            else:
                yield Token(OP, op)


def get_atom(tokenizer: Tokenizer, ops: dict):
    t = tokenizer.current
    assert t != None
    assert t.type != OP
    if t.type == LP:
        tokenizer.eat()
        val = get_expr(tokenizer, ops)
        assert tokenizer.current.type == RP
        tokenizer.eat()
        return val
    else:
        tokenizer.eat()
        return int(t.val)


def get_expr(tokenizer: Tokenizer, ops: dict, min_prec=1):
    lhs = get_atom(tokenizer, ops)
    while True:
        t = tokenizer.current
        if t is None or t.type != OP or ops[t.val].prec < min_prec:
            break

        op = t.val
        fn, prec = ops[op]
        eat_min_prec = prec + 1

        tokenizer.eat()
        rhs = get_expr(tokenizer, ops, eat_min_prec)
        lhs = fn(lhs, rhs)
    return lhs


def compute(expr: str, ops: dict):
    tokenizer = Tokenizer(expr)
    tokenizer.eat()
    return get_expr(tokenizer, ops)


with open("input", "r") as f:
    exprs = [line.strip() for line in f.readlines()]

    ops = {
        "+": Op(operator.add, 1),
        "*": Op(operator.mul, 1),
    }

    evaluation = [compute(expr, ops) for expr in exprs]
    print(sum(evaluation))

    ops = {
        "+": Op(operator.add, 2),
        "*": Op(operator.mul, 1),
    }

    evaluation = [compute(expr, ops) for expr in exprs]
    print(sum(evaluation))
