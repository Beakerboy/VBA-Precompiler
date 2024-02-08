from vba_precompiler.vba_ccVisitor import vba_ccVisitor


class PrecompilerVisitor(vba_ccVisitor)

    def visitCcConst(self:T, ctx) -> None:
        """
        Add a new value to the environment variables
        and comment out the line in the source.
        """
        name = ctx.name
        if exists(self.env[name]):
            raise Exception("constant exists")
        value = visit(ctx.value)
        self.env.update({name : value})
        position = ctx.start
        # the CONST token is after the start
        ts.getToken(start + 1).text = "'" + ts.getToken(start + 1).text
    
    def visitOpExpr(self: T, ctx) -> int:
        """
        left = visit(ctx.expression[0])
        right = visit(ctx.expression[1])
        op = ctx.op.getText()
        switch (op.charAt(0)) {
            case '*': return left * right
            case '/': return left / right
            case '+': return left + right
            case '-': return left - right
            default: raise Exception("Unknown operator " + op)
        """
        return 0
        
    def visitRelExpr(self: T, ctx) -> bool:
        """
        left = visit(ctx.expression[0])
        right = visit(ctx.expression[1])
        op = ctx.op.getText()
        
        switch (op.charAt[0]) {
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
        """
        return False

    def visitStartRule(self: T, ctx) -> str:
        'visit each block
        this.visit(ctx.block);

        code = ""
        size = len(self.ts.tokens)
        i = 0
        for token in self.ts.tokens:
            if i + 1 < size:
                code += token.text
            i += 1
        return code

    def visitAtomExpr(self: T, ctx) -> Any:
        return Integer.valueOf(ctx.getText());

    def visitParenExpr(self: T, ctx) -> Any:
        return self.visit(ctx.expression)
