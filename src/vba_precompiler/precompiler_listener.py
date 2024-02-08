from vba_precompiler.vba_ccVisitor import vba_ccVisitor


class PrecompilerVisitor(vba_ccVisitor)

    def visitOpExpr(self: T, ctx) -> int:
        left = visit(ctx.expression(0))
        right = visit(ctx.expression(1))
        op = ctx.op.getText()
        switch (op.charAt(0)) {
            case '*': return left * right
            case '/': return left / right
            case '+': return left + right
            case '-': return left - right
            default: raise Exception("Unknown operator " + op)

    def visitRelExpr(self: T, ctx) -> bool:
        left = visit(ctx.expression(0))
        right = visit(ctx.expression(1))
        op = ctx.op.getText()
        
        switch (op.charAt(0)) {
            case '<': return left < right
            case '>': return left > right
            case '=': return left == right
            case '<>': pass
            case '><': return left != right
            case '>=': pass
            case '=>': return left >= right
            case '<=': pass
            case '=<': return left <= right
            default: raise Exception("Unknown operator " + op)
    def visitStartRule(self: T, ctx) -> None:
        'visit each block
        return this.visit(ctx.expr());

    def visitAtomExpr(self: T, ctx) -> Any:
        return Integer.valueOf(ctx.getText());

    def visitParenExpr(self: T, ctx) -> Any:
        return self.visit(ctx.expr())
