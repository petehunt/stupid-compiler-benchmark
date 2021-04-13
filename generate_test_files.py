def generate_java(name):
    lines = []
    lines.append('class %s {' % name)
    lines.append('  public static void main(String[] args) {')
    for i in range(1000):
        lines.append('    System.out.println("Hello world %d");' % i)
    lines.append('  }')
    lines.append('}')
    return '\n'.join(lines)

def generate_ts():
    lines = []
    for i in range(1000):
        lines.append('console.log("Hello world %d");' % i)
    return '\n'.join(lines)

def generate_golang(name):
    lines = []
    lines.append('package main')
    lines.append('import "fmt"')
    lines.append('func %s() {' % name)
    for i in range(1000):
        lines.append('    fmt.Println("Hello world %d")' % i)
    lines.append('}')
    return '\n'.join(lines)

for i in range(50):
    with open('ts/hello%d.ts' % i, 'w') as f:
        f.write(generate_ts())
    with open('java/Hello%d.java' % i, 'w') as f:
        f.write(generate_java('Hello%d' % i))
    with open('golang/hello%d.go' % i, 'w') as f:
        if i == 0:
            name = 'main'
        else:
            name = 'hello%d' % i
        f.write(generate_golang(name))
