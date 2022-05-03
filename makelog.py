import sys
gitlog_perline = []
for l in sys.stdin:
    gitlog_perline.append(l)
print(gitlog_perline)
gitlog_written = ""
for line in gitlog_perline:
    line_newline = line + '\n'
    gitlog_written += line_newline
written = "\\begin{flushleft}\n\\tt\n" + gitlog_written + "\n\\end{flushleft}\n"
with open("/Users/hfunakura/Documents/NOTE/notes_on_formal_semantics/commitlog.tex", "w") as file:
    file.write(written)