    grammar Baby_Duck;


    @parser::header {
from MyFunctions import *
    }

    programa: {functionGoto()} PROGRAM  {setScope("global")} ID SEMICOLON   vars*  (funcs)*  MAIN {pJumpF()}  body_end  <EOF>;

    body_end: OPEN_KEY {addKey()} (statement)* CLOSE_KEY {closeKey()}  {solveQuadruples()};

    statement: assign | condition | cycle | f_call | print_;
    
    assign: ID EQUAL expresion {assignExpression($ID.text)} SEMICOLON;

    vars: (VAR ID {saveVariable($ID.text)} (COMMA ID {saveVariable($ID.text)} )*  COLON TYPE {saveType($TYPE.text)}  SEMICOLON);

    vars_func: (VAR ID {saveVariableLocal($ID.text)} (COMMA ID {saveVariableLocal($ID.text)} )*  COLON TYPE {saveTypeLocal($TYPE.text)}  {insertVariablesLocales()} {insertQuadCount()} SEMICOLON);

    funcs:  (VOID | TYPE) ID {saveFunction($ID.text, $TYPE.text)} {setScope($ID.text)} OPEN_PAREN {addParenthesis()} (ID COLON TYPE {saveParameter($ID.text, $TYPE.text)} (COMMA ID COLON TYPE {saveParameter($ID.text, $TYPE.text)})*)? CLOSE_PAREN {closeParenthesis()} {insertParameters()} OPEN_BRACKET {addBrackets()} (vars_func)* body CLOSE_BRACKET {closeBrackets()} {endScopeVars()} {setScope("global")} SEMICOLON;

    f_call: ID {proveFunction($ID.text)} OPEN_PAREN {generateERA()} {addParenthesis()} (expresion {arguments()} (COMMA {addK()} expresion {arguments()})*)? CLOSE_PAREN {closeParenthesis()} {isNull()} SEMICOLON;

    print_: (PRINT_WORD  OPEN_PAREN {addParenthesis()} {addPrint()} (expresion | STRING {saveString($STRING.text)}) {printExp()} (COMMA {addPrint()} (expresion | STRING {saveString($STRING.text)}) {printExp()})*  CLOSE_PAREN {closeParenthesis()} SEMICOLON);

    condition: IF OPEN_PAREN {addParenthesis()} expresion CLOSE_PAREN {closeParenthesis()} {csTrue()} body (ELSE {GOTO()} body)? SEMICOLON {pJumpF()};

    cycle: WHILE {whileLoop()} OPEN_PAREN {addParenthesis()} expresion  CLOSE_PAREN  {closeParenthesis()} {expresionWhile()} body SEMICOLON {endWhile()};

    body: OPEN_KEY {addKey()} (statement)* CLOSE_KEY {closeKey()};


    factor: (OPEN_PAREN {addParenthesis()} expresion CLOSE_PAREN {closeParenthesis()}) | ((ADD |SUB )? (CTE {stackConstant($CTE.text)}| ID {stackId($ID.text)}));

    termino: ((factor {multDiv()} ((MULT {addMultDiv($MULT.text)}) | (DIV {addMultDiv($DIV.text)}) ))* factor {multDiv()});

    exp:  (termino {sumRes()} ((ADD {addSumSub($ADD.text)}) | (SUB {addSumSub($SUB.text)}) ))* termino {sumRes()};

    expresion: (exp {compareExp()} (TYPE_CONDITIONAL {addCompare($TYPE_CONDITIONAL.text)}))* exp {compareExp()};
    
    

    TYPE_CONDITIONAL: GREATER | LESS | DIFFERENT;
    TYPE: INT | FLOAT;
    CTE: [0-9]+ | DECIMAL;

    FLOAT: 'float';
    INT: 'int';

    VAR: 'var';
    MAIN: 'main';
    VOID: 'void';
    PROGRAM: 'program';
    WHILE: 'while';
    DO: 'do';
    IF: 'if';
    ELSE: 'else';
    PRINT_WORD: 'print';

    OPEN_PAREN: '(';
    CLOSE_PAREN: ')';
    OPEN_KEY: '{';
    CLOSE_KEY: '}';
    OPEN_BRACKET: '[';
    CLOSE_BRACKET: ']';

    MULT: '*';
    DIV: '/';
    EQUAL: '=';
    ADD: '+';
    SUB: '-';
    GREATER: '>';
    LESS: '<';
    DIFFERENT: '!=';
    DOT: '.';
    COMMA: ',';
    SEMICOLON: ';';
    COLON: ':';

    ID: '_'? LETTER (LETTER | NUMBER | '_')*;
    LETTER: [a-zA-Z];
    DECIMAL:  NUMBER+ DOT  NUMBER+;
    NUMBER: [0-9];
    STRING: '"' .*? '"';

    WS: [ \t\r\n]+ -> skip;
