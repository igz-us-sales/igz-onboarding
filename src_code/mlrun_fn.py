def handler(context):
    name = context.get_param("name")
    context.logger.info(f'*****Hello from MLRun, {name}!*****')
    
    value = context.get_param("value")
    context.log_result("value", value)