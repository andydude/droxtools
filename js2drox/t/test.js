
function testFor() {
    var i;
    for (i = 0; i < 5; i++) {
        print(i);
    }
}

function testForIn() {
    var i, ls = [1, 2, 3];
    for (i in ls) {
        print(i);
    }
}

function testForVar() {
    for (var i = 0; i < 5; i++) {
        print(i);
    }
}

function testForVarIn() {
    var ls = [1, 2, 3];
    for (var i in ls) {
        print(i);
    }
}

function testArrayInit() {
    var ls = [1, 2, 3];
    return ls;
}

function testObjectInit() {
    var ob = {
        a: 'b',
        c: 'd',
        e: 'f'};
    return ob;
}

function testIfExp(cond) {
    return cond ? "yes" : "no";
}

function testThink() {
    return (function(){
        return null;
    })();
}

function testBlock() {
    var x = 3;
    {
        print("what");
    }
    return x;
}

function testEmpty() {
    var x = 2;
    ;;
    return;
}

function testSwitchCase(a) {
    switch (a) {
    case 1:
        print("1");
    case 2:
        print("2");
    default:
        print("d");
    }
    return 0;
}

function testSwitchCond() {
    if (1) {
        2;
    } else if (3) {
        4;
    } else if (5) {
        6;
    } else {
        7
    }
}

function testIn(a) {
    return a in testArrayInit();
}

function testInstanceOf(a) {
    return a instanceof Object;
}

function testNewArgs(a) {
    return new Object(a);
}

function testNew(a) {
    return new Object;
}

function testDelete(a) {
    delete a[0];
}

function testWhile(a) {
    while (true) {
        return 1;
    }
    return a;
}

function testDoWhile(a) {
    do testWhile(a); while (false);
    return a;
}

function testTry(a) {
    try {
        print(a);
    } catch (e) {
        print(e);
    } finally {
        print("hi");
    }
}
