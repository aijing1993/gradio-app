import os
os.system('sudo -S chmod +x /home/ubuntu/genai-20240825')
os.chdir('/home/ubuntu/genai-20240825/workspace/v2v_conda_pipeline')
os.system("bash run_app.sh")