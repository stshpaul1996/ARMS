# playground/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import subprocess

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def run_code(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        code = data.get('code')
        language = data.get('language')
        user_input = data.get('input')

        if language == 'python':
            command = ['python3', '-c', code]
        elif language == 'java':
            with open('Main.java', 'w') as f:
                f.write(code)
            command = ['javac', 'Main.java']  # Compile Java code
            subprocess.run(command, capture_output=True, text=True)
            command = ['java', 'Main']
        elif language == 'dotnet':
            with open('Program.cs', 'w') as f:
                f.write(code)
            command = ['dotnet', 'run']
        else:
            return JsonResponse({'output': 'Unsupported language'}, status=400)

        try:
            result = subprocess.run(command, input=user_input, capture_output=True, text=True, timeout=10)
            output = result.stdout if result.returncode == 0 else result.stderr
        except subprocess.TimeoutExpired:
            output = 'Error: Code execution timed out'
        except Exception as e:
            output = str(e)

        return JsonResponse({'output': output})

    return JsonResponse({'output': 'Invalid request'}, status=400)
