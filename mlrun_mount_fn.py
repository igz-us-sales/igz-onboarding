import sys
sys.path.append("/src/src_code")
import mymodule

def handler(context):
    mymodule.print_hi()
    
    name = context.get_param("name")
    context.logger.info(f'*****Hello from test.py, {name}!*****')