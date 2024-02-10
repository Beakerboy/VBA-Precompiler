from typing import Any, Dict, TypeVar
from vba_precompiler.grammar.vba_ccLexer import vba_ccLexer as Lexer
from vba_precompiler.grammar.vba_ccParser import vba_ccParser as Parser
from vba_precompiler.grammar.vba_ccVisitor import vba_ccVisitor


T = TypeVar('T', bound='PrecompilerVisitor')


class PrecompilerVisitor(vba_ccVisitor):
    NO_COMMENT = 0
    NO_COMMENT_FOUND_TRUE = 1
    COMMENT_FOUND_TRUE = 2
    COMMENT_NOT_FOUND_TRUE = 3
    COMMENT_ALL = 4

    def __init__(self: T) -> None:
        super().__init__()
        self.lines: list = []
        self.env: Dict[str, Any] = {}
        # stack for logical line comment status
        self.com_line_stk = [self.NO_COMMENT]

    def visitCcConst(self: T,  # noqa: N802
                     ctx: Parser.CcConstContext) -> None:
        """
        Add a new value to the environment variables
        and comment out the line in the source.
        """
        name = ctx.getChild(2).getText().upper()
        if name in self.env:
            raise Exception("constant exists: " + name)
        value = self.visit(ctx.getChild(4))
        self.env.update({name: value})
        const_token = ctx.getChild(1)
        self.lines.append(const_token.symbol.line)

    def visitCcIf(self: T,  # noqa: N802
                  ctx: Parser.CcIfContext) -> None:
        if_token = ctx.getChild(1)
        # comment out the ccif line
        self.lines.append(if_token.symbol.line)
        expression = self.visit(ctx.getChild(4))
        if self.com_line_stk[-1] > self.NO_COMMENT_FOUND_TRUE:
            self.com_line_stk.append(self.COMMENT_ALL)
        elif expression:
            self.com_line_stk.append(self.NO_COMMENT_FOUND_TRUE)
        else:
            self.com_line_stk.append(self.COMMENT_NOT_FOUND_TRUE)
        

    def visitCcEndif(self: T,  # noqa: N802
                     ctx: Parser.CcEndifContext) -> None:
        const_token = ctx.getChild(1)
        self.lines.append(const_token.symbol.line)
        self.com_line_stk.pop()

    def visitLogicalLine(self: T,  # noqa:N802
                         ctx: Parser.LogicalLineContext) -> None:
        if self.com_line_stk[-1] > self.NO_COMMENT_FOUND_TRUE:
            newline_token = ctx.getChild(0)
            self.lines.append(token.symbol.line + 1)
    
    def visitCcIfBlock(self: T,  # noqa: N802
                       ctx: Parser.CcIfBlockContext) -> None:
        self.visitChildren(ctx)
    
    def visitArithmeticExpression(  # noqa: N802
            self: T,
            ctx: Parser.ArithmeticExpressionContext
    ) -> int:
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

    def visitRelationExpression(self: T,  # noqa: N802
                                ctx: Parser.RelationExpressionContext) -> bool:
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

    def visitStartRule(  # noqa: N802
            self: T,
            ctx: Parser.StartRuleContext
    ) -> list:
        super().visitStartRule(ctx)

        return self.lines

    def visitLiteralExpress(  # noqa: N802
            self: T,
            ctx: Parser.LiteralExpressContext
    ) -> Any:
        if ctx.start.type == Lexer.BOOLEANLITERAL:
            return ctx.start.text.upper() == 'TRUE'
        return 0

    def visitParenthesizedExpression(  # noqa: N802
            self: T,
            ctx: Parser.ParenthesizedExpressionContext
    ) -> Any:
        return self.visit(ctx.getChild(1))
