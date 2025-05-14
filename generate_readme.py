import os
import ast
import subprocess

def extract_functions(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        node = ast.parse(file.read())
    return [n.name for n in node.body if isinstance(n, ast.FunctionDef)]

def generate_readme(base_dir):
    readme_path = os.path.join(base_dir, 'README.md')
    with open(readme_path, 'w', encoding='utf-8') as readme:
        readme.write('# 📝 Daily Coding Functions Index\n\n')
        
        for entry in sorted(os.listdir(base_dir)):
            dir_path = os.path.join(base_dir, entry)
            if os.path.isdir(dir_path) and entry.startswith('2025_'):
                readme.write(f"## 📅 {entry}\n")
                py_files = sorted([f for f in os.listdir(dir_path) if f.endswith('.py')])
                
                for idx, file_name in enumerate(py_files, start=1):
                    label = f"{entry}" if idx == 1 else f"{entry}({idx})"
                    readme.write(f" - {label}\n")
                    
                    file_path = os.path.join(dir_path, file_name)
                    func_names = extract_functions(file_path)
                    
                    for func in func_names:
                        readme.write(f"   -- def {func}(...):\n")
                readme.write('\n')

def commit_and_push(readme_path):
    subprocess.run(['git', 'add', readme_path], check=True)
    subprocess.run(['git', 'commit', '-m', '자동 업데이트: README.md 함수 목록 최신화'], check=False)
    subprocess.run(['git', 'push'], check=False)

def main():
    base_dir = 'code'
    generate_readme(base_dir)
    commit_and_push(os.path.join(base_dir, 'README.md'))

if __name__ == '__main__':
    main()
