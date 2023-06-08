https://eastlakeside.gitbook.io/interpy-zh/c_extensions

https://www.w3cschool.cn/python3/python3-enbl2pw9.html

https://algo.itcharge.cn/


https://www.cnblogs.com/wongbingming/articles/12384764.html

-------------------------------------------------------------------------------------
import os
import subprocess

# 复制当前进程的环境变量
env = os.environ.copy()

# 更新需要修改的环境变量
env['MY_VAR'] = 'my_value'

# 使用subprocess.run执行命令，并传递env参数
subprocess.run(['my_command'], env=env)

-------------------------------------------------------------------------------------


注意一下adb shell后面命令中的引号问题，我觉得有这个可能是这个原因