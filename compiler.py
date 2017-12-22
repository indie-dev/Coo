import sys as sys
import os as os


#Lex interpreter
def lex(file, content):
    content = list(content)
    token = ""
    for code in content:
        token += code
        if token == " ":
            token = ""
        elif ";" in token:
            token = token.replace(";", "")
        elif "{" in token:
            token = token.replace("{", ":\n\t")
        elif "uses" in token:
            token = token.replace("uses", "import")
        elif "}" in token:
            token = token.replace("}", "")
        elif ">>" in token:
            token = token.replace(">>", ".")
        elif "obj" in token:
            token = token.replace("obj", "def")
        elif "ends_with" in token:
            token = token.replace("ends_with", "replace")
        elif "with" in token:
            token = token.replace("with", "while")
        elif "str" in token:
            print("'str' variable is unknown")
        elif "for" in token:
            token = token.replace("for", "while")
        elif "pr_out" in token:
            token = token.replace("pr_out", "print")
        elif "fopen" in token:
            token = token.replace("fopen", "open")
    file.write(token)
    file.write("main("+str(sys.argv)+")")
def compile(file_path):
    code = open(file_path, "r")
    tmp = open(os.path.dirname(file_path)+"bin/"+os.path.splitext(file_path)[0]+".bin", "w")
    footer = ""
    lex(tmp, code.read())
    tmp.flush()
    tmp.close()

def compile_all(filepath):
    println("Compiling all sources")
    for dirname, dirnames, filenames in os.walk('.'):
        # print path to all subdirectories first.

        # print path to all filenames.
        for filename in filenames:
            if ".coo" in filename:
                compile(filename)

def println(line):
    #Check if the user is asking for no output
    if "--no-noise" not in sys.argv:
        print(line)

def error(line):
    println("Coo ERR: "+line)

#Compile the source code into .bin file
def compile_src(file_path):
    if not os.path.isdir(os.path.dirname(file_path)):
        os.system("mkdir bin")
    
    compile(file_path)

    os.system("python "+os.path.dirname(file_path)+"bin/"+os.path.splitext(file_path)[0]+".bin")
    compile_all(os.path.dirname(file_path))
    if "--delete-bin" in sys.argv:
        os.system("rm "+os.path.dirname(file_path)+"bin/"+os.path.splitext(file_path)[0]+".bin")


def get_proj(ring):
    try:
        compile_src(ring)
    except Exception as e:
        print("IO"+str(e))

get_proj(sys.argv[1])