from typing import List, Tuple
from minsk_compiler.expression_syntax import ExpressionSyntax
from minsk_compiler.syntax_token import SyntaxToken


class SyntaxTree:
    diagnostics: Tuple[str, ...]
    root: ExpressionSyntax
    end_of_file_token: SyntaxToken

    def __init__(
        self,
        diagnostics: List[str],
        root: ExpressionSyntax,
        end_of_file_token: SyntaxToken,
    ):
        self.diagnostics = tuple(diagnostics)
        self.root = root
        self.end_of_file_token = end_of_file_token
