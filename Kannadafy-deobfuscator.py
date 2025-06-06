import ast
import astor  # pip install astor
import os
import sys
import io

class ExecReplacer(ast.NodeTransformer):
    def visit_Expr(self, node):
        # Replace exec(...) with print(...)
        if isinstance(node.value, ast.Call) and getattr(node.value.func, 'id', '') == 'exec':
            node.value.func.id = 'print'
        return self.generic_visit(node)

def reveal_exec_from_file(filename):
    if not os.path.exists(filename):
        print(f"[!] File '{filename}' not found.")
        return

    with open(filename, "r", encoding="utf-8") as f:
        source = f.read()

    try:
        tree = ast.parse(source)
    except Exception as e:
        print(f"[!] Failed to parse script: {e}")
        return

    # Replace exec with print
    tree = ExecReplacer().visit(tree)
    ast.fix_missing_locations(tree)
    modified_code = astor.to_source(tree)

    # Save modified version of the script
    revealed_filename = f"revealed_{os.path.basename(filename)}"
    with open(revealed_filename, "w", encoding="utf-8") as f:
        f.write(modified_code)

    print(f"[*] Modified script saved as: {revealed_filename}")
    print(f"[*] Running modified script to extract deobfuscated output...")

    # Capture printed output
    original_stdout = sys.stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output

    try:
        exec(compile(tree, filename="<ast>", mode="exec"))
    except Exception as e:
        print(f"[!] Error while running modified code: {e}")

    sys.stdout = original_stdout
    result = captured_output.getvalue()
    captured_output.close()

    # Save deobfuscated content
    base_name = os.path.splitext(os.path.basename(filename))[0]
    deobf_filename = f"deobfuscated_{base_name}.py"
    with open(deobf_filename, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"[*] Deobfuscated output saved to: {deobf_filename}")

if __name__ == "__main__":
    filename = input("Enter the Python script to analyze: ").strip()
    reveal_exec_from_file(filename)
