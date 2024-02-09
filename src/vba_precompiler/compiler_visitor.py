from typing import TypeVar
from vba_precompoler.vba_ccParser import vba_ccParser as Parser
from vba_precompiler.vba_ccVisitor import vba_ccVisitor


T = TypeVar('T', bound='PrecompilerVisitor')


class PrecompilerVisitor(vba_ccVisitor):

    def visitCcConst(self: T,  # noqa: N802
                     ctx: Parser.CcConstContext) -> None:
        """
        Add a new value to the environment variables
        and comment out the line in the source.
        """
        # name = ctx.name
        name = "Win16".upper()
        if name not in self.env:
            raise Exception("constant exists")
        value = self.visit(ctx.value)
        self.env.update({name: value})
        position = ctx.start
        # the CONST token is after the start
        ts.getToken(start + 1).text = "'" + ts.getToken(start + 1).text
    
    def visitOpExpr(self: T,  # noqa: N802
                    ctx: Parser.OpExprContext) -> int:
        """
        left = visit(ctx.expression[0])
        right = visit(ctx.expression[1])
        op = ctx.op.getText()
        switch (op.getText()) {
            case '*': return left * right
            case '/': return left / right
            case '+': return left + right
            case '-': return left - right
            default: raise Exception("Unknown operator " + op)
        """
        return 0
        
    def visitRelExpr(self: T,  # noqa: N802
                     ctx: Parser.RelExprContext) -> bool:
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

    def visitStartRule(self: T,  # noqa: N802
                       ctx: Parser.StartRuleContext) -> str:
        # visit each block
        this.visit(ctx.block);

        code = ""
        size = len(self.ts.tokens)
        i = 0
        for token in self.ts.tokens:
            if i + 1 < size:
                code += token.text
            i += 1
        return code

    def visitAtomExpr(self: T,  # noqa: N802
                      ctx: Parser.AtomExprContext) -> Any:
        return Integer.valueOf(ctx.getText());

    def visitParenExpr(self: T,  # noqa: N802
                       ctx: Parser.ParenExprContext) -> Any:
        return self.visit(ctx.expression)
