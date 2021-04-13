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

for i in range(50):
    with open('ts/hello%d.ts' % i, 'w') as f:
        f.write(generate_ts())
    with open('java/Hello%d.java' % i, 'w') as f:
        f.write(generate_java('Hello%d' % i))
