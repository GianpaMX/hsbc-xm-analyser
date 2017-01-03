
def parse(argv, defaultOutput, defaultConfig):
    output = defaultOutput
    config = defaultConfig

    inputFilenames = []

    i = 1
    while i < len(argv):
        if argv[i] in ['-c', '--config']:
            config.readFrom(argv[i + 1])
            i += 2
            continue

        if argv[i] in ['-o', '--output']:
            output = open(argv[i + 1], 'w')
            i += 2
            continue

        if not argv[i].startswith('-'):
            inputFilenames.append(argv[i])

        i += 1

    return inputFilenames, output, config