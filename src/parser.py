def parse(line):
    line = line.strip()
    if not line:
        return []

    commands = []
    for part in line.split("|"):
        part = part.strip()
        if part:
            tokens = []
            current = ""
            in_quotes = False
            quote_char = ""

            for char in part:
                if char in ('"', "'") and not in_quotes:
                    in_quotes = True
                    quote_char = char
                elif char == quote_char and in_quotes:
                    in_quotes = False
                    quote_char = ""
                elif char == " " and not in_quotes:
                    if current:
                        tokens.append(current)
                        current = ""
                else:
                    current += char

            if current:
                tokens.append(current)

            if tokens:
                commands.append(tokens)

    return commands